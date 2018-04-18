usage: `dbshell [-h] [DATABASE_URL]`

Runs a database command-line client given a database URL.

Invokes Django's
[dbshell](https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell)
management command to connect to a database  whose connection parameters are
specified as a database URL either as a command-line parameter or via the
`DATABASE_URL` environment variable.

For valid database URL values, see:
[https://github.com/kennethreitz/dj-database-url](https://github.com/kennethreitz/dj-database-url)

positional arguments:
  `DATABASE_URL`

optional arguments:
   `-h, --help`    show this help message and exit
