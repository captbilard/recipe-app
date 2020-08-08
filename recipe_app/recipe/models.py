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
    meal_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, null=True, blank=True)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True )

    class Meta:
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.name