from django.shortcuts import render
from django.http import JsonResponse
from base.serializers import StudentSerializer
# from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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

@api_view(['POST'])
def create_student(request):
    stud_serializer = StudentSerializer(data = request.data)
    if stud_serializer.is_valid():
        stud_serializer.save()
        return Response({'message':'Student created successfully'})
    else:
        return Response(stud_serializer.errors)
    
# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
    
#     if user is not None:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})
#     else:
#         return Response({'error': 'Invalid credentials'}, status=400)


class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=StudentSerializer(data=request.data)
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def myProducts(req):
#     all_products = ProductSerializer(Product.objects.all(), many=True).data
#     return Response(all_products)
