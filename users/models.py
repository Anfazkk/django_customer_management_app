from django.db import models


class Customer(models.Model):
    number = models.IntegerField()
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    date_of_birth = models.DateField()
    password = models.CharField(max_length=255)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    event = models.ManyToManyField('events.Events')

    def __str__(self):
        return self.user.username
