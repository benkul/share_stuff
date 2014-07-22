import os

# ****This is from Tango with Django. Have just begun to modify to fit Sharing App

def populate():
    python_cat = add_cat('Python',
        views=128,
        likes=64,)

    add_member(cat=python_cat,
        title="Official Python Tutorial",
        url="httpL//docs.python.org/2/tutorial/")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, views=0, likes=0,):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Sharing population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharing.settings')
    from sharing.models import Member

    populate()