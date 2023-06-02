from django.urls import path
from . import views

urlpatterns = [
    path("trigger-etl/", views.trigger_etl_view, name="trigger_etl"),
]
