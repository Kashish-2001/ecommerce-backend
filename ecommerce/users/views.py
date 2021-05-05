from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status


class CustomUserView(APIView):
    def post(self, request):
        data = request.data
        user = CustomUser.objects.create(phone = data["phone"], name= data["name"])
        serializer = CustomUserSerializer(user, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)