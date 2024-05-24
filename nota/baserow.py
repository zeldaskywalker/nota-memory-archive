from . import models
from django.urls import path
import json
import requests

def get_archive_all():
    data = requests.get(
        "https://baserow.nota.im/api/database/rows/table/131/?user_field_names=true&order_by=Date",
        headers={
            "Authorization": "Token LDNBHCatq2lPFEd2LUEh2r6SIstAA9y8"
            }).json()

    return data["results"]

def get_archival_material(row_id):
    request_string = "https://baserow.nota.im/api/database/rows/table/131/" + str(row_id) + "/?user_field_names=true"
    data = requests.get(
        request_string,
        headers={
            "Authorization": "Token LDNBHCatq2lPFEd2LUEh2r6SIstAA9y8"
            }).json()

    return data

def get_press_all():
    data = requests.get(
        "https://baserow.nota.im/api/database/rows/table/133/?user_field_names=true&order_by=Date",
        headers={
            "Authorization": "Token LDNBHCatq2lPFEd2LUEh2r6SIstAA9y8"
            }).json()

    return data["results"]