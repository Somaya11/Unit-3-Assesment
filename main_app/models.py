from django.db import models
# from django.views.generic.edit import about
# Create your models here.
class widget_list( models.Model):
    description = models.CharField(max_length=100)
    quanity = models.IntegerField()

# class about(about):
#     model = widget_list
#     fields = '__all__'