常用命令速查
环境安装
pip install pytest
pip install requests
pip install openpyxl
pip install pytest-html
pip install allure-pytest

运行测试
bashpytest                          # 运行当前目录所有测试
pytest test_api.py              # 运行指定文件
pytest tests/                   # 运行指定文件夹
pytest -v                       # 显示详细结果
pytest -v -s                    # 显示详细结果 + print输出

生成报告
bash# pytest-html 报告
pytest -v --html=report.html --self-contained-html

# Allure 报告
pytest tests/ -v --alluredir=reports --clean-alluredir
allure serve reports

常用组合（平时最常用这两条）
bash# 跑测试 + 看结果
pytest tests/ -v -s

# 跑测试 + 生成Allure报告
pytest tests/ -v --alluredir=reports --clean-alluredir && allure serve reports