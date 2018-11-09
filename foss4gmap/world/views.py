from django.shortcuts import render
from .models import WorldBorder, Suinanjiko
from rest_framework import generics,viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
import json

from world import serializers

# def map(request):
#     maps = WorldBorder.objects.get(name='Japan').mpoly.geojson
#     return render(request, 'world/map.html', {'maps':maps})

def map(request):
    contexts = {}
    return render(request,'world/map.html',contexts)

class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = serializers.WorldBorderSerializer

class SuinanjikoViewSet(viewsets.ModelViewSet):
    queryset = Suinanjiko.objects.all()
    serializer_class = serializers.SuinanjikoSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True


class GeojsonAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            encjson  = serialize('geojson', Suinanjiko.objects.all())
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)

        return response
