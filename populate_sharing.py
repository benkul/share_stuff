import os

# ****This is from Tango with Django. Have just begun to modify to fit Sharing App

def populate():
    member_1 = add_member('John1', John, Halifax, test1@gmail.com, 123, 
                C:/ksjflksd/sf, 97210
    member_2 = add_member('Sean1', Sean, Johnson, test1@gmail.com, 123, 
                C:/ksjflksd/sf, 97212

    add_item( ):

    # Print out what we have added to the user.
    for m in Member.objects.all():
        for i in Item.objects.filter(member=c):
            print "- {0} - {1}".format(str(m), str(i))

def add_member(User, pic, zip):
    m = Member.objects.get_or_create(User=User, pic=profile_picture,
            zip=zip_code,)

    return m

def add_member (username, first, last, email, passw, pic, zip):
    m = Member.objects.get_or_create(username=username, first=first_name,
            last=last_name, email=email, passw=password, pic=profile_picture,
            zip=zip_code)

    return m

def add_item(name, category, description, photo):
    i = Item.objects.get_or_create(name=name, category=category,
            description=description, photo=photo)
    return i

# Start execution here!
if __name__ == '__main__':
    print "Starting Sharing population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_stuff.settings')
    from sharing.models import Member, Item, Group

    populate()
