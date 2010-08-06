Installing Burning Man Earth Using "Buildout"
---------------------------------------------

This is much faster and easier than the old method.  It is slightly Ubuntu specific at the moment.

* Make sure you have "sudo" rights::

 su
 visudo

* In the resulting editor, add something like::

 YOURUSERNAME ALL=(ALL) ALL

* Install Python prerequisites::

 sudo easy_install virtualenv
 sudo easy_install mercurial

* Install OS dependencies::

 sudo apt-get install flex postgresql-8.3 postgresql-server-dev-8.3 libpq-dev

* Make your virtual env sandbox for the project::

 virtualenv bmedev
 cd bmedev
 source bin/activate

* In your bmedev directory, check out the BME code::

 hg clone https://earthdev.burningman.com/hg/bme

* Link (or copy if you are on Windows) the buildout scripts to the root of the project::

 ln -s bme/build/b* .

* Run the buildout based autoinstaller::

 # you only need to do this first step the first time, and then run the second step
 python bootstrap.py

 # every other time you want to update your install, just use this
 # the first time you run buildout, it will need to do some work as root, so it will
 # prompt you for your password.
 # then, it will prompt several more times for a password - this one is the database password
 # for the postgres user.  Not everyone has a password for that user, so it may just work
 # without the extra password prompting
 buildout

* Make your database (here named 'bme', but it can be whatever you like)::

sudo -u postgres createdb bme -E UTF8 -T template_postgis

* Either load a copy of the database, or else run a syncdb.  If you want to run a syncdb, make sure to put "INITIAL_SYNC=True" in your local_settings file, or it won't work the first time.  **notice that the command is "django" not "./manage".**  The "django" script adds all the sandboxed eggs and directories.

 django syncdb

* Load some sample data:

 django manage.py loaddata fixtures/*json

* Start the dev server:

 django runserver

