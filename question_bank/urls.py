from django.contrib import admin
from django.urls import path
from question import views as question_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/question/', question_views.QuestionAPI.as_view(), name="question_url"),
    path('api/user', user_views.UserAPI.as_view(), name="user_url"),
]
