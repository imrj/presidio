from presidio_anonymizer.anonymizer_parameters import Validators


class ReplaceParameters(dict):

    def validate_and_normalize_fields(self):
        pass

    def get_type(self):
        return "replace"

    def get_new_value(self):
        self.get("new_value")
