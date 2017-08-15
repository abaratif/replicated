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

    usernames = data['users']

    result = {}


    for username in usernames:

        try:
            r = requests.get(GH_BASE_URL+'users/{}/keys'.format(username))
            data = json.loads(r.text)

            # Error handling
            if r.status_code != 200:
                error = 'An unknown error has occured.'

                if 'message' in data:
                    error = data['message']

                if error == 'Not Found':
                    return response_with(resp.INVALID_INPUT_422, value={
                            'error': error
                        })
                
                elif 'rate limit exceeded' in error:
                    return response_with(resp.INVALID_INPUT_403, value={
                            'error': error
                        })

                else:
                    raise Exception(error)

            result[username] = data

        except Exception as e:
            return response_with(resp.SERVER_ERROR_500, value={
                'error': str(e)
            })

    return response_with(resp.SUCCESS_200, value={
            'data': result
    })
