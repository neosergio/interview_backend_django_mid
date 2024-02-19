from datetime import date

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
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


class OrdersBetweenDatesView(APIView):
    serializer_class = OrderSerializer
    def get(self, request, start_date, embargo_date):
        try:
            # Convert the string dates to datetime objects
            start_date = date.fromisoformat(start_date)
            embargo_date = date.fromisoformat(embargo_date)
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        # Retrieve orders between the specified start and embargo date
        orders = Order.objects.filter(start_date__gte=start_date, embargo_date__lte=embargo_date, is_active=True)
        serializer = self.serializer_class(orders, many=True)

        return Response(serializer.data, status=200)
