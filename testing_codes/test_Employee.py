import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    """针对Employee类进行测试"""

    def setUp(self):
        """创建一个雇员和一组答案以供测试"""
        self.test_employee = Employee('Steven', 'Chan', 3000)

    def test_give_default_raise(self):
        """测试能否正确增加默认的年薪"""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 8000)
    
    def test_give_custom_raise(self):
        """测试能否正确增加自定义的年薪"""
        self.test_employee.give_raise(7000)
        self.assertEqual(self.test_employee.salary, 10000)
    
    def test_give_wrong_raise(self):
        """测试当年薪增量小于零时（减薪！！）能否提示错（kan）误（yi）"""
        increase_salary = self.test_employee.give_raise(-1000)
        self.assertFalse(increase_salary)

unittest.main()