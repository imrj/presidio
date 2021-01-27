import logging

from presidio_anonymizer.entities import InvalidParamException

logger = logging.getLogger("presidio-anonymizer")


class Validators:

    @staticmethod
    def validate_exists(required_params: tuple, params: dict, anonymizer_type: str):
        for field_name in required_params:
            field_val = params.get(field_name)
            if field_val is None:
                logger.debug(
                    f"invalid input, no field_val {field_name} for {anonymizer_type}")
                raise InvalidParamException(
                    f"Invalid input, {anonymizer_type} parameters must contain {field_name}"
                )
