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


class OrderTagsEdgeView(APIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        order = Order.objects.get(id=kwargs['order_id'])
        tags = self.queryset.filter(orders__in=[order])
        serializer = self.serializer_class(tags, many=True)
        
        return Response(serializer.data, status=200)
    
    def get_queryset(self):
        return self.queryset.all()
