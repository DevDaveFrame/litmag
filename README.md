# Litmag (Pytest Playground)
This repo implements a (very) basic dockerized REST API to demonstrate writing django tests with pytest.

## Getting Started
Fork and clone this repo on your local machine
### Running the app (on Docker)
run the following from the `litmag` directory:
~~~
docker-compose up
~~~
### Running the app (locally)
To run the app locally, you'll need to have postgress installed on your machine:
~~~
brew install postgres
~~~
Create and activate a virtual environment with virtualenv:
~~~
virtualenv venv
source venv/bin/activate
~~~
Install the required dependencies from requirements.txt:
~~~
pip install -r requirements.txt
~~~
Make migrations and run the server:
~~~
python manage.py runserver
~~~