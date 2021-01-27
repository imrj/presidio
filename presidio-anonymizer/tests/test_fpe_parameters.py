import pytest

from anonymizer_parameters import FPEParameters
from presidio_anonymizer.entities import InvalidParamException


def test_given_all_params_then_validate_fpe_pass_and_no_exception_thrown():
    params = FPEParameters(
        {"old_text": "bla", "decrypt": "decrypt", "tweak": "tweak", "key": "key"})
    params.validate_and_normalize_fields()


@pytest.mark.parametrize(
    # fmt: off
    "request_json, result_text",
    [
        ({"decrypt": "decrypt", "tweak": "tweak", "key": "key"},
         "Invalid input, FPE parameters must contain old_text"),
        ({"old_text": "bla", "tweak": "tweak", "key": "key"},
         "Invalid input, FPE parameters must contain decrypt"),
        ({"old_text": "bla", "decrypt": "decrypt", "key": "key"},
         "Invalid input, FPE parameters must contain tweak"),
        ({"old_text": "bla", "decrypt": "decrypt", "tweak": "tweak"},
         "Invalid input, FPE parameters must contain key"),

    ],
    # fmt: on
)
def test_given_some_params_then_validate_fpe_fail(request_json, result_text):
    with pytest.raises(InvalidParamException) as e:
        params = FPEParameters(request_json)
        params.validate_and_normalize_fields()
    assert e.value.err_msg == result_text
