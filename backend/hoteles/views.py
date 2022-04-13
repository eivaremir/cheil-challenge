
from django.http import Http404,HttpResponseBadRequest,HttpResponseNotFound
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Hotel
from .serializers import HotelSerializer
# Create your views here.
class HotelView(APIView):
    
    def get(self, request):
        hoteles = Hotel.objects.all()
        
        serializer = HotelSerializer( hoteles,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "category":openapi.Schema(type=openapi.TYPE_INTEGER,description="(string) hotel category from 1 to 5"),
            "name":openapi.Schema(type=openapi.TYPE_STRING,description="(string) Hotel name"),
            "slug":openapi.Schema(type=openapi.TYPE_STRING,description="(string) Hotel slug",default="slug"),
            "description":openapi.Schema(type=openapi.TYPE_STRING,description="(string) Hotel large description. Up to 255 characters"),
            "thumbnail":openapi.Schema(type=openapi.TYPE_STRING,description="(string) HTTPS URL of the image"),
            "score":openapi.Schema(type=openapi.TYPE_NUMBER,description="(decimal) score from 1.0 to 5.0"),
            "price_per_night":openapi.Schema(type=openapi.TYPE_NUMBER,description="(decimal) price per night"),
        }
    ))
    def post(self, request):
        try:
            hotel=Hotel.objects.create(**request.data)
            serializer = HotelSerializer(hotel)
        except Exception as ex:
            return HttpResponseBadRequest(str(ex))
        return Response(serializer.data)
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "hotel_id":openapi.Schema(type=openapi.TYPE_STRING,description="(string) hotel hash id"),
            
        }
    ))
    def delete(self, request):
        try:
            hotel= Hotel.objects.get(hotel_id=request.data.get('hotel_id', '')).delete()
            #serializer = HotelSerializer(hotel)
        except Exception as ex:
            return HttpResponseBadRequest(str(ex))
        return Response({
            "status":"deleted",
            "result":hotel
        })
    
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["hotel_id"],
        properties={
            "hotel_id":openapi.Schema(type=openapi.TYPE_STRING,description="(string) hotel hash id"),
            "category":openapi.Schema(type=openapi.TYPE_INTEGER,description="(string) hotel category from 1 to 5"),
            "name":openapi.Schema(type=openapi.TYPE_STRING,description="(string) Hotel name"),
            "slug":openapi.Schema(type=openapi.TYPE_STRING,description="(string) Hotel slug",default="slug"),
            "description":openapi.Schema(type=openapi.TYPE_STRING,description="(string) Hotel large description. Up to 255 characters"),
            "thumbnail":openapi.Schema(type=openapi.TYPE_STRING,description="(string) HTTPS URL of the image"),
            "price_per_night":openapi.Schema(type=openapi.TYPE_NUMBER,description="(decimal) price per night"),
        }
    ))
    def put(self, request):
        try: 
            hotel = Hotel.objects.get(hotel_id=request.data.get("hotel_id",""))
        except Hotel.DoesNotExist:
            raise Http404
        try:
            hotel.hotel_id = request.data.get("hotel_id",hotel.hotel_id)
            hotel.category = request.data.get("category",hotel.category)
            hotel.name = request.data.get("name",hotel.name)
            hotel.slug = request.data.get("slug",hotel.slug)
            hotel.description = request.data.get("description",hotel.description)
            hotel.thumbnail = request.data.get("thumbnail",hotel.thumbnail)
            hotel.price_per_night = request.data.get("price_per_night",hotel.price_per_night)
            hotel.save()
            #serializer = HotelSerializer(hotel)
        except Exception as ex:
            return HttpResponseBadRequest(str(ex))
        return Response({
            "status":"updated",
            "result":HotelSerializer(hotel).data
        })


@api_view(['GET'])
def hotel_read(request,slug):
    
    
    hotel =  Hotel.objects.get(slug=slug)
    serializer = HotelSerializer(hotel)
    return Response(serializer.data)

@api_view(['GET'])
def hotels_ordered(request,order):
    
    if not order in ["asc","desc"]:
        return HttpResponseBadRequest("Please provide an ordering direction. Available options: asc, desc")
    hotels =  Hotel.objects.all().order_by(f"{'-' if order == 'desc' else ''}price_per_night")
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method="POST",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["hotel_id"],
        properties={
            "category":openapi.Schema(type=openapi.TYPE_STRING,description="(string) hotel category from 1 to 5",default="5"),
            "score_from":openapi.Schema(type=openapi.TYPE_INTEGER,description="(int) hotel score from (greater or equal than...)"),
            "score_to":openapi.Schema(type=openapi.TYPE_INTEGER,description="(int) hotel score from (lower or equal than...)")
        }
    )) 
@api_view(['POST'])
def hotels_search(request):
    category = request.data.get('category', '')
    score_from = request.data.get('score_from', '')
    score_to = request.data.get('score_to', '')
    query = Q()
    if category:
        query = Q(category__icontains=category) 
    

    if score_from:
        query = query & Q(score__gte=score_from)
    if score_to:
        query = query & Q(score__lte=score_to)
    
    #import pdb; pdb.set_trace()
    hotels = Hotel.objects.filter(query).order_by(f"{'-' if request.data.get('order', '') == 'desc' else ''}price_per_night")
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)