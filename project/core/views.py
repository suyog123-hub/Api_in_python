from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Student
from .serializers import StudentSerializers

class APITestView(APIView):
    def get(self,request):
        abc=Student.objects.all()
        serailizer=StudentSerializers(abc,many=True)
        return Response({'message':serailizer.data})
    
    def post(self,request):
        serilizer=StudentSerializers(data=request.data)
        if serilizer.is_valid():
            serilizer.save()

            return Response({"message":"dta submit"})