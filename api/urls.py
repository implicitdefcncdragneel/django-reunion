from django.urls import path
from api.account.views import AuthenticateUserAPIView,FollowUnfollowAPIView
from api.post.views import PostCreateAPIView,PostDeleteAPIView

urlpatterns = [
    path("authenticate/",AuthenticateUserAPIView.as_view(),name="authenticate-user"),
    path("follow/<str:id>/",FollowUnfollowAPIView.as_view(),name="follow-user"),
    path("unfollow/<str:id>/",FollowUnfollowAPIView.as_view(),name="unfollow-user"),
    path("user/",FollowUnfollowAPIView.as_view(),name="no-followers-following"),
    path("posts/", PostCreateAPIView.as_view(), name="create-post"),
    path("posts/<str:id>/", PostDeleteAPIView.as_view(), name="delete-post"),
]
