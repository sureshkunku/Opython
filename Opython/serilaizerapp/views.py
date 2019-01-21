from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework import status
from Opythonapp.models import UserProfile
from serilaizerapp.serilaizer import userprofileSerilaizer,userpostserilaizer,userputserilaizer,userdeleteserilaizer
# Create your views here.

class userlist(APIView):

    def get(self, format=None, pk=None):
        user=UserProfile.objects.all()
        paginator=Paginator(user,3)
        page = self.request.GET.get('page')
        try:
            ser = paginator.page(page)
        except PageNotAnInteger:
            ser = paginator.page(1)
        except EmptyPage:
            ser = paginator.page(paginator.num_pages)
        serilaizer=userprofileSerilaizer(ser,many=True)
        return Response(serilaizer.data)
    def post(self, format=None):
        ser=userpostserilaizer(data=self.request.data)
        if ser.is_valid():
            ser.save()
            return Response("user created sucessfuly",status=status.HTTP_201_CREATED)
        else:
            return Response(ser._errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self, format=None, pk=None):
        user=UserProfile.objects.filter(id=pk)
        ser=userputserilaizer(data=self.request.data,instance=user)
        if ser.is_valid():
            try:
                ser.save()
            except Exception as err:
                return Response("issue : %s "%err.mesaage,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response("User updated sucessfuly")
        else:
            return Response(ser._errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, format=None,pk=None):
        req_data=UserProfile.objects.filter(id=1)
        ser=userdeleteserilaizer(data=self.request.data,instance=req_data)
        if ser:
            ser=ser[0]
            ser.delete()
            return Response('User deleted sucessfuly')
        else:
            return Response("No records found",status=status.HTTP_404_NOT_FOUND)


