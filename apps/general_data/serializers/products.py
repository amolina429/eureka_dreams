from rest_framework import serializers
from ..models.products import Products

class ProductsSerializers(serializers.ModelSerializer):
      third_verification_code = serializers.IntegerField()
      id_third_parties = serializers.CharField(max_length=100)
      alternate_id = serializers.CharField(max_length=100)

      class Meta:
            model = Products
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
  
