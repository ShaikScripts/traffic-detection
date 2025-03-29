from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=3000)
    gender = models.CharField(max_length=300)


class predict_abnormal_traffic(models.Model):

    Fid= models.CharField(max_length=300)
    lat= models.CharField(max_length=300)
    lon= models.CharField(max_length=300)
    street= models.CharField(max_length=300)
    region= models.CharField(max_length=300)
    traffic_date_time= models.CharField(max_length=300)
    junction_no= models.CharField(max_length=300)
    vechile_type= models.CharField(max_length=300)
    no_of_vehicles= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



