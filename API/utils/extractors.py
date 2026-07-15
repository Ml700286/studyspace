import jsonpath


def json_extractor(case,res):
    if case["json_extract"]:
        for key, value in eval(case["json_extract"]).items():
            value = jsonpath.jsonpath(res.json(), value)[0]
            # print(value)
            all[key] = value