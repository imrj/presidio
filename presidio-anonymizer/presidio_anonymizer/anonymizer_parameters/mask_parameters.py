import logging

from presidio_anonymizer.anonymizer_parameters import Validators


class MaskParameters(dict):
    logger = logging.getLogger("presidio-anonymizer")

    def validate_and_normalize_fields(self):
        Validators.validate_exists(("masking_char", "chars_to_mask", "from_end"),
                                   self, self.get_type())

    def get_masking_char(self):
        self.get("masking_char")

    def get_chars_to_mask(self):
        self.get("chars_to_mask")

    def get_from_end(self):
        self.get("from_end")

    def get_type(self):
        return "mask"

    def get_effective_chars_to_mask(self, original_text, chars_to_mask):
        return min(len(original_text), chars_to_mask) if chars_to_mask > 0 else 0
