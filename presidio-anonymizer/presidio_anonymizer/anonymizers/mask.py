"""Mask some or all given text entity PII with given character."""
from presidio_anonymizer.anonymizers import Anonymizer
from presidio_anonymizer.anonymizers.validators import validate_parameter
from presidio_anonymizer.entities import InvalidParamException


class Mask(Anonymizer):
    """Mask the given text with given value."""

    CHARS_TO_MASK = "chars_to_mask"
    FROM_END = "from_end"
    MASKING_CHAR = "masking_char"

    def anonymize(self, text: str = None, params: dict = None) -> str:
        """
        Mask a given amount of text with a given character.

        :param text: the text to be masked
        :param params:
            masking_char: The character to be masked with
            chars_to_mask: The amount of characters to mask
            from_end: Whether to mask the text from it's end
        :return: the masked text
        """
        effective_chars_to_mask = self._get_effective_chars_to_mask(
            text, params.get(self.CHARS_TO_MASK)
        )
        from_end = params.get(self.FROM_END)
        masking_char = params.get(self.MASKING_CHAR)
        return self._get_anonymized_text(
            text, effective_chars_to_mask, from_end, masking_char
        )

    def validate(self, params: dict = None) -> None:
        """
        Validate the parameters for mask.

        :param params:
            masking_char: The character to be masked with
            chars_to_mask: The amount of characters to mask
            from_end: Whether to mask the text from it's end
        """
        masking_char = params.get(self.MASKING_CHAR)
        validate_parameter(masking_char, self.MASKING_CHAR, str)
        if len(masking_char) > 1:
            raise InvalidParamException(
                f"Invalid input, {self.MASKING_CHAR} must be a character"
            )

        validate_parameter(params.get(self.CHARS_TO_MASK), self.CHARS_TO_MASK, int)
        validate_parameter(params.get(self.FROM_END), self.FROM_END, bool)

    def anonymizer_name(self) -> str:
        """Return anonymizer name."""
        return "mask"

    @staticmethod
    def _get_effective_chars_to_mask(text, chars_to_mask):
        return min(len(text), chars_to_mask) if chars_to_mask > 0 else 0

    @staticmethod
    def _get_anonymized_text(text, chars_to_mask, from_end, masking_char):
        if not from_end:
            return masking_char * chars_to_mask + text[chars_to_mask:]
        else:
            mask_from_index = len(text) - chars_to_mask
            return text[:mask_from_index] + masking_char * chars_to_mask
