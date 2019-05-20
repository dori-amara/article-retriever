# article-retriever
Provides ability to retrieve and save articles using WordPress REST API

# To run utility locally

Clone repository.

    git clone https://github.com/dori-amara/article-retriever.git

Create virtual environment.

    python3 -m venv venv

Activate virtual environment.

    source venv/bin/activate

Install requirements.

    pip install -r requirements.txt

Run migrations.

    ./manage.py migrate

Create superuser.

    ./manage.py createsuperuser

Optionally, run tests.

    ./manage.py test

Run utility.

    ./manage.py retrieve_techcrunch_top_100.py

# View Results

Run server locally 

    ./manage.py runserver
    
Navigate to admin page in webrowser 

    http://127.0.0.1:8000/admin/
    
Log in using superuser

View Articles