from ..serializers.subcategories import SubcategoriesSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class SubcategoriesViews(APIView):
      permission_classes = [IsAuthenticated]
      def post(self, request):
          serializer = SubcategoriesSerializers(data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def get(self, request):
          serializer = SubcategoriesSerializers(pk=request.params.id)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def put(self, request):
          serializer = SubcategoriesSerializers(pk=request.params.id)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request):
          serializer = SubcategoriesSerializers(pk=request.params.id)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


