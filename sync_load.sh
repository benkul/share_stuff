# Script to run syncdb, loaddata, and populate_sharing.py

# delete database
rm sharing.db

# run syncdb command without input prompts
python manage.py syncdb --noinput

# run loaddata command to reload superuser authorization
python manage.py loaddata auth.json

# run populate_sharing.py file
python populate_sharing.py
