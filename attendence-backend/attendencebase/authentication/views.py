import json
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers, generics, status, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from authentication.models import User
from authentication.permissions import IsAccountOwner
from authentication.serializers import UserSerializer, UserCreateSerializer
from authentication.utils import UserRecommendationPagination
from miscellaneous.utils import CustomMetaDataMixin



class UserCreateView(CustomMetaDataMixin, generics.CreateAPIView):
    """
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer





class UserViewSet(CustomMetaDataMixin, viewsets.ModelViewSet):
    """

    """
    #authentication_classes = [SessionAuthentication, ]
    permission_classes = [permissions.IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def __validate_user(self, user_id):
        if self.request.user.id != user_id:
             raise serializers.ValidationError({
                'user': 'The user_id is invalid'
             })

    def __validate_email(self, email):
        if User.objects.filter(email=email).exists():
             raise serializers.ValidationError({
                'user': 'User with the E-mail already exists'
             })

    def __validate_phone_number(self, phone_number):
        if User.objects.filter(mobile_number=phone_number).exists():
             raise serializers.ValidationError({
                'user': 'User with the Phone Number already exists'
             })

    def __validate_password(self, password):
        if len(password) == 0:
            raise serializers.ValidationError({
                'user': 'Password not supplied'
             })

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        self.__validate_email(request.data["email"])
        self.__validate_phone_number(request.data["mobile_number"])
        self.__validate_password(request.data['password'])
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            response_data = UserSerializer(user).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = UserSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)