from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware

import requests

from retriever.models import Article


def retrieve_and_save(base_url, quantity):
    """
    Retrieves and saves articles using WordPress REST API from specified
    WordPress site.

    :param base_url: The base URL for the WordPress api for the specified site
    :param quantity: The number of articles to retrieve and save
    """
    articles = get_articles(base_url, quantity)
    for article in articles:
        author_id = article['author']
        author = get_author(base_url, author_id)
        save_article(article, author)


def get_articles(base_url, quantity):
    """
    Retrieves articles using WordPress REST API from specified WordPress site.

    Documentation: https://developer.wordpress.org/rest-api/

    :param base_url: The base URL for the WordPress api for the specified site
    :param quantity: The number of articles to retrieve and save
    """
    response = requests.get('{}/posts?per_page={}'.format(base_url, quantity))
    articles = response.json()
    return articles


def save_article(article, author):
    """
    Builds Article from retrieved data and saves to DB.

    :param article: A dictionary representing the article data
    :param author: A dictionary representing the author data
    """
    source_id = article['id']
    date_published = get_date_published(article['date_gmt'])
    author_name = author['name'] if 'name' in author else ''
    title = article['title']['rendered'] if article['title'] else ''
    url = article['link']
    content = article['content']['rendered'] if article['content'] else ''

    Article.objects.create(
        source_id=source_id,
        date_published=date_published,
        author=author_name,
        title=title,
        url=url,
        content=content
    )

    print("Saved article '{}' published {}.".format(title, date_published.strftime("%b %d, %Y")))


def get_date_published(date_string):
    """
    Parses datetime string and makes timezone aware

    :param date_string: String representation of published datetime
    :return: Datetime representation of published datetime
    """
    return make_aware(parse_datetime(date_string))


def get_author(base_url, author_id):
    """
    Retrieves author information using WordPress REST API from specified WordPress site
    for specified author id.

    Documentation: https://developer.wordpress.org/rest-api/

    :param base_url: The base URL for the WordPress api for the specified site
    :param author_id: The author id
    """
    if author_id is None:
        return ''
    response = requests.get('{}/users/{}'.format(base_url, author_id))
    author = response.json()
    return author
