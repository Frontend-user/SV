# from django.db import models
#
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

from django.db import models


# ads
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)


# class Message(models.Model):
#     user_sender = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     user_receiver = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     text = models.CharField(max_length=200)
#     created_date = models.DateTimeField(auto_now_add=True)

class WallPost(models.Model):
    text = models.CharField(max_length=500)
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)

# class Friend(models.Model):
#     friends = models.ManyToManyField('self')
