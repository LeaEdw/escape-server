from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    try:
        new_user = User.objects.create_user(
            username = request.data["username"],
            password = request.data["password"],
            email = request.data["email"],
            first_name = request.data["first_name"],
            last_name = request.data["last_name"],
            is_admin = request.data.get('is_admin', False),
        )
        token = Token.objects.create(user=new_user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data["username"]
    password = request.data["password"]

    authenticated_user = authenticate(username = username, password = password)

    if authenticated_user is not None: 
        token = Token.objects.get_or_create(user=authenticated_user)
        return Response({'token': token[0].key})
    else:
        return Response(
            {'reason': 'Invalid credentials'},
            status=status.HTTP_400_BAD_REQUEST
        )
