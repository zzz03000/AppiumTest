from appium.webdriver.common.appiumby import AppiumBy
from base_page import BasePage

class HomePage(BasePage):
    # 1. 화면 내 요소 위치(Locators) 정의
    BUTTON_1_XPATH = '//android.widget.Button[@content-desc="button_1"]'

    # 2. 이 화면에서 수행할 액션 정의
    def click_button_1(self):
        self.click(AppiumBy.XPATH, self.BUTTON_1_XPATH)
        print("button_1을 클릭했습니다.")