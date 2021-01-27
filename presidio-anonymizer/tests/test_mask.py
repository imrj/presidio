# import math
#
# import pytest
# from presidio_anonymizer.anonymizers.mask import Mask
#
#
# @pytest.mark.parametrize(
#     # fmt: off
#     "masking_character, chars_to_mask, anonymized_text",
#     [
#         ("*", 3, "***"),
#         ("3", 3, "333"),
#         ("3", math.inf, "333"),
#         ("😈", math.inf, "333"),
#         (" ", math.inf, "333"),
#         (" ", math.inf, "333"),
#     ])
#     # fmt: on
# def test_given_special_character_for_masking_then_masked_anonymized_text_returns_as_expected(masking_character, chars_to_mask, anonymized_text):
#     params = {"masking_character": masking_character, "chars_to_mask": chars_to_mask}
#
#     actual_anonymized_text = Mask().anonymize(params=params)
#
#     assert anonymized_text == actual_anonymized_text
#
#
# def test_given_masking_character_and_length_then_return_string_with_recurring_character_on_the_specific_length():
#     masking_character = "*"
#     chars_to_mask = 3
#     params = {"masking_character": masking_character, "chars_to_mask": chars_to_mask}
#
#     actual_anonymized_text = Mask().anonymize(params=params)
#
#     assert len(actual_anonymized_text) == chars_to_mask
#     assert all(character == masking_character for character in actual_anonymized_text)
