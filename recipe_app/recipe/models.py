from django.db import models

# Create your models here.
class Meals(models.Model):
    SOUP_AND_STEW = 'SP'
    SWALLOW = 'SW'
    REGULAR_MEAL = 'RM'

    FOOD_CATEGORY = [
        (SOUP_AND_STEW, 'Soup & Stew'),
        (SWALLOW, 'SWALLOW'),
        (REGULAR_MEAL, 'Meal')
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=FOOD_CATEGORY, default=REGULAR_MEAL)
    ingredients = models.TextField()
    steps = models.TextField()
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True )

    class Meta:
        verbose_name_plural = 'Meals'

    def _str__(self):
        return self.name