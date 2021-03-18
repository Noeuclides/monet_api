import datetime 
  

class ProcessFileLine:
    def __init__(self, model_fields: list, field_length: list, line: str) -> None:
        self.model_fields = model_fields
        self.cummulatives = self.get_cumulative_field(field_length)
        self.model_dict = self.create_model_dict(line, self.zip_model_fields())

    def get_cumulative_field(self, length_list: list) -> list:
        cummulative = 0
        cummulative_list = []
        for elem in length_list:
            cummulative += elem
            cummulative_list.append(cummulative)
        return cummulative_list

    def zip_model_fields(self) -> zip:
        return zip(self.model_fields, self.cummulatives[0:-2], self.cummulatives[1:])

    def create_model_dict(self, line: str, zip_obj: zip) -> dict:
        return {key: line[start:end] for key, start, end in zip_obj}

    def get_date(self, key: str) -> None:
        key_date = datetime.datetime.strptime(self.model_dict[key], '%Y%m%d')
        self.model_dict[key] = key_date.date()

    def str_to_int(self, key: str) -> None:
        self.model_dict[key] = int(self.model_dict[key])

    def str_to_float(self, key: str) -> None:
        val = self.model_dict[key]
        self.model_dict[key] = float(val[:-2] + '.' + val[-2:])



