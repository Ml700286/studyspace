import allure
import jsonpath
import pymysql
import pytest
import requests

from utils.analyse_case import analyse_case
from utils.excel_utils import read_excel
from jinja2 import Template

from utils.case_assert import http_assert,sql_assert
from utils.extractors import json_extractor


class Testrunner:
    # 读取用例
    data = read_excel("data/接口自动化测试用例.xlsx")

    # 全局属性
    all={}

    # 参数化
    @pytest.mark.parametrize("case",data)
    def test_case(self,case):
        all=self.all

        # 渲染case
        case=eval(Template(str(case)).render(all))

        allure.dynamic.feature(case["feature"])
        allure.dynamic.title(case["id"]+"---"+case["title"])

        # 1.解析请求数据
        request_data=analyse_case(case)

        # 2.发送请求，得到响应结果
        res=requests.request(**request_data)
        # print("\n1111111111111111",res.json())

        # 3.处理断言（提取）
        #  http断言
        http_assert(case,res)
        sql_assert(case)

        # sql断言

        # 4.提取
        # json
        json_extractor(case,res)

        # sql提取
        if case["sql_extract"]:
            for key, value in eval(case["sql_extract"]).items():
                value = result[0]
                # print(value)
                all[key] = value


