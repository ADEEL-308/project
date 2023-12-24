from django.db import models

# Create your models here.
class Menu(models.Model):
    Name=models.CharField(max_length=255),
    No_of_guests=models.IntegerField(),
    BookingDate=models.DateField()


class Booking(models.Model):
    title=models.CharField(max_length=255),
    price=models.DecimalField(decimal_places=10,max_digits=2),
    inventory=models.IntegerField()
    
