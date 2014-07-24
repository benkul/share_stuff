import os

# Populates database with data for-
#   User (username, first_name, last_name, email, password,)
#   Member (profile_picture, zip_code)
#   Item (member, name, category, description, photo)

def populate():

    user_1 = add_user('John1', 'John', 'Halifax', 'test1@gmail.com', 123)
    member_1 = add_member(user_1, 'profile_images/2014-03-21_15.03.25.jpg',
                '97210')
    add_item(member_1, 'Volt Meter', 'Electronics', 'works OK', 
            'item_images/Drill.jpeg')


    user_2 = add_user('Sean1', 'Sean', 'Johnson', 'test1@gmail.com', 123)
    member_2 = add_member(user_2, 'profile_images/2014-03-21_15.03.25.jpg',
                '97210')
    add_item(member_2, 'Drill', 'Tools', 'works OK', 
            'item_images/Drill.jpeg')

    for i in Item.objects.all():
        print "- {0}".format(str(i))

    for u in User.objects.all():
        print "- {0}".format(str(u))

    for m in Member.objects.all():
        print "- {0}".format(str(m)) 


def add_item(member, name, cat, description, photo):

    i = Item.objects.get_or_create(
                member=member,
                name=name,
                category=cat,
                description=description,
                photo=photo)[0]
    return i


def add_user(username, first, last, email, passw): 
    u = User.objects.get_or_create(username=username,
                first_name=first,
                last_name=last,
                email=email,
                password=passw)[0]
    u.set_password(u.password)
    u.save()

    return u


def add_member(user, pic, zip):
    m = Member.objects.get_or_create(user=user, profile_picture=pic,
                zip_code=zip)[0]
    return m


if __name__ == '__main__':
    print "Starting Sharing population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_stuff.settings')
    from sharing.models import Item, Member
    from django.contrib.auth.models import User


    populate()

