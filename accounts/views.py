from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username) #CustomUser hat hinzugefügtes Feld email
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)    
    


@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    
    def post(self, request):
        try:
            request.user.auth_token.delete() # löscht den User Token bei Logout
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)