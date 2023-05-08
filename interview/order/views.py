from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class TagOrdersEdgeView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        tag = OrderTag.objects.get(id=kwargs['tag_id'])
        orders = self.get_queryset().filter(tags__in=[tag])
        serializer = self.serializer_class(orders, many=True)
        
        return Response(serializer.data, status=200)
    
    def get_queryset(self):
        return self.queryset.all()
