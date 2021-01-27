import pytest

from anonymizer_parameters import HashParameters
from presidio_anonymizer.entities import InvalidParamException


def test_given_all_params_then_validate_fpe_pass_and_no_exception_thrown():
    params = HashParameters({"old_text": "bla"})
    params.validate_and_normalize_fields()


@pytest.mark.parametrize(
    # fmt: off
    "request_json, result_text",
    [
        ({"bla": "bla"},
         "Invalid input, hash parameters must contain old_text"),

    ],
    # fmt: on
)
def test_given_some_params_then_validate_fpe_fail(request_json, result_text):
    with pytest.raises(InvalidParamException) as e:
        params = HashParameters(request_json)
        params.validate_and_normalize_fields()
    assert e.value.err_msg == result_text
