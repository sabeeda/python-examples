from rest_framework import serializers  
from .models import Students  
  
class StudentSerializer(serializers.ModelSerializer):  
    first_name = serializers.CharField(max_length=200, required=True)  
    last_name = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField()  
    mobile = serializers.CharField(max_length=10, required=True)  
  
    def create(self, validated_data):
           return Students.objects.create(**validated_data)  
    def update(self, instance, validated_data):     
        instance.save()  
        return instance  
    
    class Meta:  
        model = Students  
        fields = ('__all__')  
  