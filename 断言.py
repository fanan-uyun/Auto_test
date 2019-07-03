a = 1
assert a,"a is flase"
print(a)
#上述断言类似下面的raise
a = 0
if not a:
    raise AssertionError("a is flase")
print(a)

import unittest
# #unittest使用的方法
# class OurTest(unittest.TestCase):
#     """
#     继承编写测试的基础类
#     """
#     def setUp(self):
#         """
#         类似于类的init方法，在测试执行之初制动执行，通常用来做测试数据的准备
#         """
#     def test_add(self):
#         """
#         具体测试的方法，使用testcase编写具体测试的方法，函数名称必须以test开头
#         函数当中的内容通常是获取预期值，和运行结果值
#         然后对两个值进行断言
#         """
#     def tearDown(self):
#         """
#         类似类的del方法，用来回收测试的环境
#         """
#
# if __name__ == "__main__":
#     unittest.main()

# unittest使用的方法
class OurTest(unittest.TestCase):
    """
    继承编写测试的基础类
    """
    def setUp(self):
        """
        类似于类的init方法，在测试执行之初制动执行，通常用来做测试数据的准备
        """
        self.a = 1
        self.b = 1
        self.result = 3
    # def test_add(self):
        """
        具体测试的方法，使用testcase编写具体测试的方法，函数名称必须以test开头
        函数当中的内容通常是获取预期值，和运行结果值
        然后对两个值进行断言
        """
        run_result = self.a + self.b
        self.assertEqual(run_result,self.result,"self.a + self.b 不等于 3")
    def tearDown(self):
        """
        类似类的del方法，用来回收测试的环境
        """

# if __name__ == "__main__":
    # unittest.main()