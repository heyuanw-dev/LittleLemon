Run <python manage.py runserver> to start the server

Testable urls:
http://127.0.0.1:8000/admin/ (admin site of the project)
http://localhost:8000/restaurant/booking/tables (table booking operations, token authentication required)
http://127.0.0.1:8000/restaurant/menu-items/ (list all menu items)
http://127.0.0.1:8000/restaurant/menu-items/<int:pk> (list a single menu item)
http://127.0.0.1:8000/auth/token/login/ (obtain a token for the user)
