from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
        def get(self, request, format=None):
                    return Response({"message": "Hello, Monitoring!"})
