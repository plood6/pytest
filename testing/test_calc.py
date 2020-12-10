import pytest
import yaml

from python_codes.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)

    datas_add = datas['add']
    add_datas = datas_add['datas']
    add_myid = datas_add['myid']

    datas_div = datas['div']
    div_datas = datas_div['datas']
    div_myid = datas_div['myid']


class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=add_myid
    )
    def test_add(self, a, b, expect):
        add_result = self.calc.add(a, b)
        if isinstance(add_result, float):
            add_result = round(add_result, 2)
        assert add_result == expect

    @pytest.mark.parametrize(
        "m, n, z",
        div_datas, ids=div_myid
    )
    def test_div(self, m, n, z):
        div_result = self.calc.div(m, n)
        if isinstance(div_result, float):
            div_result = round(div_result, 2)
        assert div_result == z
