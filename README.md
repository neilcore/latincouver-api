# latincouver-api
The primary objective of this project is to deliver a comprehensive solution that enables directors, members, and volunteers to access information efficiently in a clean, fast, and organized manner.


======================
START PROJECT
    - docker-compose up


=====================
MAKE MIGRATIONS
    - docker-compose run api python manage.py makemigrations
                                              - migrate
OR IF THE CONTAINER IS ALREADY RUNNING
    - docker-compose exec api python manage.py makemigrations
                                              - migrate


=====================
CREATE SUPERUSER
    - docker-compose run api python manage.py createsuperuser
OR IF THE CONTAINER IS ALREADY RUNNING
    - docker-compose exec api python manage.py createsuperuser


====================
Localhost address found on CORS_ALLOWED_ORIGINS are for the frontend (DEBUG true)
for the "CORS_ALLOWED_ORIGINS" on settings. change the host address if needed

=======================
JWT is configured for testing/development purposes
ACCESS_TOKEN_LIFETIME is set to 60 seconds
REFRESH_TOKEN_LIFETIME is set to 1 minute
-- FEEL FREE TO MODIFY