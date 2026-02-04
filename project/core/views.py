"""
Student API View

This module provides API endpoints for Student model operations.
Supports GET (retrieve all students) and POST (create new student) operations.

Dependencies:
    rest_framework.views.APIView: Base class for API views
    rest_framework.response.Response: HTTP response wrapper
    rest_framework.status: HTTP status codes
    .models.Student: Student model
    .serializers.StudentSerializers: Student serializer
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializers
class APITestView(APIView):
    """
    It is used for GET, POST, PUT, PATCH methods.
    """
    def get(self, request):
        """
        It is used to convert the complex data into native Python.
        """
        abc = Student.objects.all()
        serailizer = StudentSerializers(abc, many=True)
        return Response({'message': serailizer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        It is used for POST requests.
        """
        serilizer = StudentSerializers(data=request.data)
        '''It is used for validation.'''
        if serilizer.is_valid():
            serilizer.save()
            return Response({"message": "data submit"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serilizer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
        Update a student record.
        """
        instance = Student.objects.get(id=id)
        serilizer = StudentSerializers(data=request.data, instance=instance)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"message": "update successfully"})
        else:
            return Response({"message": serilizer.errors})

    def patch(self, request, id):
        """
        Partially update a student record.
        """
        instance = Student.objects.get(id=id)
        serilizer = StudentSerializers(data=request.data, instance=instance, partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"message": "update successfully"})
        return Response({"message": serilizer.errors})
    
    def delete(self,request,id):
        try:
            data=Student.objects.get(id=id)
            data.delete()
            return Response({'message':'data delted successfully'})
        except Student.DoesNotExist:
            return Response({'message':"alredy deleted"},status=status.HTTP_404_NOT_FOUND)
    