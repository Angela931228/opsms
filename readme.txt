// start virtual environment
virtualenv env
source env/bin/activate

//install requirement

pip install -r requirements.txt

//django sitetree

add sitetree in installed app

python manage.py migrate
