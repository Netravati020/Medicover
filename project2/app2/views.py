
from django.shortcuts import render

from rest_framework.generics import GenericAPIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer
from .models import Employee


# read all the data
class EmployeeList(GenericAPIView,ListModelMixin):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer
    # authentication_classes= [JWTAuthentication]
    # permission_classes= [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        return self.list(request,*args,**kwargs)


# insert the data into record
class EmployeeCreate(GenericAPIView,CreateModelMixin):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

    def post(self,request, *args, **kwargs):
       return self.create(request,*args,**kwargs)

# reading only one record
class EmployeeRetrive(GenericAPIView,RetrieveModelMixin):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer 

    def get(self,request, *args, **kwargs):
       return self.retrieve(request,*args,**kwargs) 


# class LoginView(APIView):
#     permission_classes= (IsAuthenticated,)
    
#     def get(self,request):
#         content= {'messege':'Welcome!'}
#         return Response(content)


