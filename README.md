# ❝ QuoteBox

![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A minimal personal quote collection app built with Django. Submit quotes, approve them via the admin panel, and serve a random one on the homepage.

## Features

- **Random quote** on the homepage — refreshes on every visit
- **Submit quotes** via a simple form (text + author)
- **Admin approval workflow** — quotes are hidden until approved
- **All quotes list** — browse every approved quote with date
- **SQLite** — zero-config database, works out of the box

## Quick Start

```bash

# 1. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create an admin user
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Pages

| URL | Description |
|-----|-------------|
| `/` | Homepage — shows a random approved quote |
| `/quotes/` | List of all approved quotes |
| `/add/` | Form to submit a new quote |
| `/admin/` | Django admin panel |

## Admin Panel

Log in at `/admin/` to manage quotes.

- The **Approved** column has inline checkboxes for quick toggling
- Use the **Actions** dropdown to bulk approve or unapprove selected quotes
- Newly submitted quotes default to **unapproved** and are hidden from public pages until approved

## Project Structure

```
quote_project/
├── manage.py
├── requirements.txt
├── .gitignore
├── db.sqlite3
├── quote_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quotes/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates/
    ├── base.html
    └── quotes/
        ├── home.html
        ├── add_quote.html
        └── quote_list.html
```

## Data Model

```python
class Quote(models.Model):
    text       = TextField()
    author     = CharField(max_length=200)
    approved   = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
```

## Requirements

- Python 3.8+
- Django 4.2+

## Going Further

Some natural next steps if you want to extend the app:

- **Tags** — categorise quotes by topic and filter by tag
- **Search** — full-text search across quote text and authors
- **Favourites** — let visitors like or star quotes
- **Pagination** — keep the list page fast as quotes accumulate
- **User accounts** — let registered users track their own submissions
- **REST API** — JSON endpoints to back a mobile app or frontend
- **Export** — download the full collection as CSV or JSON

## License

MIT — do whatever you like with it.
