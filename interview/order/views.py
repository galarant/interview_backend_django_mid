from dateutil import parser
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get(self, request: Request, *args, **kwargs) -> Response:
        start_date = request.GET.get('start_date') and parser.parse(request.GET.get('start_date'))
        embargo_date = request.GET.get('embargo_date') and parser.parse(request.GET.get('embargo_date'))
        if start_date and embargo_date:
            orders = self.get_queryset().filter(start_date__gte=start_date, embargo_date__lte=embargo_date)
        else:
            orders = self.get_queryset()
        print(f"start_date: {start_date} embargo_date: {embargo_date}")
        serializer = self.serializer_class(orders, many=True)
        
        return Response(serializer.data, status=200)
    
    def get_queryset(self):
        return self.queryset.all()


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
