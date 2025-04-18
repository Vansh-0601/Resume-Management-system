from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Resume
import PyPDF2, re, os


@login_required
def home(request):
    if request.method == 'POST':
        pdf = request.FILES['pdf']
        reader = PyPDF2.PdfReader(pdf)
        text = ''.join([page.extract_text() for page in reader.pages if page.extract_text()])

        resume = Resume.objects.create(
            user=request.user,
            pdf=pdf,
            name=text.split('\n')[0][:50],
            email=re.search(r'[\w\.-]+@[\w\.-]+', text).group() if re.search(r'[\w\.-]+@[\w\.-]+', text) else '',
            phone=re.search(r'\+?\d[\d\s\-]{8,}\d', text).group() if re.search(r'\+?\d[\d\s\-]{8,}\d', text) else '',
            skills=', '.join([s for s in ['python', 'django', 'postgresql', 'react', 'html', 'css'] if s in text.lower()]),
            resume_file=pdf  # Save the file to both fields
        )
        return redirect('home')
    
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'core/home.html', {'resumes': resumes})

@login_required
def upload_resume(request):
    if request.method == 'POST':
        pdf = request.FILES['pdf']
        reader = PyPDF2.PdfReader(pdf)
        text = ''.join([page.extract_text() for page in reader.pages if page.extract_text()])

        Resume.objects.create(
            user=request.user,
            pdf=pdf,
            name=text.split('\n')[0][:50],
            email=re.search(r'[\w\.-]+@[\w\.-]+', text).group() if re.search(r'[\w\.-]+@[\w\.-]+', text) else '',
            phone=re.search(r'\+?\d[\d\s\-]{8,}\d', text).group() if re.search(r'\+?\d[\d\s\-]{8,}\d', text) else '',
            skills=', '.join([s for s in ['python', 'django', 'sql', 'react', 'html', 'css'] if s in text.lower()]),
            resume_file=pdf
        )
        return redirect('upload_resume')
    
    return render(request, 'core/upload.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@csrf_exempt
def resume_api(request):
    resumes = Resume.objects.all().values('id', 'name', 'email', 'phone', 'skills')
    return JsonResponse(list(resumes), safe=False)

@csrf_exempt
def delete_resume(request, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id)
        resume.delete()
        return JsonResponse({'message': 'Resume deleted successfully!'}, status=200)
    except Resume.DoesNotExist:
        return JsonResponse({'error': 'Resume not found!'}, status=404)

def admin_view(request):
    resumes = Resume.objects.all()
    return render(request, 'core/admin_resumes.html', {'resumes': resumes})

def download_pdf(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    file_path = resume.pdf.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))

class ResumeDetail(APIView):
    def delete(self, request, pk):
        try:
            # Fetch the resume by ID
            resume = Resume.objects.get(pk=pk)
            resume.delete()  # Delete the resume from the database
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Resume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
