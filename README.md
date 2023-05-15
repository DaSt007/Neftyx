# NEftyx

Vyukovy projek napsany v jazyce Python, pouzivajici webovy framework [Flask](https://flask.palletsprojects.com/en/2.3.x/) pro back-end.

Pro front-end pouzivam [Bootstrap5](https://getbootstrap.com/docs/5.2/getting-started/introduction/).

Je to dobra stranka na ktery jsou kotatka a filmy.

## Takhle se to pousti na localhostu

S livereloadem:

```
source ./venv/Scripts/activate
python start.py
```

Bez livereloadu:

```
flask --app app run --debug -p 8000
```