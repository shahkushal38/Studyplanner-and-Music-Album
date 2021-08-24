from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer

# Create your views here.
class StockList(APIView):
    def get(self,request):
        stocks=Stock.objects.all()
        serializer=StockSerializer(stocks, many=True)
        return Response(serializer.data)
