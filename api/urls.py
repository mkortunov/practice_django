from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ActorDetail.as_view()),
    path('', ActorList.as_view()),
]


