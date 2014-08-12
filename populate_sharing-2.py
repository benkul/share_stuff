import os

# Populates database with data for-
#   User (username, first_name, last_name, email, password,)
#   Member (profile_picture, zip_code)
#   Item (member, name, category, description, photo)

def populate():
    # add member with one item
    user_1 = add_user('John1', 'John', 'Halifax', 'test1@gmail.com', 123)
    member_1 = add_member(user_1, 'profile_images/2014-03-21_15.03.25.jpg',
                '97210')
    add_item(member_1, 'Volt Meter', 'Electronics', 'works OK', 
            'item_images/Drill.jpeg')

    # add member with two items
    user_2 = add_user('Sean1', 'Sean', 'Johnson', 'test1@gmail.com', 123)
    member_2 = add_member(user_2, 'profile_images/2014-03-21_15.03.25.jpg',
                '97210')
    add_item(member_2, 'Drill', 'Tools', 'works OK', 
            'item_images/Drill.jpeg')

    add_item(member_2, 'Juicer', 'Kitchen', 'works OK', 
            'item_images/Drill.jpeg')

    # add member with no items
    user_3 = add_user('Sally1', 'Sally', 'Smith', 'test1@gmail.com', 123)
    member_3 = add_member(user_3, 'profile_images/2014-03-21_15.03.25.jpg',
                '97210')

    # add group 
    # member_list_1 = [member_1, member_2]
    moderator_1 = add_moderator(member_1)
    group_1 = add_group(moderator_1, 'Group 1', "The Best Group Ever")

    for i in Item.objects.all():
        print "- {0}".format(str(i))

    for m in Member.objects.all():
        print "- {0}".format(str(m))

    for m in Moderator.objects.all():
        print "- {0}".format(str(m))

    for g in Group.objects.all():
        print "- {0}".format(str(g))

# ********group.member.add()*************


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

def add_moderator(member):
    mod = Moderator.objects.get_or_create(member=member)[0]
    return mod

def add_group(moderator, name, description):
    g = Group.objects.get_or_create(moderator=moderator, name=name,
                description=description,)[0]
    return g


if __name__ == '__main__':
    print "Starting Sharing population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share_stuff.settings')
    from sharing.models import Item, Member, Group, Moderator
    from django.contrib.auth.models import User


    populate()

