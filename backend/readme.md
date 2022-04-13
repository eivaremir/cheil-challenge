## Proyect Setup

1. install pip dependencies `pip install -r requirements.txt`.
2. For linux do, execute the following commands before step 3:
   1. `sudo apt install python3-dev build-essential`
   2. `sudo apt install libssl1.1`
   3. `sudo apt install libssl1.1=1.1.1f-1ubuntu2`
   4. `sudo apt install libssl-dev`
   5. `sudo apt install libmysqlclient-dev`
3. Connect to your MySQL Server and create a new schema called `cheil`
4. Create migrations with `python manage.py makemigrations`
5. Apply migrations with `python manage.py migrate`
6. Run server with `python manage.py runserver`

## Django API Admin

The API include with itself a django admin site accesible via `localhost:8000/admin`. Before you access this you need to create a superuser with `python manage.py createsuperuser` and use this access for log into the admin site.
