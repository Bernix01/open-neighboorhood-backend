# Open Neighborhood

An app for a better neighborhood. Focused on four main objectives:

* Aliquot payments management.
* Visitors management.
* Neighborhood funds management. (Divide current budget into small budgets for many purposes.)
* Entrance and payments statistics for a better neighborhood understanding.

## Setup environment

1. Install all deps with `pip install -r requirements.txt`
2. Create a `.env` file with your local information. See `.env.example`.
3. Make sure all migrations are applied to your local `python manage.py migrate`
4. Start the local server with `python manage.py runserver`


## References
* For enter Django-Admin use the next credentials:
    user = admin 
    password = admin
* The "help_text" parameter is to specify what is expected in the database models