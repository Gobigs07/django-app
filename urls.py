from django.urls import path
from .views import db_check

urlpatterns = [
    path("db-check/", db_check),
]
