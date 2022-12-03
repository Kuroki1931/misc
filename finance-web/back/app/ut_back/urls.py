from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('authen/', include('djoser.urls.jwt')),
    path('', include('accounts.urls')),
    path('accounts/password_change_form/', views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change_form'),
    path('accounts/password_change_done/', views.PasswordChangeDoneView.as_view(template_name='registration/password_change_finish.html'), name='password_change_done'),
    path('accounts/password_reset_form/', views.PasswordResetView.as_view(template_name='registration/password_reset.html', from_email=' office54@office54.net '), name='password_reset'),
    path('accounts/password_reset_done/', views.PasswordResetDoneView.as_view(template_name='registration/password_reset_mail_done.html'), name='password_reset_done'),
    path('accounts/password_reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirmation.html'), name='password_reset_confirm'),
    path('accounts/password_reset_finish/', views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_finish.html'), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)