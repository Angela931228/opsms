// start virtual environment
virtualenv env
source env/bin/activate

//install requirement

pip install -r requirements.txt


//update database
python manage.py makemigrations
python manage.py migrate
