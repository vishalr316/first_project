import os
# Configuring the settings for the project.
# Need to do this before we start manipulating the actual models
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

# Import and configure/setup the project settings
import django
django.setup()

# FAKE POPULATION SCRIPT
import random
from first_app.models import AccessRecord,Webpage,Topic

from faker import Faker

# Create instance of the object
fakegen = Faker()

# list of Topics for different websites
topics = ['Search','Social','Marketplace','News','Games']

# function to add topics. Similar to shell commands
def add_topic():
    """ 
    objects.get_or_create() will retrieve topic if present in model or create it.
    top_name=random.choice
    Grab [0] because of the way its formatted back
    this whole thing returns a tuple. The firt index has the reference to the created object based on the topic that we have supplied.  
    """
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    """ 
    
     """

    for entry in range(N):

        #  get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("populating complete!")