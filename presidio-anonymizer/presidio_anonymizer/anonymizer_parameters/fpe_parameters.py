from presidio_anonymizer.anonymizer_parameters import Validators


class FPEParameters(dict):

    def validate_and_normalize_fields(self):
        Validators.validate_exists(("old_text", "decrypt", "tweak", "key"), self,
                                   self.get_type())

    def get_type(self):
        return "FPE"

    def get_old_text(self):
        self.get("old_text")

    def get_decrypt(self):
        self.get("decrypt")

    def get_tweak(self):
        self.get("tweak")

    def get_key(self):
        self.get("key")
