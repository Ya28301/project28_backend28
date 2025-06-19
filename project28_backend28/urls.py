from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # مسار الصفحة الرئيسية
    path('content/', include('content.urls')),  # مسار صفحات المحتوى
    path('interactions/', include('interactions.urls')),  # مسار التفاعل
]
