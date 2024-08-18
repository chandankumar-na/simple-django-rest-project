from rest_framework import generics, status
from rest_framework.response import Response

from .models import Users
from .serializers import UserSerializer

class UsersListCreate(generics.ListCreateAPIView):
    queryset= Users.objects.all()
    serializer_class= UserSerializer

    def delete(self,request, *args, **kwargs):
        Users.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class= UserSerializer
    lookup_field= "pk"






