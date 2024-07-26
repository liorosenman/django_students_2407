from django.shortcuts import render
from django.http import JsonResponse

from base.serializers import ProductSerializer
from .serializers import ProductSerializer, StudentSerializer
from .models import Product, Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView

def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in Product.objects.all(): #run on every row in the table...
        res.append({"title":img.title,
                "description":img.description,
                "completed":False,
               "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return a

@api_view(['GET'])
def get_students(request):
    all_students = StudentSerializer(Student.objects.all(), many=True).data
    return Response(all_students)

class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=ProductSerializer(data=request.data)

# @api_view(['GET'])
# def myProducts(req):
#     all_products = ProductSerializer(Product.objects.all(), many=True).data
#     return Response(all_products)
