from . import models
from django.urls import path
import json
import requests

import os

def get_archive_all():
    AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    data = requests.get(
        "https://baserow-production-f90e.up.railway.app/api/database/rows/table/75/?user_field_names=true&order_by=Date",
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data["results"]

def get_archival_material(row_id):
    AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    request_string = "https://baserow-production-f90e.up.railway.app/api/database/rows/table/75/" + str(row_id) + "/?user_field_names=true"
    data = requests.get(
        request_string,
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data

def get_press_all():
    AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")
    AUTH_STRING = "Token " + AUTHORIZATION_TOKEN
    data = requests.get(
        "https://baserow-production-f90e.up.railway.app/api/database/rows/table/76/?user_field_names=true&order_by=Date",
        headers={
            "Authorization": AUTH_STRING
            }).json()

    return data["results"]
