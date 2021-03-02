import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graber.settings')

django.setup()
from food.models import Ingredient, Recipe, Taste
from faker import Factory

Faker = Factory.create
fakegen = Faker()


def add_ingredient():
    '''
    Ingredient seeder for creating the entry in the database
    table
    '''
    name = fakegen.sentence(nb_words=5, variable_nb_words=False)
    image = fakegen.image_url()
    i = Ingredient.objects.get_or_create(name=name, image=image)
    return i


def add_recipe():
    '''
    Recipe table seeder
    '''
    title = fakegen.sentence(nb_words=3, variable_nb_words=False)
    readyInMinutes = random.randrange(0, 100)
    r = Recipe.objects.get_or_create(readyInMinutes=readyInMinutes, title=title)
    return r


def add_taste():
    '''
    Fake data seeder for Taste database table
    '''
    sweetness = random.randrange(0, 100) / 7
    saltiness = random.randrange(0, 100) / 7
    sourness = random.randrange(0, 100) / 7
    bitterness = random.randrange(0, 100) / 7
    savoriness = random.randrange(0, 100) / 7
    fattiness = random.randrange(0, 100) / 7
    spiciness = random.randrange(0, 100) / 7

    t = Taste.objects.get_or_create(
        sweetness=sweetness,
        saltiness=saltiness,
        sourness=sourness,
        bitterness=bitterness,
        savoriness=savoriness,
        fattiness=fattiness,
        spiciness=spiciness,
    )
    return t


def populate(N=20):
    '''
    Populating the database
    '''
    for entry in range(N):
        add_ingredient()
        add_recipe()
        add_taste()


if __name__ == '__main__':
    print("populating script!")
    populate()
    print('Done seeding')
