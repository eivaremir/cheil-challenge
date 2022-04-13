from django.db import models
import uuid
# Create your models here.

class Hotel(models.Model):
    hotel_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(
        max_length = 1, 
        choices = (
            ("1","1 Star"),
            ("2","2 Stars"),
            ("3","3 Stars"),
            ("4","4 Stars"),
            ("5","5 Stars")
        ), 
        default = '4')
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=255,blank=True, null=True)
    thumbnail = models.CharField(blank=True, null=True,max_length=255)
    score = models.DecimalField(max_digits=2, decimal_places=1,default=5)
    price_per_night =models.DecimalField(max_digits=5, decimal_places=2,default=75)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

class Picture(models.Model):
    picture_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, related_name='picture', on_delete=models.CASCADE)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, related_name='review', on_delete=models.CASCADE)
    content = models.TextField(max_length=255,blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=2, decimal_places=1,default=5)
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return f"({self.score}): {self.content[0:10]}"