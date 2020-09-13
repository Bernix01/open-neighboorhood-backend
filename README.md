# Open Neighborhood

An app for a better neighborhood. Focused on four main objectives:

* Aliquot payments management.
* Visitors management.
* Neighborhood funds management. (Divide current budget into small budgets for many purposes.)
* Entrance and payments statistics for a better neighborhood understanding.

## Setup environment

By default and as expected by the `DEBUG` env var the project will try to load the frontend from a dev server on port 3000 (check the frontend repo for instructions) it's not required but this way you could develop an integration feature or test without changing the url.

### Requirements

* Python 3.x
* pipenv (`pip install pipenv`)
* Docker (_optional_)

### Local (no docker)

0. Make sure you have installed `pipenv` [see here](https://pypi.org/project/pipenv/) and `docker` [see here](https://www.docker.com/get-started) **(optional)**
1. Install all deps with `pipenv install`
2. Create a `.env` file with your local information. See `.env.example`.
3. Spin up your local database and database manager (postgres and maybe pgadmin or any of your taste). Check `settings.py` for default database name and credentials or set the right environment variables.
4. Enable your shell with the virtual environment with `pipenv shell` or just prefix every step with `pipenv run`
5. Make sure all migrations are applied to your local `python manage.py migrate`
6. Start the local server with `python manage.py runserver`

### With Docker

If you have docker installed follow this steps:

0. Run `docker-compose up --build` to start all de containers. The build flag is needed to detect any dependency changes. This will only start a postgress database and a pgAdmin container.
1. Run `pipenv install` to install all dependencies required for the project. From then you can run `pipenv shell` to conect the current terminal to the virtual environment or prepend `pipenv run` to the following steps
2. Within that bash terminal run `(pipenv run) python manage.py migrate` to run all migrations.
3. Within that bash terminal run `(pipenv run) python manage.py createsuperuser` to create the root admin.
4. Within that bash terminal run `(pipenv run) python manage.py runserver` to spinup the server.
5. Enjoy.

## Deployment

The backend is continuous delivered by github actions. Althought frontend it's not continuous integrated with the project.

To deploy the backend server with a new frontend version you must have the frontend production `build` folder. You can have either build it yourself or grab it from the latest release on the frontend repo. Just drop the build folder with all of its content on the root folder. Then run `python manage.py collectstatic` and commit the changes.

## References

* To enter pgAdmin webadmin use the following credentials:
    user = super@email.com
    password = supperpassword
* To enter Django-Admin use the following credentials:
    user = admin
    password = admin
* The "help_text" parameter is used to specify what is expected in the database models. **Bear that in mind.**
