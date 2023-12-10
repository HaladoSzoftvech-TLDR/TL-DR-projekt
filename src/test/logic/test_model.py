from src.main.tools.privacy_policy_generator import generate_pp_for_test
from src.main.logic.model import summarize


def test_model():
    for i in range(0, 100):
        gen_pp = generate_pp_for_test()
        res = summarize(gen_pp[1])
        print("Check company name")
        check_string_containment(res, gen_pp[0]["company_name"])
        print("Check data types")
        check_string_containment(res, gen_pp[0]["data_types"])
        print("Check retention period")
        check_string_containment(res, gen_pp[0]["retention_period"])
        print("Check user rights")
        check_string_containment(res, gen_pp[0]["user_right"])


def check_string_containment(result, _string):
    assert _string in result


def check_list_containment(result, _list):
    for _l in _list:
        assert _l in result
