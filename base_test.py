import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities = dict
(
    platformName='Android',
    automationName='uiautomator2',                              # 안드로이드 전용 드라이버
    deviceName='emulator-5554',                                 # 에뮬레이터 이름
    app='C:/Users/gustp/Downloads/app-release.apk'              # 실제 apk 파일 경로
)

appium_server_url = 'http://localhost:4723'

class BaseTest(unittest.TestCase): # 드라이버 연결 및 종료 담당하는 클래스
    def setUp(self) -> None: # return 하는 값이 없다.
        # 테스트 전 세션 연결
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        # 테스트 후 세션 종료
        if self.driver:
            self.driver.quit()