from django.shortcuts import render, HttpResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api.serializers import course
from api import serializers as app01_serializers
from api.utils.response import BaseResponse
from api import models
import json

class CoursesView(ViewSetMixin, APIView):

    def list(self,request,*args,**kwargs):
        ret = BaseResponse()

        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)

            # 分页之后的结果执行序列化
            ser = course.CourseModelSerializer(instance=course_list, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)

    def create(self,request,*args,**kwargs):
        pass

    def retrieve(self,request,pk,*args,**kwargs):
        response = {'code':1000, 'data':None,'error':None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = course.CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

    def update(self,request,pk,*args,**kwargs):
        pass

    def destroy(self,request,pk,*args,**kwargs):
        pass

# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseView(APIView):
    """
	查看所有学位课
	"""

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()

    try:
        # 从数据库获取数据
        queryset = models.DegreeCourse.objects.all()

        # 分页
        page = PageNumberPagination()
        degree_list = page.paginate_queryset(queryset, request, self)

        # 分页之后的结果执行序列化
        ser = course.DegreeCourseSerializer(instance=degree_list, many=True)
        ret.data = ser.data

    except Exception as e:
        ret.code = 500
        ret.error = '获取数据失败'

    return Response(ret.dict)

# b.查看所有学位课并打印学位课名称以及学位课的奖学金

# c.展示所有的专题课

# d. 查看id=1的学位课对应的所有模块名称

# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

# f.获取id = 1的专题课，并打印该课程相关的所有常见问题

# g.获取id = 1的专题课，并打印该课程相关的课程大纲

# h.获取id = 1的专题课，并打印该课程相关的所有章节
