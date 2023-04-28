from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class AuthenticateUserAPIView(generics.GenericAPIView):

    def get(self, request):
        return Response({"message":"test"})