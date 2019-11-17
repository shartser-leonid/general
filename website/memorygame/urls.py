from django.urls import path

from . import views

app_name = 'memorygame'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_screen/', views.login_screen, name='login_screen'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('question/',views.question,name='question'),
    path('question/question_process/',views.question_process ,name='question/question_process'),
    path('question/question_answer/',views.question_answer ,name='question/question_answer'),
    path('user/',views.user_session ,name='user'),
    path('server/',views.server ,name='server'),
    path('program_view/', views.program_view, name='program_view'),
    path('program_activate/<int:user_prog_id>/', views.program_activate, name='program_activate'),
    path('program_progress/<int:user_prog_id>/', views.program_progress, name='program_progress'),
    path('program_report/<int:id>/', views.program_report, name='program_report')
    
    ]
 