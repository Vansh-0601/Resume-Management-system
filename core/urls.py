from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import ResumeDetail

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/resumes/', views.resume_api, name='resume_api'),
    path('delete/<int:resume_id>/', views.delete_resume, name='delete_resume'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('download/<int:resume_id>/', views.download_pdf, name='download_pdf'),
    path('api/resumes/<int:pk>/', ResumeDetail.as_view(), name='resume-detail'),
]
