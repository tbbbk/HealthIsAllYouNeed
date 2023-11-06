from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Model representing a user.
Fields:
- username: The user's username (primary key).
- password: The user's password.
- introduction: A brief introduction about the user.
- weight: The user's weight with a maximum of 3 digits and 2 decimal places.
- height: The user's height with a maximum of 3 digits and 2 decimal places.
- target: The user's target weight with a maximum of 3 digits and 2 decimal places.
- age: The user's age.
- gender: The user's gender (True for male, False for female).
- email: The user's email address.
- loseOradd: The user's plan is whether lose or add weight (True for lose, False for add).
"""
class User(AbstractUser):
    introduction = models.TextField(max_length=100)
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    target = models.DecimalField(max_digits=3, decimal_places=2)
    age = models.IntegerField()
    gender = models.BooleanField()
    email = models.EmailField()
    loseORadd = models.BooleanField()







