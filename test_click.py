import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# 1. Capability 설정 (이미지 정보 기반)
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',                              # 안드로이드 전용 드라이버
    deviceName='emulator-5554',                                 # 에뮬레이터 이름
    app='C:/Users/gustp/Downloads/app-release.apk'              # 실제 apk 파일 경로
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None: # return 하는 값이 없다.
        # 테스트 전 세션 연결
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        # 테스트 후 세션 종료
        if self.driver:
            self.driver.quit()

    def test_click_button_1(self) -> None:
        # 2. Inspector에서 가져온 XPath로 button_1 요소 찾기
        # image_2.png의 App Source 정보를 바탕으로 작성된 XPath입니다.
        xpath_value = '//android.widget.Button[@content-desc="button_1"]'
        button_1 = self.driver.find_element(by=AppiumBy.XPATH, value=xpath_value)

        # 3. 요소 클릭 동작 수행
        button_1.click()
        print("button_1을 클릭했습니다.")

if __name__ == '__main__':
    unittest.main()