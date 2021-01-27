"""Mask some or all given text entity PII with given character."""
from presidio_anonymizer.anonymizer_parameters.mask_parameters import MaskParameters
from presidio_anonymizer.anonymizers import Anonymizer
from presidio_anonymizer.entities.invalid_exception import InvalidParamException


class Mask(Anonymizer):
    """Mask the given text with given value."""

    def anonymize(self, original_text=None, params={}):
        """
        Anonymize a given amount of text with a given character.

        :return: The given text masked as requested
        """
        mask_parameters = MaskParameters(params)
        mask_parameters.char

        return ""


def get_effective_chars_to_mask(original_text, chars_to_mask):
    return min(len(original_text), chars_to_mask) if chars_to_mask > 0 else 0
