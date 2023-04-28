from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import generics,status,permissions
from api.account.exception import CantFollowYourself

from api.account.models import User

from api.account.serializers import AuthenticateUserSerializer, FollowingSerializer, MyTokenObtainPairSerializer

# Create your views here.
class AuthenticateUserAPIView(generics.GenericAPIView):

    serializer_class = AuthenticateUserSerializer

    def post(self, request):
        serializer=AuthenticateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            try:
                data={}
                _user_id=User.objects.get(email=serializer.data["email"])
                _token=MyTokenObtainPairSerializer
                refresh = _token.get_token(_user_id)
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)
                return Response(data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(str(e))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUnfollowAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowingSerializer

    def get(self, request):
        try:
            specific_user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            raise NotFound("User with that username does not exist")

        following_list = specific_user.following_list()
        followers_list = specific_user.followers_list()
        foserializer = FollowingSerializer(following_list, many=True)
        frserializer = FollowingSerializer(followers_list, many=True)
        return Response({"user_name":specific_user.email,"following": foserializer.data,"followers":frserializer.data}, status=status.HTTP_200_OK)

    def post(self, request, id):
        try:
            specific_user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise NotFound("User with that id does not exist")

        if specific_user.id == request.user.id:
            raise CantFollowYourself
            
        user_instance = User.objects.get(id=specific_user.id)
        current_user_profile = request.user

        if current_user_profile.check_following(user_instance):
            return Response(f"You already follow {specific_user.email}", status=status.HTTP_400_BAD_REQUEST)

        current_user_profile.follow(user_instance)
        return Response(f"You now follow {specific_user.email}", status=status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            specific_user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise NotFound("User with that id does not exist")
        user_instance = User.objects.get(id=specific_user.id)
        current_user_profile = request.user
        if not current_user_profile.check_following(user_instance):
            return Response(f"You do not follow {specific_user.email}", status=status.HTTP_400_BAD_REQUEST)
        current_user_profile.unfollow(user_instance)
        return Response(f"You have unfollowed {specific_user.email}", status=status.HTTP_200_OK)