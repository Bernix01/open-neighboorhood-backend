# Open Neighborhood

An app for a better neighborhood. Focused on four main objectives:

* Aliquot payments management.
* Visitors management.
* Neighborhood funds management. (Divide current budget into small budgets for many purposes.)
* Entrance and payments statistics for a better neighborhood understanding.

## Setup environment

### Local

0. Make sure you have installed `pipenv` [see here](https://pypi.org/project/pipenv/) and `docker` [see here](https://www.docker.com/get-started)
1. Install all deps with `pipenv install`
2. Create a `.env` file with your local information. See `.env.example`.
3. Spin up your local database and database manager with `docker-compose up -d`. Database will be running on port `5432` and `pgadmin` on port `4444`.
4. Enable your shell with the virtual environment with `pipenv shell` or just prefix every step with `pipenv run`
5. Make sure all migrations are applied to your local `python manage.py migrate`
6. Start the local server with `python manage.py runserver`

### Docker

If you have docker installed follow this steps:

0. Run `docker-compose up --build` to start all de containers. The build flag is needed to detect any dependency changes.
1. Run `docker-compose exec web bash` to start a bash terminal on the web service (our django app).
2. Within that bash terminal run `pipenv run python manage.py migrate` to run all migrations.
3. Within that bash terminal run `pipenv run python manage.py createsuperuser` to create the root admin.
4. Enjoy.

## References

* To enter pgAdmin webadmin use the following credentials:
    user = super@email.com
    password = supperpassword
* To enter Django-Admin use the following credentials:
    user = admin
    password = admin
* The "help_text" parameter is used to specify what is expected in the database models. **Bear that in mind.**
