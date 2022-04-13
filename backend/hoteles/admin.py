from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import Picture
from .models import Review

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_id','category','name','price_per_night',"score",'date_added')
    list_editable = ('category', 'name',"score","price_per_night")

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('picture_id','hotel','url','date_added')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id','hotel','content',"score",'date_added')
    