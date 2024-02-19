
from django.urls import path

from interview.order.views import (DeactivateOrderView, OrderListCreateView,
                                   OrderTagListCreateView)

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:order_id>/deactivate/', DeactivateOrderView.as_view(), name='deactivate-order'),
]
