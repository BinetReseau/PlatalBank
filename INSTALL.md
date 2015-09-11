# Dependencies

D'abord, installez `python3` et `pip`:

    # Sous une Debian-like
    apt-get install python3 python3-pip libsasl2-dev

    # Sous Archlinux
    pacman -S python python-pip libsasl # et si vous préférez l'installer avec pacman, python-django

    # Sous OSX, passer par brew. Si confronté à un problème avec sasl, tenter ceci :
    xcrun --show-sdk-path
    sudo ln -s <the_path_from_above_command>/usr/include /usr/include

Puis utilisez `pip` pour télécharger les paquets python nécessaires:

    pip3 install -r requirements.txt

## Optional dependencies

    bpython3

# Running the server

## Generating the database

First, generate the migration file:

    python3 manage.py makemigrations

Then, create the db.sqlite3 file using this migration:

    python3 manage.py migrate

## Running the server

Once you have the db.sqlite3 file, you are ready to run the server:

    python3 manage.py runserver
