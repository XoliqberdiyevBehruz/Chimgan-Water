import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class WhyUs(BaseModel):
    icon = models.ImageField(upload_to='why_us_icons/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(BaseModel):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    description = models.TextField()   

    def __str__(self):
        return self.name
    

class Media(BaseModel):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image.name
    

class AboutCompany(BaseModel):
    expirience = models.CharField(max_length=255)
    clients = models.CharField(max_length=255)
    partners = models.CharField(max_length=255)
    products = models.CharField(max_length=255)

    def __str__(self):
        return f"About Company: {self.expirience}, {self.clients}, {self.partners}, {self.products}"
    

class Feedback(BaseModel):
    profile_image = models.ImageField(upload_to='feedback/')
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Feedback from {self.full_name} - {self.rating} stars"
    

class NewsCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title
    
