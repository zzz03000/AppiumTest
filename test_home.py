import unittest
from base_test import BaseTest
from home_page import HomePage

class TestHome(BaseTest):
    def test_click_button_1(self) -> None:
        # HomePage 객체 생성 (BaseTest의 self.driver 전달)
        home_page = HomePage(self.driver)
        
        # 버튼 1 클릭 동작 수행
        home_page.click_button_1()

if __name__ == '__main__':
    unittest.main()