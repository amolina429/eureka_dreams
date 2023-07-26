from ..serializers.categories import CategoriesSerializers
from ..models.categories import Categories
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from ..logic.categories import CategoriesLogic

# Create your views here.
class CategoriesViews(APIView, CategoriesLogic):
    #   permission_classes = [IsAuthenticated]

      def get(self, request, *args, **kwargs):
          draw = int(self.request.GET['draw'])
          order_by_column_index = self.request.GET.get('order[0][column]')
          order_by = self.request.GET.get('columns[' + order_by_column_index + '][data]')
          order_type = self.request.GET.get('order[0][dir]')
          start = int(self.request.GET['start'])
          length = int(self.request.GET['length']) + start
          search = self.request.GET.get('search[value]')
          filter_by_category_id = self.request.GET.get('columns[0][search][value]')
          filter_by_category_name = self.request.GET.get('columns[1][search][value]')
  
          filters = {
              'draw': draw,
              'order_by': order_by,
              'order_type': order_type,
              'start': start,
              'length': length,
              'search': {
                  'general_filter': search,
                  'filter_by_category_id': filter_by_category_id,
                  'filter_by_category_name': filter_by_category_name,
              }
          }
          return JsonResponse(self.get_categories(filters))

      def post(self, request):
          data = {
              'nombre': request.POST['nombre'],
          }
          return JsonResponse(self.create_category(data))

class CategoriesEditViews(APIView, CategoriesLogic):
      def get(self, request, *args, **kwargs):
          id = self.request.GET.get('id')
          return JsonResponse(self.get_categories_by_id(id))

      def put(self, request, *args, **kwargs):
          data = {
              'nombre': request.POST['nombre'],
              'id': request.POST['id'],
          }
          return JsonResponse(self.update_category(data))

      def delete(self, request, *args, **kwargs):
          print(request.POST)
          data = {
              'id': request.POST['id'],
          }
          return JsonResponse(self.update_category(data))
