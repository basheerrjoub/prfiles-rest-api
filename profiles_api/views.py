from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializers import HelloSerializer


class HelloApiView(APIView):
    """Testing API View"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of features of APIView"""
        features = ["Effiecient", "Good and responsive", "Robust"]

        return Response({"message": "features of API", "features": features})

    def post(self, request):
        """Create a serializer to valid the name of the user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling put request"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Handling Patch request"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deleting an object in the database"""
        return Response({"method": "Delete"})
