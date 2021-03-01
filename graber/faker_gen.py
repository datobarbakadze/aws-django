import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graber.settings')

django.setup()
from food.models import Ingredient
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
    i = Ingredient.objects.get_or_create(name=name, image=image)[0]
    i.save()
    return i


def populate(N=5):
    '''
    Populating the database
    '''
    for entry in range(N):
        add_ingredient()


if __name__ == '__main__':
    print("populating script!")
    populate()
    print('Done seeding')
