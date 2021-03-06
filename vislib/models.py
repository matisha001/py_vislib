from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def default_datetime():    
    now = timezone.now()   
    return now

# Create your models here.
class Chart(models.Model):
    chart_id=models.CharField(max_length=64, primary_key=True)
    chart_name=models.CharField(max_length=128)
    desc=models.CharField(max_length=512, null=True)
    content=models.TextField()
    is_private=models.BooleanField()
    status=models.IntegerField()
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(db_index=True, default=default_datetime)
    updated_at = models.DateTimeField(db_index=True, null=False)

class Dashboard(models.Model):
  dashboard_id=models.CharField(max_length=64, primary_key=True)
  name=models.CharField(max_length=128)
  desc=models.CharField(max_length=512, null=True)
  content=models.TextField()
  is_private=models.BooleanField()
  status=models.IntegerField()
  creator=models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(db_index=True, default=default_datetime)
  updated_at = models.DateTimeField(db_index=True, null=False)

class ChartBoardMap(models.Model):
  chart=models.ForeignKey(Chart, on_delete=models.CASCADE)
  dashboard=models.ForeignKey(Dashboard, on_delete=models.CASCADE)
  id=models.CharField(max_length=64, primary_key=True)
  created_at = models.DateTimeField(db_index=True, default=default_datetime)
  updated_at = models.DateTimeField(db_index=True, null=False)

class BoardOrder(models.Model):
  creator=models.ForeignKey(User, on_delete=models.CASCADE)
  order=models.TextField()
  id=models.CharField(max_length=64, primary_key=True)
  created_at = models.DateTimeField(db_index=True, default=default_datetime)
  updated_at = models.DateTimeField(db_index=True, null=False)
