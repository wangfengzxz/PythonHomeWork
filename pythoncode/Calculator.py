"""
    计算器类，负责计算加减乘除
"""
class Calculator:
    def add(self, a, b):
        """
        两个参数相加
        :param a: 第一个数
        :param b: 第二个数
        :return: 返回 两数之和
        """
        return a + b

    def sub(self, a, b):
        """
        两个参数相减
        :param a: 第一个数
        :param b: 第二个数
        :return: 返回 两数之差
        """
        return a - b

    def mul(self, a, b):
        """
        两个参数相乘
        :param a: 乘数
        :param b: 被乘数
        :return: 返回 两数乘积
        """
        return a * b

    def div(self, a, b):
        """
        两个数相除
        :param a: 被除数
        :param b: 除数
        :return: 两束之除
        :throw: 如果除数为0，则抛错 ZeroDivisionError('除数不能为0！')
        """
        if b == 0:
            raise ZeroDivisionError("除数不能为0！")
        return a / b
