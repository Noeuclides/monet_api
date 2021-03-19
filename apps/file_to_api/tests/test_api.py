import os
import json
from django.core.management import call_command
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class TestAPI(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestAPI, cls).setUpClass()
        base_path = os.path.abspath('apps/file_to_api/tests/test_files')
        filepath = os.path.join(base_path, "test_file.txt")
        call_command('file_process', filepath)

    def test_request_control_endpoint(self):
        client = APIClient()
        response = client.get('/api/control/1')
        obj_created = {
            "id": 1,
            "register_type": 1,
            "NIT": "0000901371820",
            "entity_name": "ElefanteTech",
            "agreement_code": "000000000010948",
            "transmission_date": "2021-03-09",
            "tracking_number": "P",
            "expiration_date": "2021-03-09",
            "register_number": 5,
            "total_transaction_value": 100000.0}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), obj_created)

    def test_request_detail_endpoint(self):
        client = APIClient()
        response = client.get('/api/detalle/1')
        obj_created = {
            "id": 1,
            "register_type": 6,
            "client_id": "5654545",
            "client_name": "PRUEBA TES",
            "bank_account": "",
            "bank_account_number": "",
            "transaction_type": "",
            "transaction_value": 32000.0,
            "validation_indicator": "N",
            "reference1": "5654545",
            "reference2": "RECEIVABLE_896375",
            "expiration_date": "2021-03-09",
            "billed_period": "",
            "cycle": ""}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), obj_created)
