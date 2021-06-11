# Setting up the project

https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

``` bash
# Project directory
$ mkdir project
$ cd project

# Configure virtualenv + dependencies
$ python -m venv venv
$ venv/Scripts/activate
(venv)$ pip install Flask python-dotenv
(venv)$ pip freeze > requirements.txt
```

Instead of make a `export FLASK_APP = app.py` each time you access, create a `.flaskenv` for the `python-dotenv` package

```
# File:   .flaskenv

FLASK_APP=run.py
FLASK_ENV=development
```


### Directory structure

To maintain a good dir structure and organize the different components

```
project/
    ├── app/
    │   ├── static/
    │   └── templates/
    ├── .flaskenv
    ├── run.py
    └── requirements.txt

/app              all the code. As /src dir in JS
/app/static       assets like CSS, JS or images
/app/templates    HTML files
```


### App logic

The system auth will be divided into 2 blocks: Auth pages, and unauth pages

```
app/
 ├── static/
 ├── templates/
 │
 ├── __init__.py     # create_app logic
 ├── auth.py         # onboarding routes (login, signup, logout)
 ├── main.py         # 'index' and authorized route 'profile'
 ├── models.py       # table structure models
 └── db.sqlite       # database sqlite3
```

---

### Install dependencies

```
$ pip install -r requirements.txt
```
