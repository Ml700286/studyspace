import pytest
import os

if __name__ =="__main__":
    # 输出详情信息，不捕获标准输入输出，文件名称，输出报告，路径，清除上次记录（不叠加）
    pytest.main(["-vs","case_runner.py","--alluredir","./report/json-report","--clean-alluredir"])
    os.system("allure generate ./report/json-report -o ./report/allure-report --clean")
    # os.system("allure open ./report/allure-report")