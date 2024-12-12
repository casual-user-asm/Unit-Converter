from django.urls import path
from .views import home

app_name = "converter"
urlpatterns = [path("", home, name="home")]
