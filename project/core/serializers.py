from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    phone=serializers.IntegerField()
    nessage=serializers.CharField()



    #api bata aako data lai database ma rakhni kaam garxa 
    def create(self,validated_data):
        return Student.objects.create(**validated_data)