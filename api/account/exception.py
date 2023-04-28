from rest_framework.exceptions import APIException

class CantFollowYourself(APIException):
    default_detail = "You cannot follow yourself!"