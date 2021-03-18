from django.core.management.base import BaseCommand
from .process_line import ProcessFileLine
from apps.file_to_api.models import FileControlRecord, RegisterDetail

MODEL_FIELDS = [
    'NIT', 'entity_name', 'agreement_code', 'transmission_date',
    'tracking_number', 'expiration_date', 'register_number', 'total_transaction_value'
]

FIELD_LENGTH = [1, 13, 20, 15, 8, 1, 8, 8, 17, 79]

DETAIL_REGISTER_MODEL = [
    'client_id', 'client_name', 'bank_account', 'bank_account_number',
    'transaction_type', 'transaction_value', 'validation_indicator', 'reference1',
    'reference2', 'expiration_date', 'billed_period', 'cycle'
]
DEATIL_FIELD_LENGTH = [
    1, 13, 20, 9, 17, 2, 17, 1, 30, 30, 8, 2, 3, 17
]

class Command(BaseCommand):
    help = 'Process file and fill the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='file path to process')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.read_file(file_path)
    
    def read_file(self, filepath):
        with open(filepath) as fp:
            line = fp.readline()
            count = 1
            while line:
                line = line.replace('\n', '')
                if count == 1:
                    if line[0] != '1':
                        raise ValueError("El primer caracter de la línea de control debe ser 1")
                    if line[-79:].strip():
                        raise ValueError("Los últimos 79 caracteres de línea de control son de reserva")
                    line_obj = ProcessFileLine(MODEL_FIELDS, FIELD_LENGTH, line)
                    print(line_obj.model_dict)
                    line_obj.get_date('expiration_date')
                    line_obj.get_date('transmission_date')
                    print(line_obj.model_dict)
                    line_obj.str_to_int('register_number')
                    line_obj.str_to_float('total_transaction_value')
                    print(line_obj.model_dict)
                    model_instance = FileControlRecord(**line_obj.model_dict)
                    model_instance.save()
                    
                else:
                    if line[0] != '6':
                        raise ValueError("El primer caracter de la línea de control debe ser 6")
                    if line[-17:].strip():
                        raise ValueError("Los últimos 17 caracteres de línea de control son de reserva")
                    line_obj = ProcessFileLine(DETAIL_REGISTER_MODEL, DEATIL_FIELD_LENGTH, line)
                    print(line_obj.model_dict)
                    line_obj.get_date('expiration_date')
                    line_obj.str_to_float('transaction_value')
                    print(line_obj.model_dict)
                    model_instance = RegisterDetail(**line_obj.model_dict)
                    model_instance.save()
                line = fp.readline()
                count += 1
        