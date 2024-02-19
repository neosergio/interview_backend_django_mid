
from django.urls import path

from interview.order.views import (OrderListCreateView, OrdersBetweenDatesView,
                                   OrderTagListCreateView)

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('between_dates/<str:start_date>/<str:embargo_date>/', OrdersBetweenDatesView.as_view(), name='orders-between-dates')
]