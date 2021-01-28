import pytest

from presidio_anonymizer.anonymizer_parameters import MaskParameters
from presidio_anonymizer.entities import InvalidParamException


def test_given_all_params_then_validate_fpe_pass_and_no_exception_thrown():
    params = MaskParameters(
        {"masking_char": "*", "chars_to_mask": 1, "from_end": False})
    params.validate_and_normalize_fields()


@pytest.mark.parametrize(
    # fmt: off
    "request_json, result_text",
    [
        ({"masking_char": "*", "chars_to_mask": 1},
         "Invalid input, mask parameters must contain from_end"),
        ({"masking_char": "*", "from_end": False},
         "Invalid input, mask parameters must contain chars_to_mask"),
        ({"chars_to_mask": 1, "from_end": False},
         "Invalid input, mask parameters must contain masking_char"),
    ],
    # fmt: on
)
def test_given_some_params_then_validate_fpe_fail(request_json, result_text):
    with pytest.raises(InvalidParamException) as e:
        params = MaskParameters(request_json)
        params.validate_and_normalize_fields()
    assert e.value.err_msg == result_text
