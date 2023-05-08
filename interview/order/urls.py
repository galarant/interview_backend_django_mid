
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagsEdgeView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:order_id>/tags/', OrderTagsEdgeView.as_view(), name='order-tags-edge'),

]
