from selenium import webdriver
import pytest

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    extends the pytest plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.png(screen))
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
        # driver.get('file:///C:/Users/morris.lin/Desktop/pythonProject/cy/tests/reports/Report.html')


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
    driver.close()


def createBrowser():
    global driver
    driver = webdriver.Chrome(executable_path='../chromedriver')
    return driver


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    return createBrowser
# 只是返回參數 在利用這個參數去執行
