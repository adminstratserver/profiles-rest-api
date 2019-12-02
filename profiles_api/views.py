from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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
                # status=status.HTTP_400_BAD_REQUEST
                status=400
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
