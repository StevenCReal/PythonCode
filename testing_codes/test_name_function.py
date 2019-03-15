import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):  #这个类必须继承unittest.TestCase 类
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？ """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name,
                         'Janis Joplin')  #断言方法用来核实得到的结果是否与期望的结果一致

    def test_first_middle_last_name(self):
        """能够正确处理像Samuel M Jackson这样的姓名吗？ """
        formatted_name = get_formatted_name('samuel', 'jackson', 'm')
        self.assertEqual(formatted_name, 'Samuel M Jackson')


unittest.main()