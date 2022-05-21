from django.urls import path
from .views import get_all_branch

urlpatterns = [
    path('', get_all_branch, name = "get_all_branch"),
]
