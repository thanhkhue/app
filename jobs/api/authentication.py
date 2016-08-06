from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


def get_api_token(request):
    ''' Use to get API token from authenticated user '''
    UserModel = get_user_model()
    user = UserModel.objects.get(username=request.user.username)
    token, created = Token.objects.get_or_create(user=user)
    return token.key
