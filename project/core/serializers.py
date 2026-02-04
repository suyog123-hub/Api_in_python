"""
Student API Serializer

This module defines serializers for the Student model, including validation logic
for age and phone number fields.

Dependencies:
    - rest_framework: Django REST Framework for serializers
    - re: Regular expression operations for phone validation
    - .models: Local Student model
"""
import re

from rest_framework import serializers

from .models import Student
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.CharField()
    phone=serializers.CharField()
    nessage=serializers.CharField()
    #api bata aako data lai database ma rakhni kaam garxa 
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    def validate_age(self,age):
        if int(age)>100 or int(age)<0:
            raise serializers.ValidationError("age should be between 0 to 100")
        return age
    def validate_phone(self,phone):
        if not re.match(r"^(98|97)\d{8}$",phone):
            raise serializers.ValidationError("invalid phone number")
        return phone 
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.phone=validated_data.get('phone',instance.phone)
        instance.nessage=validated_data.get('nessage',instance.nessage)
        instance.save()
        return instance
    
