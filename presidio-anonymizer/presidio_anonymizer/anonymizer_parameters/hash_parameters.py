from presidio_anonymizer.anonymizer_parameters import Validators


class HashParameters(dict):

    def validate_and_normalize_fields(self):
        Validators.validate_exists(("old_text",), self, self.get_type())

    def get_old_text(self):
        self.get("old_text")

    def get_type(self):
        return "hash"
