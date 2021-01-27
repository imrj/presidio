import logging

from presidio_anonymizer.entities import InvalidParamException


class MaskParameters:

    logger = logging.getLogger("presidio-anonymizer")

    def __init__(self, params: dict):
        masking_char = params.get("masking_char")
        chars_to_mask = params.get("chars_to_mask")
        from_end = params.get("from_end")

    def _validate_fields(self, params):
        for field in ("start", "end", "score", "entity_type"):
            if content.get(field) is None:
                self.logger.debug(f"invalid input, no field {field} for {content}")
                raise InvalidParamException(
                    f"Invalid input, analyzer result must contain {field}"
                )

    def get_effective_chars_to_mask(original_text, chars_to_mask):
        return min(len(original_text), chars_to_mask) if chars_to_mask > 0 else 0
