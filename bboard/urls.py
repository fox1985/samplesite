"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import index, by_rubric, add_and_save
#---------------------------------------
from .mix import  BbCreateView, BbIindexView, BbDetailView, BbRubricView, BbEditView, BbDeleteView
#------------------------------------------------------------------------------------------------------------
#Чтобы реализовать на своем сайте процедуру  аутентификации (входа),
from django.contrib.auth.views import LoginView

# Контроллер PasswordChangeView:смена пароля
from django.contrib.auth.views import PasswordChangeDoneView

#Контроллер PasswordResetView: отправка письма для сброса пароля
from django.contrib.auth.views import PasswordResetView

# Контроллер PasswordResetConfirm View: собственно сброс пароля
from django.contrib.auth.views import PasswordResetConfirmView

#Контроллер PasswordResetCompleteView: уведомление об успешном сбросе пароля
from django.contrib.auth.views import PasswordResetCompleteView


urlpatterns = [
    #path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    #path('', index, name='ndex'),
    #path('add/', add_and_save, name='add'),#добавить обявения

    #------------------------------------------------------------------

    path('', BbIindexView.as_view(), name='index'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),# загаловак статьи делат ссылкой спереходом на статью

    path('<int:rubric_id>/', BbRubricView.as_view(), name='by_rubric'),# левое меню рубрики

    path('<int:<int:pk>/', BbEditView.as_view(), name='edit'),# редактировать статью

    path('add', BbCreateView.as_view(), name='add'),  # добавить обявения

    path('delete/<int:pk>/', BbDeleteView.as_view(), name='del'),  # удалить запись

    #-----------------------------------------------------------------------------------
    #Контроллер LogoutView. выход с сайта
    path('accounts/login/', LoginView.as_view(), name='logout'),
    # Контроллер Password ChangeView: смена пароля
    path('accounts/password_change/', PasswordChangeDoneView.as_view(template_name='registration/change_password.html'), name='password_change' ),
    #Контроллер PasswordChangeDone View: уведомление об успешной смене пароля
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'), name='password_change_done'),
    # Контроллер PasswordResetView: отправка письма для сброса пароля
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='registration/reset_password.html',subject_template_name='email/reset_subject.txt', email_template_name='registration/reset_email.html'), name='password_reset'),
    #Контроллер PasswordResetDoneView: уведомление об отправке письма для сброса пароля
    path('accounts/password_reset/done/', PasswordResetView.as_view(template_name='registration/email_sent.html'), name='password_reset_done'),
    # Контроллер PasswordResetConfirm View: собственно сброс пароля
    path('accounts/reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='registration/confirm_password.html'), name='password_reset_confirm' ),
    #Контроллер PasswordResetCompleteView: уведомление об успешном сбросе пароля
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_confirmed.html'), name='password_reset_complete'),




]
