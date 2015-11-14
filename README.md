# tcc3portal
a web portal by flask with Bootstrap UI
## Development Environment
At the bare minimum you'll need the following for your development environment:<br><br>
1.[Python](https://www.python.org/downloads/release/python-343/) -Version: 3.4.3<br>
2.[Mongodb](https://www.mongodb.org/)<br><br>
It is strongly recommended to also install and use the following tools:<br><br>
1.[virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv)<br>
2.[virtualenvwrapper](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenvwrapper)<br><br>
##Local Setup
The following assumes you have all of the recommended tools listed above installed.
### 1. Clone the project:
    $ git clone https://github.com/Vito2015/tcc3portal.git
    $ cd tcc3portal
### 2. Create and initialize virtualenv for the project:
    $ mkvirtualenv tcc3portal-venv
    $ pip install -r requirements.txt
### 3. Update the tcc3portal's settings, what u need:
* `SSO_CENTER_HOST`@ [sso center config](https://github.com/Vito2015/tcc3portal/blob/master/tcc3portal/settings.py\#L43-43)
* `MONGODB_SETTINGS`@ [mongodb config](https://github.com/Vito2015/tcc3portal/blob/master/tcc3portal/settings.py\#L22-23)


### 4. Run the development server:
    $ python wsgi.py
### 5. Open [http://0.0.0.0:9000/](http://0.0.0.0:9000/)
