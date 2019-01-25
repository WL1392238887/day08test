import allure
import pytest


class Test_01:
    @allure.step(title='这是第一个测试用例名称')
    def test_o1(self):
        print('hahhahah')

    @allure.step(title='这是第二个测试用例名称')
    def test_02(self):
        print('alllalalal')