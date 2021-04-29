git clone https://github.com/Fanni98/django.git
parancssorba: pip install virtualenv
cd django
virtualenv venv
cd venv\Scripts
activate
cd../.. kimegyünk a django mappáig
pip install -r requirements.txt
manage.py runserver
tesztek futtatása: manage.py test
