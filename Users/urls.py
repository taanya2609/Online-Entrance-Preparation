from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('result/', views.GetResult, name='get-result'),
    path('index/', views.GetUserLists, name='admin-index'),
    path('users/', views.GetUserLists, name='user-details'),
    path('exams/', views.GetExamsLists, name='exam-details'),
    path('user-search/', views.UserSearch, name='user-search'),
    path('exam-search/', views.ExamSearch, name='exam-search'),
    path('feedbacks/', views.GetFeedbackLists, name='feedback'),
    path('reports/', views.GetReportsLists, name='report-lists'),
    path('questions/', views.GetQuestionLists, name='questions'),
    path('add-question/', views.AddQuestion, name='add-question'),
    path('subjects/', views.GetSubjectLists, name='subject-details'),
    path('report-search/', views.ReportSearch, name='report-search'),
    path('report/<str:id>/mark', views.MarkReport, name="mark-report"),
    path('delete-account/', views.DeleteAccount, name='delete-account'),
    path('update-profile/', views.UpdateProfile, name='update-profile'),
    path('subject-search/', views.SubjectSearch, name='subject-search'),
    path('users/edit-user/<str:id>', views.EditUsers, name="edit-user"),
    path('model-test/<program>', views.TakeModelTest, name='model-test'),
    path('update-password/', views.UpdatePassword, name='update-password'),
    path('feedback-search/', views.FeedbackSearch, name='feedback-search'),
    path('question-search/', views.QuestionSearch, name='question-search'),
    path('feedback/<str:id>/mark', views.MarkFeedBack, name="mark-feedback"),
    path('programmes/', views.GetProgrammeLists, name='getProgrammeDetails'),
    path('program-selector/', views.ProgramSelector, name='program-selector'),
    path('report/edit-report/<str:id>', views.EditReports, name='edit-report'),
    path('model-test/<str:programme>/<str:subject>', views.GetSpecificQuestions),
    path('subject/edit-subject/<str:id>', views.EditSubject, name='edit-subject'),
    path('report-question/<str:id>', views.ReportQuestions, name='report-question'),
    path('feedback/edit-feedback/<str:id>', views.EditFeedback, name='edit-feedback'),
    path('questions/edit-question/<str:id>', views.EditQuestions, name="edit-question"),
    path('detailed-result/<slug:slug>', views.DetailedHistory, name='detailed-history'),
    path('admin-change-password/', views.AdminChangePassword, name='admin-change-password'),
    path('questions/edit-question/<str:id>/delete', views.DeleteQuestion, name="delete-question"),
    path('report-question/<str:id>/added', views.DisplayReportedQuestion, name='report-question-added'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='FindAccount.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetView.as_view(template_name='ResetPasswordSent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='NewPassword.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='RecoverPasswordComplete.html'), name='password_reset_complete'),
    path('<str:redirect_to>/', views.GoTo, name='go_to'),
]
