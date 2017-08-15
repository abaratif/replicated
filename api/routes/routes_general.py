#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_author import Author, AuthorSchema

route_path_general = Blueprint("route_path_general", __name__)


def requests_helper(urls):
    """
    Takes in a dict of username : URL pairs, and makes requests for each URL
    Returns a dict of username: request pairs after executing r
    """
    DEFAULT_ERROR = 'An unknown error has occured.'

    # Execute all the requests
    reqs = {urls[username] for username in urls.keys()}
    reqs = {requests.get(req) for req in reqs}

    # print reqs
    # return None
    response = {}

    for req in reqs:
        username = req.url.split('/')[4]
        data = json.loads(req.text)

        # Error handling
        if req.status_code != 200:
            error = data.get('message') if 'message' in data else DEFAULT_ERROR
            raise Exception(error)

        response[username] = data

    return response

def error_hanlder_helper(error):
    error = str(error)
    # print("Error handler got the error: {}".format(error))
    if 'Not Found' in error:
        return response_with(resp.INVALID_INPUT_422, value={
                'error': error
            })

    elif 'rate limit exceeded' in error:
        return response_with(resp.UNAUTHORIZED_403, value={
                'error': error
            })

    return response_with(resp.SERVER_ERROR_500, value={
        'error': error
    })

@route_path_general.route('/v1.0/keys', methods=['POST'])
def fetch_keys():
    """
    Get github keys
    ---
    consumes:
    - "application/json"
    produces:
    - "application/json"
    parameters:
        - name: users
          in: body
          description: JSON Blob with a "users" attribute, which contains a list of github usernames.
          required: true
          schema:
            type: string
    responses:
            200:
                description: Sucessfully fetched github keys for each username
                schema:
                  properties:
                    username:
                      type: array
                      items:
                        schema:
                            properties:
                                id:
                                    type: string
                                key:
                                    type: string

    """
    GH_BASE_URL = 'https://api.github.com/'

    # Read in input from POST
    data = request.get_json()

    if 'users' not in data:
        return response_with(resp.INVALID_INPUT_422, value={
                'error': "JSON Input malformed"
            })

    urls = {username: GH_BASE_URL+'users/{}/keys'.format(username) for username in data['users']}

    result = {}

    try:
        result = requests_helper(urls)

    except Exception as error:
        return error_hanlder_helper(error)

    return response_with(resp.SUCCESS_200, value={
            'data': result
    })
