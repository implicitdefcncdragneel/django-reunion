from django.urls import path
from api.account.views import AuthenticateUserAPIView,FollowUnfollowAPIView
from api.post.views import PostCreateAPIView,PostDeleteAPIView,get_all_post
from api.services.views import CommentAPIView,ReactionAPIView,get_post

urlpatterns = [
    path("authenticate/",AuthenticateUserAPIView.as_view(),name="authenticate-user"),
    path("follow/<str:id>/",FollowUnfollowAPIView.as_view(),name="follow-user"),
    path("unfollow/<str:id>/",FollowUnfollowAPIView.as_view(),name="unfollow-user"),
    path("user/",FollowUnfollowAPIView.as_view(),name="no-followers-following"),
    path("posts/", PostCreateAPIView.as_view(), name="create-post"),
    path("posts/<str:id>/", PostDeleteAPIView.as_view(), name="delete-post"),
    path("like/<str:id>/", ReactionAPIView.as_view(), name="like-post"),
    path("unlike/<str:id>/", ReactionAPIView.as_view(), name="unlike-post"),
    path("comment/<str:id>/", CommentAPIView.as_view(), name="comment-post"),
    path("post/<str:id>/", get_post, name='get-post'),
    path("all_posts/", get_all_post, name='get-all-post'),
]
