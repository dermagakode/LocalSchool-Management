Local School Management
=======================

Management is deployed to cloud server to serve LocalSchool Edge. It helps school to manage their student attendance and to publish their teaching materials.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: GPLv3

Contributing
------------

Git Commit and Git Flow 
^^^^^^^^^^^^^^^^^^^^^^^^

Please add an issue if you have feature request or found a bug. You can fork this repo then request a Pull Request.

We use :code:`pre-commit` to make sure everything is good before commiting. Install it with::

  pre-commit install

if you can't commit, probably you need to introduce the hook::

  git config core.hooksPath .git/hooks/pre-commit


Run Local
^^^^^^^^^

Install postgres and redis or use docker compose below

::
  docker-compose -f utility/docker-compose.yml up -d

Set up virtual environment

.. code-block:: bash
  mkvirtualenv localshool_management # change if you use venv or pyenv
  pip install -r requirements/local.txt


We will use env file stored in :code:`.envs/local`. Copy :code:`.secret.example` as :code:`.secret`, then run::

  export DJANGO_READ_DOT_ENV_FILE=True
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py run


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy localshool_management

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd localshool_management
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html




