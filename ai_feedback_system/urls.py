from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('feedback.urls')),   # 👈 VERY IMPORTANT
    path('admin/', admin.site.urls),
]
