from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authen', views.obtain_auth_token),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)