from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None,**kwargs):
        if not email:
            raise ValueError('Users must have an Email')

        user = self.model(
            email=email,**kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# ads

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    last_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    friends = models.ManyToManyField('self')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def users_dict(self) -> dict:
        return {
            'id': self.email,
        }



# class Message(models.Model):
#     user_sender = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     user_receiver = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     text = models.CharField(max_length=200)
#     created_date = models.DateTimeField(auto_now_add=True)

class WallPost(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    user = models.ForeignKey(to='User', on_delete  =  models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)

    def dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'created_date': self.created_date,
        }




