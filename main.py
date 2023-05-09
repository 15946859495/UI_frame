import os
import pytest
from core.until.sendfeishu import sendFeiShu
from core.until.settings import settings
from core.until.Get_ip import get_ip
from core.until.Makedir import mkdir


if __name__ == "__main__":
    os.environ["NO_COLOR"] = "1"  # 环境 变量声明 不需要颜色
    pytest.main()  # 不要传递参数
    files_name, report_path = mkdir()

    if settings["allure_gen"]:
        os.system(f"allure generate ./temp/allure_results -o {files_name} --clean")  # 生成报告
        sendFeiShu(get_ip(), report_path)
    if settings["allure_show"]:
        os.system(f"allure open -p 666  {files_name}")
