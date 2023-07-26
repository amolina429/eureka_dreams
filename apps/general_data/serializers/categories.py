from rest_framework import serializers
from ..models.categories import Categories

class CategoriesSerializers(serializers.ModelSerializer):
      id = serializers.IntegerField()
      nombre = serializers.CharField(max_length=100)

      class Meta:
            model = Categories
            fields = '__all__'

      def validate_third_verification_code(self, third_verification_code):
          data = self.initial_data
          print("data: ",self)
          if not isinstance(third_verification_code, int):
             raise serializers.ValidationError("El código de verificación debe ser numerico")
          return third_verification_code
  
      def validate_type_third_id(self, third_type_id):
          data = self.initial_data
          print("data: ",self)
          if third_type_id in ('NIT','NE') and 'third_verification_code' not in data :
             raise serializers.ValidationError("Tercero corresponde a persona Juridica, debe tener código de verificación")
          return third_type_id
  
      def validate(self, data):
          print("self: ",self)
          print("data: ",data)
          return data
  
