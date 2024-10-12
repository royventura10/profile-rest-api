from crypt import methods

from pyexpat.errors import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):


    serializer_class=serializers.HelloSerializer

    def get(self,request, format=None):
        """Tenemos que crear una diccionario o lista para enviarlo"""
        an_apiview=[
            '1. Hola 1',
            '2. Hola 2',
            '3. Hola 3',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            #email=serializer.validated_data.get('email')
            message = f'Hello {name}'
            return Response({'menssage': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({"method":'PUT'})

    def patch(self,resquest,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method' 'DELETE'})



class HelloViewSet(viewsets.ViewSet):

    # Utilizamos el mismo Serializer, tmb lo llamamos
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        a_viewset=[
            'User01',
            'User02',
            'User03',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # email=serializer.validated_data.get('email')
            message = f'Hello {name}'
            return Response({'menssage': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})






