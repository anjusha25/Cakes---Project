from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

# Create your views here.

from . models import Cake,Category,Shape,Weight

from . serializers import CakeSerializer,CategorySerializer,ShapeSerializer,WeightSerializer

from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication

from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly

from authentication.permissions import IsAdmin,IsUser

from rest_framework_simplejwt.authentication import JWTAuthentication

class CakeListCreateView(APIView):

    serializer_class=CakeSerializer

    # authentication_classes=[BasicAuthentication]
    # authentication_classes=[TokenAuthentication]

    authentication_classes=[JWTAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method =='POST':

            permissions=[IsAdmin]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        cakes=Cake.objects.all()

        serializer=self.serializer_class(cakes,many=True)


        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'Cake created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class CakeRetrieveUpdateDestroyView(APIView):

    serializer_class=CakeSerializer

    # authentication_classes=[BasicAuthentication]

    # authentication_classes=[TokenAuthentication]

    authentication_classes=[JWTAuthentication]
    

    def get_permissions(self):

        permissions=[]

        if self.request.method in ['PATCH','DELETE']:

            permissions=[IsAdmin]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        cake=Cake.objects.get(id=id)

        serializer=self.serializer_class(cake)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id=kwargs.get('id')

        cake=Cake.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=cake,partial=True)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'Cake updated sucessfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        cake=Cake.objects.get(id=id)

        cake.delete()

        data={'msg':'cake deleted sucessfully'}

        return Response(data,status=204)

class CategoryListCreateView(APIView):

    serializer_class=CategorySerializer

    authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method =='POST':

            permissions=[IsAdminUser]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        category=Category.objects.all()

        serializer=self.serializer_class(category,many=True)


        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'Category created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class CategoryRetrieveUpdateDestroyView(APIView):

    serializer_class=CategorySerializer

    authentication_classes=[BasicAuthentication]

    def get_permissions(self):

        permissions=[]

        if self.request.method in ['PATCH','DELETE']:

            permissions=[IsAdminUser]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        category=Category.objects.get(id=id)

        serializer=self.serializer_class(category)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id=kwargs.get('id')

        category=Category.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=category,partial=True)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'Category updated sucessfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        category=Category.objects.get(id=id)

        category.delete()

        data={'msg':'category deleted sucessfully'}

        return Response(data,status=204)


class ShapeListCreateView(APIView):

    serializer_class=ShapeSerializer

    authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method =='POST':

            permissions=[IsAdminUser]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        shape=Shape.objects.all()

        serializer=self.serializer_class(shape,many=True)


        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'Shape created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class ShapeRetrieveUpdateDestroyView(APIView):

    serializer_class=ShapeSerializer

    authentication_classes=[BasicAuthentication]

    def get_permissions(self):

        permissions=[]

        if self.request.method in ['PATCH','DELETE']:

            permissions=[IsAdminUser]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        shape=Shape.objects.get(id=id)

        serializer=self.serializer_class(shape)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id=kwargs.get('id')

        shape=Shape.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=shape,partial=True)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'shape updated sucessfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        shape=Shape.objects.get(id=id)

        shape.delete()

        data={'msg':'Shape deleted sucessfully'}

        return Response(data,status=204)


class WeightListCreateView(APIView):

    serializer_class=WeightSerializer

    authentication_classes=[BasicAuthentication]

    # permission_classes=[IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        permissions=[]

        if self.request.method =='POST':

            permissions=[IsAdminUser]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        weight=Weight.objects.all()

        serializer=self.serializer_class(weight,many=True)


        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'weight created sucessfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)

class WeightRetrieveUpdateDestroyView(APIView):

    serializer_class=WeightSerializer

    authentication_classes=[BasicAuthentication]

    def get_permissions(self):

        permissions=[]

        if self.request.method in ['PATCH','DELETE']:

            permissions=[IsAdminUser]

        return[permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        weight=Weight.objects.get(id=id)

        serializer=self.serializer_class(weight)

        return Response(serializer.data,status=200)

    def patch(self,request,*args,**kwargs):

        id=kwargs.get('id')

        weight=Weight.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=weight,partial=True)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'weight updated sucessfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):
    
        id=kwargs.get('id')
    
        weight=Weight.objects.get(id=id)

        weight.delete()

        data={'msg':'Weight deleted sucessfully'}

        return Response(data,status=204)





