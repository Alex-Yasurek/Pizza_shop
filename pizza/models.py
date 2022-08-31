from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=100)

    # adding this lets us decide what to show in the admin area
    def __str__(self):
        return self.title

class Toppings(models.Model):
    # topping_choices = (
    #     ("cheese", "Cheese"),
    #     ("pepperoni", "Pepperoni"),
    #     ("chicken", "Chicken"),
    #     ("peppers", "Peppers"),
    #     ("sausage", "Sausage"),
    #     ("olives", "Olives"))
    toppings = models.CharField(max_length=50)

    def __str__(self):
        return self.toppings


class Pizza(models.Model):
    topping1 = models.ForeignKey(Toppings, on_delete=models.CASCADE)
    topping2 = models.ForeignKey(
        Toppings, related_name='toppings2toppings', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
