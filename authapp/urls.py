from django.urls import path
from .views import edit, dashboard, register,form_submission,index
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'authapp'

urlpatterns = [
    path('',index,name='index'),
    path('register/', register, name='register'),
    #  path('form/', views.form_submission, name='form'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/form', form_submission, name='form'),
    path('dashboard/submit-form/', views.form_submission, name='form_submission'),
    path('dashboard/proposal/inbox/', views.proposal_inbox, name='proposal_inbox'),
    path('dashboard/status/', views.status_page, name='status_page'),
    path('dashboard/save/', views.save_page, name='save_page'),
    path('dashboard/form-details/<str:reference_number>/', views.form_details, name='form_details'),
    path('dashboard/success/', views.success_page, name='success_page'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)