from django.db import models

'''
All the models are used for caching the actual
api request results for faster access.
'''


class Recipe(models.Model):
    '''
    Model for caching Reciepe data.s
    '''
    title = models.CharField(max_length=100)
    readyInMinutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    '''
    Model for caching Ingrediens.
    '''
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Taste(models.Model):
    sweetness = models.FloatField()
    saltiness = models.FloatField()
    sourness = models.FloatField()
    bitterness = models.FloatField()
    savoriness = models.FloatField()
    fattiness = models.FloatField()
    spiciness = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "sweetness is " + self.sweetness
