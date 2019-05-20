import unittest
from unittest.mock import patch

from retriever.utils import retrieve_and_save


class TestRetrieveAndSave(unittest.TestCase):

    @patch('retriever.utils.save_article')
    @patch('retriever.utils.get_author')
    @patch('retriever.utils.get_articles')
    def test_retrieve_and_save(self, mock_get_articles, mock_get_author, mock_save_article):
        # Given: A base url
        base_url = 'https://techcrunch.com/wp-json/wp/v2'

        # Given: A quantity
        quantity = 3

        # Given: A call to get_articles returns a list of 3 articles (minimally represented here)
        mock_get_articles.return_value = [{'author': '1'}, {'author': '2'}, {'author': '3'}]

        # Given: A call to get_author returns an author
        mock_get_author.return_value = "Author Name"

        # Given: A call to save_article succeeds

        # When: We retrieve and save
        retrieve_and_save(base_url, quantity)

        # Then: get_articles is called
        mock_get_articles.assert_called_once_with(base_url, quantity)

        # And: get_author is called for each article
        assert quantity == mock_get_author.call_count

        # And: save_article is called for each article
        assert quantity == mock_save_article.call_count
