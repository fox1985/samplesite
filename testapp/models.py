from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

# Create your models here.
class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Spare(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Делтали'
        verbose_name = 'Деталь'


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit', through_fields=('machine', 'spare') )
    notes = GenericRelation('Note')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Машины'
        verbose_name = 'Машина'



class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)



class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')





# Пример nрямоrо (мноrотабnмчноrо) насnедования модеnей

class Message(models.Model):
    content = models.TextField()




class PrivateMessage(Message):
    user = models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)




