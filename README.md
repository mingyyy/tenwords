# Ten words about me

A project aims to combine the two popular arenas of Python: web application development and data visualization.
The ultimate goal of the project is a platform for everyone to visualize how people thinking of them 
by collecting ten adjectives from their family, friends and acquaintances. 

## How does this work?

1. Register as a user
2. Generate a unique code and a link (related to your username)
3. Send this link to people you want to hear their opinions
4. Accessing the page based on the link, you friend enter <= 10 words about your
5. Submit their words, then look at the results and analytics about you!
6. You can come to the result page and check your dashboard

## Structure of the Project
```
project_tenwords
    |-- .venv
    |-- tenwords
        |__ __init__.py
        |__ settings.py
        |__ urls.py
        |__ wsgi.py
    |-- core
        |__ migrations
        |__ __init__.py
        |__ admin.py
        |__ apps.py
        |__ models.py
        |__ tests.py
        |__ urls.py
        |__ views.py

    |-- user
        |__ migrations
        |__ __init__.py
        |__ admin.py
        |__ apps.py
        |__ models.py
        |__ tests.py
        |__ urls.py
        |__ views.py    
    |-- templates
        |-- core
            |__ base.html
            |__ home.html
            |__ words.html
            |__ dashboard.html
        |-- user
            |__ register.html
            |__ login.html
            |__ logout.html
            |__ profile.html
    |-- static
    .gitignore
    

```
