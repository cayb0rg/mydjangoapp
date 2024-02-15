# Django Notes

## Databases

- MySQL provides test databases
- Collation = utf8_general_ci
- Use lower cases table names
- Materia uses InnoDB

Run python3 -m pip freeze > requirements.txt to get requirements

ForeignKeys are many-to-one relationships (like multiple answers being related to a single question)

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk.

## Starting

1. run  `docker-compose build` and `docker-compose up`
2. run `docker ps` to get container id
3. run `docker exec -it <container_id> bash` to go inside container
4. run `python manage.py makemigrations` (to make migrations for changes) and `python manage.py migrate` (to apply those changes to database)

If you mess up a database migration, you can reset using:
`python manage.py reset_db`
Then run `python manage.py migrate`

`python manage.py sqlmigrate` shows the SQL, but doesn’t make any changes. `python manage.py check` is similar

Primary keys added automatically

### How to get inside container and do stuff

1. docker exec -it [container_id] bash
2. python manage.py shell
3. from django.db import models
4. from polls.models import Choice, Question

### Example .env file

```
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=mydjangodb
MYSQL_USER=root
MYSQL_CHARSET=utf8
MYSQL_COLLATION=utf8_general_ci
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

## Database Queries

[Model].objects.all() returns all objects in table
[Model].objects.filter(), .exclude(), and .get() queries by keyword arguments or field lookups (`field__lookuptype=value) (such as “question_text_startswith=‘What’”)

To filter by foreign key, attach `_id` to end

### Common field lookup types

- __year
- __exact (equivalent to SELECT … WHERE [field] = [value])
  - This is the default lookup type
- __contains (equivalent to SELECT … WHERE [field] LIKE [value])
- __icontains (case insensitive)
- __startswith
- __endswith

**Foreign key sets**: Question is implicitly given the `choice_set` field to hold the “other side” of a ForeignKey relation. Use the `create` call to construct a new Choice object, call the INSERT statement, and add the choice to the set.

**Relationship spans**: Django takes care of SQL JOINs automatically. To create a relationship span, use the field names of the related fields separated by double underscores

Make your app modifiable in admin by adding `from .models import [Model]` and `admin.site.register([Model])`

I learned that creating volumes in docker-compose.yaml will allow you to share files between the host machine and Docker containers.
`volumes:`
` - ./host_directory:/container_directory `

## Views and Templates

Views return `HttpResponse` or an exception

Put templates in a subdirectory to namespace them. Like `polls/templates/polls/template.html`

**To render a template**:

- render(request, template_name, dictionary of variables/context)

Use try/except blocks for getting entries in the database. To return exceptions, use `raise`, such as `raise Http404(“Error message here”)`

`get_object_or_404()`: used for getting items from database, and if not found raises a `Http404`

Django likes to maintain loose coupling. This means raising exceptions in the view layer instead of the model layer.

dot-syntax first from dictionary lookup -> attribute lookup -> list-index lookup

`{% url %}` returns the URL definition specified in the `urls` module
Add namespaces to the URLconf to differentiate between URL names

use `request.POST` to get post data by keyname

HttpResponseRedirect redirects the user to a URL

`reverse()` is used for URL construction from view name and variable portion of the URL pattern

### Generic Views

Define classes like so: `class [View](generic.[GenericViewName]`. Must provide the model attribute or define the `get_queryset()` method

- `template_name` tells Django to use a specific template name
- `context_object_name` tells Django to override name of context variable
Can subclass built in generic views, like TemplateView, DetailView, ListView, RedirectView
- Arguments passed to `as_view()` override the attributes set on the class

Jacob Kaplan-Moss, one of Django’s original developers, says “Code without tests is broken by design.”

`Client` tests code at the view level as a user would

## Testing Principles

- Create a separate TestClass for each model or view
- Create a separate test method for each set of conditions you want to test
- Use test method name to describe their function

## Static Files

`django.contrib.staticfiles` stores location to static files

### Dedicated Server

Web server serves files in the `STATIC_ROOT` under the URL `STATIC_URL`

1. When static files change, run `collectstatic` locally
2. Push local `STATIC_ROOT` to static file server using `rsync`

### Amazon S3

<https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html>

```[language=Python]
STORAGES = {
    # ...
    "staticfiles": {"BACKEND": "myproject.storage.S3Storage"}
}
```

Run `collectstatic` to push static files to S3.
