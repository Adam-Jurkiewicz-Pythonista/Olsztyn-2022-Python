# Flask - aplikacja Webowa

Korzystamy z materiałów:
- https://python101.readthedocs.io/pl/latest/webflask/todo/index.html#dodawanie-zadan - obsługa formularza we Flasku
- https://github.com/programujemy-python/programuj-w-zespole/blob/main/teachers_sample_codes/zajecia_01/bootstrap_page.html  - Strona html
- https://getbootstrap.com/docs/5.2/forms/form-control/#example - przykłady formularza do wpisania IP
- https://ipstack.com/ - API do generowania informacji
- IP klinta - https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data

```python
from flask import request
request.remote_addr
request.environ['REMOTE_ADDR']
```

Jeśli starczy czasu to deployment na Heroku