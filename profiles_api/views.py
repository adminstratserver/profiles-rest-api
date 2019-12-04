from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


def HelloAPI(request):
    return HttpResponse("Hello World!")

class HelloAPIView(APIView):
    def get(self, request):
        init1 = [
            'data1',
            'data2',
            'data3'
                ]
        init2 = [
            'data4',
            'data5',
            'data6'
        ]
        return Response({'key1':init1, 'key2':init2})

    serializer_class = serializers.HelloSerializer

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Create a put message """
        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """Create a patch message """
        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Create a delete message """
        return Response({'Method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        init11 = [
            'data11',
            'data12',
            'data13'
                ]
        init12 = [
            'data14',
            'data15',
            'data16'
        ]
        return Response({'key1':init11, 'key2':init12})

    def create(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle getting part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)