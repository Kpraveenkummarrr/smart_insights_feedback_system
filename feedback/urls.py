from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('submit/', views.submit_feedback, name='submit'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('delete/<int:id>/', views.delete_feedback, name='delete'),
    path('export/', views.export_csv, name='export'),
]
