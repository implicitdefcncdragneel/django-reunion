from django.urls import path
from api.account.views import AuthenticateUserAPIView

urlpatterns = [
    path("authenticate/",AuthenticateUserAPIView.as_view(),name="authenticate-user"),
]
