import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from main.tools.privacy_policy_generator import generate_pp_for_test
from main.logic.model import summarize
import pytest


@pytest.mark.parametrize("gen_pp", [generate_pp_for_test() for i in range(100)])
def test_model(gen_pp):
    res = summarize(gen_pp[1]).lower()
    print("Check company name: " + gen_pp[0]["company_name"].lower())
    check_list_containment(res, gen_pp[0]["company_name"].lower())
    print("Check data types")
    check_list_containment(res, gen_pp[0]["collected_data_types"].lower())
    print("Check retention period")
    check_list_containment(res, gen_pp[0]["retention_period"].lower())
    print("Check user rights")
    check_list_containment(res, gen_pp[0]["user_right"].lower())


def check_string_containment(result, _string):
    assert _string in result, _string + " was in in the result"


def check_list_containment(result, _list):
    for _l in _list:
        assert _l in result, _l + " was in in the result"
