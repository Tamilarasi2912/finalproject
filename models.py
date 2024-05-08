from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length =  10)
    email = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name
COLOR_CHOICES = (
    ('','Select'),
    ('10AM','10 AM'),
    ('11AM','11 AM'),
    ('12PM', '12PM'),)
STS = (
    ('','Select'),
    ('Booked','Book'),
    ('Cancelled','Cancel'),
    ('Pending', 'Pending'),)
class Doctor_Detail(models.Model):
    doctor_name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    phone_number = models.CharField(max_length=30,null=True)
    specialist = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=40)
    country = models.CharField(max_length=30,null=True)
    state = models.CharField(max_length=30,null=True)
    city = models.CharField(max_length=30,null=True)
    hospital_address = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.doctor_name
class Appointment(models.Model):
    hospital_id =  models.ForeignKey(Doctor_Detail, on_delete=models.CASCADE)
    customer_id =  models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    booking_time = models.CharField(max_length=20, choices=COLOR_CHOICES)
    booking_status = models.CharField(max_length=20, choices=STS)
    msg = models.TextField(max_length=2000,null=True,blank=True)
    def __str__(self):
        return self.customer_id.name
