import jsonpath
import pymysql
import requests

def http_assert(case,res):
    if case["check"]:
        assert jsonpath.jsonpath(res.json(), case["check"])[0] == case["expected"]
    else:
        assert case["expected"] in res.text

def sql_assert(case):
    if case["check"] and case["sql_expected"]:
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            database="studyspace",
            user="root",
            password="root630",
            charset="utf8"
        )
        cur = conn.cursor()
        cur.execute(case["sql_check"])
        result = cur.fetchone()
        cur.close()
        conn.close()
        assert result[0] == case["sql_expected"]
