# 需要导入上级路径到sys的path，否则命令行无法读取到上级路径，可以痛殴sys.path打印看到文件查询路径
# 命令行运行方式：cd testing, 然后pytest xx.py.通过 pytest test_calculator.py -vs
import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator

"""
    测试类
"""
class TestCalc:

    # 可以将初始化放到这里来，然后测试用例使用
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("../data/calculator_add.yaml")))
    def test_add(self, a, b, result):
        """
        加法测试用例
        """
        assert self.calc.add(a, b) == result
        pass

    # @pytest.mark.login
    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("../data/calculator_div.yaml")))
    def test_div(self, a, b, result):
        """
        加法测试用例，添加了异常逻辑判断，除数为0捕获异常则通过
        """
        if b == 0:
            try:
                assert self.calc.div(a, b) == result
                print("除 0 异常数据未正常异常抛出")
                raise Exception("除 0 异常数据未正常异常抛出")
            except ZeroDivisionError as e:
                print("除 0 异常数据异常抛出")
        else:
            assert self.calc.div(a, b) == result
        pass
