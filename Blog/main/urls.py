from django.urls import path
from . import views

urlpatterns = [
    path('', views.postView.as_view()),

]