from django.urls import path
from . import views
from .views import CreateownCV

urlpatterns = [
    path('', CreateownCV.as_view(), name="createCV"),
]