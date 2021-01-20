import os
from typing import List

import pytest
import yaml

from calc_codes.calcular import Calc

yaml_file_path = os.path.dirname(__file__) + "/data/calcular.yaml"

with open(yaml_file_path) as f:
    data = yaml.safe_load(f)

    add_datas = data['add']['datas']
    add_myid = data['add']['myid']

    sub_datas = data['sub']['datas']
    sub_myid = data['sub']['myid']

    mul_data = data['mul']['datas']
    mul_myid = data['mul']['myid']

    div_datas = data['div']['datas']
    div_myid = data['div']['myid']


@pytest.fixture(params=add_datas, ids=add_myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的测试数据为 {data}")
    yield data
    print("结束计算")


@pytest.fixture(params=sub_datas, ids=sub_myid)
def get_sub_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的测试数据为 {data}")
    yield data
    print("结束计算")


@pytest.fixture(params=mul_data, ids=mul_myid)
def get_mul_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的测试数据为 {data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas, ids=div_myid)
def get_div_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的测试数据为 {data}")
    yield data
    print("结束计算")


@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calc
    return calc


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
