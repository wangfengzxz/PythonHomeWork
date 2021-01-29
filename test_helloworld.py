# 自己的测试类
# 常见的执行命令行参数
# 1、pytest --collect-only ，
# 只收集用例， 输出如下
# collected 2 items
#
# <Module test_calc.py>
#   <Function test_add>
# <Module test_calculator.py>
#   <Class TestCalc>
#       <Function test_add>

# 2、pytest -k 'aaa' 正则匹配
# pytest test_calculator.py -k 'test_add', 只执行了py文件下的指定的匹配的测试用例

# 3、pytest -m mark 标记名 标记, 例如 ： pytest -m search -vs,  如果有warnings，则看pytest.ini文件

# 4、pytest --junitxml=./result.xml  生成执行结果

# 5、pytest --setup-show   回溯fixture的执行过程

# 更多 pytest --help 查看帮助文档

# pytest的测试框架
# 类似的setup,teardown同样更灵活
# 模块级（setup_module/teardown_module）模块始末，全局的（优先最高）
# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
# 类级（setup_class/teardown_class）只在类中前后运行一次（在类中）
# 方法级（setup_method/teardown_method）开始于方法末（在类中）
# 类里面的（setup/teardown）运行在调用方法的前后