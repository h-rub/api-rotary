from authentication.serializer import RegisterSerializer, UserSerializer
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from authentication.authTokenRotary import CsrfExemptTokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, mixins
from rest_framework.authtoken.models import Token
from authentication.models import CustomUser

class LoginView(generics.GenericAPIView):
    authentication_classes = (CsrfExemptTokenAuthentication,)
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            login(request, user)
            token_dict = {
            'token': str(token.key),  # None
            }
            resp = UserSerializer(user, context=self.get_serializer_context()).data
            resp.update(token_dict)
            return Response(
                resp,
                status=status.HTTP_200_OK)
        else:
            print("No existe el usuario")
            # No backend authenticated the credentials
            return Response([{'error':'Credenciales inválidas'}],status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    authentication_classes = (CsrfExemptTokenAuthentication,)

    def post(self, request):
        # Borramos de la request la información de sesión
        email = request.data.get('email')
        user = CustomUser.objects.get(email=email)
        try:
            token = Token.objects.get(user_id=user.id)
            token.delete()
        except:
            return Response([{'msg':'No existe un token para el usuario'}], status=status.HTTP_401_UNAUTHORIZED)
        # Devolvemos la respuesta al cliente
        return Response([{'msg':'Sesión cerrada correctamente'}], status=status.HTTP_200_OK)


class SignUpView(generics.GenericAPIView):
    authentication_classes = (CsrfExemptTokenAuthentication,)
    serializer_class = RegisterSerializer
    
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Usuario creado correctamente. Ahora puedes iniciar sesión",
        })

from django.core.files.base import ContentFile

def upload_photo(request):
    print(request.POST)
    return Response({'msg':'Petición recibida'})