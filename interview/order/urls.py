
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, TagOrdersEdgeView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('tags/<int:tag_id>/orders/', TagOrdersEdgeView.as_view(), name='tag-orders-edge'),
    path('', OrderListCreateView.as_view(), name='order-list'),
]
