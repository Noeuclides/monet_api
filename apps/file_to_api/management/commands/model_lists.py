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
