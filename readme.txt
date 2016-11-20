// start virtual environment
virtualenv env
source env/bin/activate

//install requirement

pip install -r requirements.txt

//migrate db
python manage.py migrate
