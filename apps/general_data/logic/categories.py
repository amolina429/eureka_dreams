from ..serializers.categories import CategoriesSerializers
from ..models.categories import Categories
from rest_framework import status
from django.db.models import Case, CharField, F, Q, Value, When

class CategoriesLogic():
    def get_categories(self, filters):
        # if filters['order_type'] == 'desc':
        #     filters['order_by'] = str('-' + filters['order_by'])

        filter_object = Q()

        if 'search' in filters:
            if 'general_filter' in filters['search']:
                filter_object |= Q(
                    id__icontains=filters['search']['general_filter'])
                filter_object |= Q(
                    nombre__icontains=filters['search']['general_filter'])

            if filters['search']['filter_by_category_id'] != '':
                filter_object &= Q(
                    category_id__icontains=filters['search']['filter_by_category_id'])

            if filters['search']['filter_by_category_name'] != '':
                filter_object &= Q(
                    category_name__icontains=filters['search']['filter_by_category_name'])

        categories_data = Categories.objects.values('id','nombre').filter(filter_object)

        recordsFiltered = Categories.objects.filter(filter_object).count()

        recordsTotal = Categories.objects.count()

        return {
            'draw': filters['draw'],
            'recordsTotal': recordsTotal,
            'recordsFiltered': recordsFiltered,
            'data': list(categories_data),
        }

    def create_category(self, data):
        Categories.objects.create(
            nombre=data['nombre']
        )
        return { 
            'message': "creado con exito!"
        }

    def get_categories_by_id(self, id):
        get_category = Categories.objects.values().get(id=id)
        return { 
            'data': get_category
        }

    def update_category(self, data):
        Categories.objects.filter(id=data['id']).delete()
        return { 
            'message': "creado con exito!"
        }