from appium.webdriver.common.appiumby import AppiumBy

class BasePage: # 공통 UI 담당, Appium 드라이버를 직접 제어하는 기본 기능(클릭, 입력 등)을 제공함
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator): # 요소를 찾아서 반환
        return self.driver.find_element(*locator)

    def click(self, locator):   # 요소를 찾아서 클릭
        self.find_element(locator).click()