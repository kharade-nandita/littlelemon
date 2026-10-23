Little Lemon Restaurant API
Meta Back-End Developer Capstone Project

Endpoints:
GET/POST                 /api/menu/
GET/PUT/PATCH/DELETE     /api/menu/<id>/
GET/POST                 /api/booking/
GET/PUT/PATCH/DELETE     /api/booking/<id>/
POST                     /api/api-token-auth/
POST                     /auth/token/login/
POST                     /auth/token/logout/
GET/POST                 /auth/users/
POST                     /auth/users/ (registration)

Run:
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py runserver
pipenv run python manage.py test restaurant
