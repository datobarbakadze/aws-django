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

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    '''
    Model for caching Ingrediens.
    '''
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name
