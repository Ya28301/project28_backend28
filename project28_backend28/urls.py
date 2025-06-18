
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


from django.contrib import admin
from django.urls import path, include  # ← نضيف include هنا

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # روابط التطبيقات الجديدة
    path('core/', include('core.urls')),
    path('content/', include('content.urls')),
    path('interactions/', include('interactions.urls')),
]
