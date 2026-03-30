# API自动化测试项目

基于 Python + Pytest + Requests 的接口自动化测试框架

## 技术栈
- Python 3.14
- Pytest
- Requests
- Allure 测试报告
- Excel 数据驱动

## 项目结构
├── tests/          # 测试用例
├── test_data/      # 测试数据
├── conftest.py     # 公共配置
└── reports/        # 测试报告

## 运行方式
pytest tests/ -v --alluredir=reports --clean-alluredir
allure serve reports