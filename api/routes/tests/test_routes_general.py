#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from api.utils.test_base import BaseTestCase
# from api.models.model_author import Author
# from api.models.model_book import Book
# from datetime import datetime


# def create_authors():
#     author1 = Author(name="John", surname="Doe").create()
#     Book(title="Test Book 1", year=datetime(1976, 1, 1), author_id=author1.id).create()
#     Book(title="Test Book 2", year=datetime(1992, 12, 1), author_id=author1.id).create()

#     author2 = Author(name="Jane", surname="Doe").create()
#     Book(title="Test Book 3", year=datetime(1986, 1, 3), author_id=author2.id).create()
#     Book(title="Test Book 4", year=datetime(1992, 12, 1), author_id=author2.id).create()


class TestAPI(BaseTestCase):
    # def setUp(self):
    #     super(TestAuthors, self).setUp()
    #     create_authors()

    # def test_get_authors(self):
    #     response = self.app.get(
    #         '/api/v1.0/authors',
    #         content_type='application/json'
    #     )
    #     data = json.loads(response.data)
    #     self.assertEqual(200, response.status_code)
    #     self.assertTrue('authors' in data)

    # def test_get_author_detail(self):
    #     response = self.app.get(
    #         '/api/v1.0/authors/1',
    #         content_type='application/json'
    #         )
    #     data = json.loads(response.data)
    #     self.assertEqual(200, response.status_code)
    #     self.assertTrue('author' in data)

    def test_keys_1(self):
        """
            Test to get keys using hardcoded usernames
        """
        users = {
            'users': [
                'kennethreitz',
                'gvanrossum',
                'abaratif'
            ]
        }

        response = self.app.post(
            '/api/v1.0/keys',
            data=json.dumps(users),
            content_type='application/json'
            )
        self.assertEqual(200, response.status_code)


        json_response = json.loads(response.data)
        self.assertTrue('data' in json_response)

        data = json_response['data']

        self.assertTrue('abaratif' in data)
        self.assertTrue('gvanrossum' in data)

        self.assertTrue(len(data['gvanrossum']) == 1)
        self.assertTrue(len(data['abaratif']) == 0)
        self.assertTrue(len(data['kennethreitz']) == 4)

    def test_keys_2(self):
        """
            Test getting keys for a single user.
        """
        users = {
            'users': [
                'gvanrossum'
            ]
        }

        response = self.app.post(
            '/api/v1.0/keys',
            data=json.dumps(users),
            content_type='application/json'
            )
        self.assertEqual(200, response.status_code)

        json_response = json.loads(response.data)
        self.assertTrue('data' in json_response)

        data = json_response['data']

        self.assertTrue('gvanrossum' in data)
        self.assertTrue(len(data['gvanrossum']) == 1)

    def test_keys_3(self):
        """
            Test getting keys for an invalid username.
            Server should respond with code 422, invalid input
        """

        users = {
            'users': [
                'abaratif_is_cool'
            ]
        }

        response = self.app.post(
            '/api/v1.0/keys',
            data=json.dumps(users),
            content_type='application/json'
            )
        self.assertEqual(422, response.status_code)

    def test_keys_4(self):
        """
            Test getting keys with malformed input
        """
        users = {
            'whosers': [
                'guy1'
            ]
        }

        response = self.app.post(
            '/api/v1.0/keys',
            data=json.dumps(users),
            content_type='application/json'
            )
        self.assertEqual(422, response.status_code)

    # def test_keys_5(self):
        """
        *****
        Do not uncomment unless prepared to exceed github api rate limit
        *****

        Test getting keys for many users,
        exceeding the rate limit for un-authenticated requests
        """
        # REPEAT_COUNT = 50

        # usernames = ['gvanrossum'] * REPEAT_COUNT

        # users = {
        #     'users' : usernames
        # }

        # response = self.app.post(
        #     '/api/v1.0/keys',
        #     data=json.dumps(users),
        #     content_type='application/json'
        #     )
