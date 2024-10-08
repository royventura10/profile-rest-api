from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self,request, format=None):
        """Tenemos que crear una diccionario o lista para enviarlo"""
        an_apiview=[
            '1. Hola 1',
            '2. Hola 2',
            '3. Hola 3',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})


