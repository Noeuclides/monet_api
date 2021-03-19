import os
from django.core.management import call_command
from django.test import TestCase
from apps.file_to_api.models import FileControlRecord


class TestCommand(TestCase):

    def test_invalid_control_line(self):
        base_path = os.path.abspath('apps/file_to_api/tests/test_files')
        filepath = os.path.join(base_path, "invalid_type_first_line.txt")
        with self.assertRaises(ValueError, msg='El primer caracter de la línea de control debe ser 1'):
            call_command('file_process', filepath)

    def test_invalid_detail_line(self):
        base_path = os.path.abspath('apps/file_to_api/tests/test_files')
        filepath = os.path.join(base_path, "invalid_type_second_line.txt")
        with self.assertRaises(ValueError, msg='El primer caracter de la línea de control debe ser 6'):
            call_command('file_process', filepath)

    def test_invalid_length_line(self):
        base_path = os.path.abspath('apps/file_to_api/tests/test_files')
        filepath = os.path.join(base_path, "invalid_line_length.txt")
        with self.assertRaises(ValueError, msg='Línea no válida'):
            call_command('file_process', filepath)

    def test_create_instance_db(self):
        base_path = os.path.abspath('apps/file_to_api/tests/test_files')
        filepath = os.path.join(base_path, "create_model_instance.txt")
        call_command('file_process', filepath)
        control = FileControlRecord.objects.get(id=1)
        self.assertEquals(control.entity_name, 'TestTech')
