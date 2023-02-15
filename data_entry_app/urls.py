from django.urls import path
from data_entry_app.views import RegisterApi


urlpatterns = [
    path("api/register", RegisterApi.as_view()),
]
