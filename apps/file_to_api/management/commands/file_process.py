from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from .process_line import ProcessFileLine
from apps.file_to_api.models import FileControlRecord, RegisterDetail
from .model_lists import (
    MODEL_FIELDS, FIELD_LENGTH, DETAIL_REGISTER_MODEL, DEATIL_FIELD_LENGTH
)


class Command(BaseCommand):
    help = 'Process file and fill the database'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file_path', type=str, help='file path to process')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.read_file(file_path)

    def read_file(self, filepath: str) -> None:
        with open(filepath) as fp:
            line = fp.readline()
            count = 1
            while line:
                line = line.replace('\n', '')
                if count == 1:
                    if line[0] != '1':
                        raise ValueError(
                            "El primer caracter de la línea de control debe ser 1")
                    if line[-79:].strip():
                        raise ValueError(
                            "Los últimos 79 caracteres de línea de control son de reserva")
                    self.save_model_instance(
                        FileControlRecord, MODEL_FIELDS, FIELD_LENGTH, line)
                else:
                    if line[0] != '6':
                        raise ValueError(
                            "El primer caracter de la línea de control debe ser 6")
                    if line[-17:].strip():
                        raise ValueError(
                            "Los últimos 17 caracteres de línea de control son de reserva")
                    self.save_model_instance(
                        RegisterDetail, DETAIL_REGISTER_MODEL,
                        DEATIL_FIELD_LENGTH, line)
                line = fp.readline()
                count += 1

    def clean_field(
            self,
            obj_instance: ProcessFileLine,
            key_list: list,
            type_to_clean: str) -> None:
        for key in key_list:
            if type_to_clean == 'date':
                obj_instance.get_date(key)
            if type_to_clean == 'int':
                obj_instance.str_to_int(key)
            if type_to_clean == 'float':
                obj_instance.str_to_float(key)

    def save_model_instance(
            self,
            model: Any,
            model_list: list,
            field_length: list,
            line: str) -> None:
        line_obj = ProcessFileLine(model_list, field_length, line)
        self.clean_field(
            line_obj, ['expiration_date', 'transmission_date'], 'date')
        self.clean_field(line_obj, ['register_number'], 'int')
        self.clean_field(
            line_obj, [
                'total_transaction_value', 'transaction_value'], 'float')

        model_instance = model(**line_obj.model_dict)
        model_instance.save()
