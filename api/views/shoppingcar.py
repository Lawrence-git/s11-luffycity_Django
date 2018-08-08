from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

SHOPPING_CAR = {}

class ShoppingCarView(ViewSetMixin,APIView):

    def create(self,requset,*args,**kwargs):
        """
        加入购物车
        :param requset:
        :param args:
        :param kwargs:
        :return:
        """

        return Response({'code':10000})