from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    type_choices = [
        ('standart', 'Standart'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ]
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null = True, blank = True)
    capacity = models.IntegerField(default=2)
    image = models.ImageField(upload_to='', null=True, blank=True)
    type_room = models.CharField(choices=type_choices, max_length=50, default='standart')
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    persons = models.IntegerField(default = 1)
    phone_number = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Кімната: {self.room} - Дата заїзду: {self.check_in} Дата виїзду: {self.check_out}'