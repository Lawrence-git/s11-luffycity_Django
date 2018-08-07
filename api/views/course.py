from django.shortcuts import render,HttpResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api.serializers.course import CourseSerializer,CourseModelSerializer
from api import serializers as app01_serializers
from api.utils.response import BaseResponse
from api.models import models
import json


# class CoursesView(ModelViewSet):
#     queryset=Course.objects.all()
#     serializer_class =app01_serializers.Course_serializers


class CoursesView(APIView):

    def get(self,request,*args,**kwargs):
        # response = {'code':1000,'data':None,'error':None}
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)

            # 分页之后的结果执行序列化
            ser = CourseModelSerializer(instance=course_list,many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)


class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

