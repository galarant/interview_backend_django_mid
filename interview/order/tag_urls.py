
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, TagOrdersEdgeView


urlpatterns = [
    path('<int:tag_id>/orders/', TagOrdersEdgeView.as_view(), name='tag-orders-edge'),
]
