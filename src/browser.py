from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest

# Удалённый запуск
# @pytest.fixture()
# def set_up_browsers():  # Функция настройки браузера
#     # Создание объекта ChromeOptions
#     options = ChromeOptions()
#     # options.add_argument("--headless") # Опционально: запускать браузер без графического интерфейса
#     options.set_capability("browserName", "chrome")
# #    options.set_capability("browserVersion", "130.0.6723.116") # skillbox_1
#     options.set_capability("browserVersion", "latest") # skillbox_2
#     options.set_capability("platformName", "windows")
#
#     # Подключение к Selenoid
#     driver = Remote(
#         command_executor="http://127.0.0.1:4444/wd/hub",
#         options=options
#     )
#     yield driver
#     driver.quit()


#Для запуска локально
@pytest.fixture()
def set_up_browsers():
    options = ChromeOptions()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "130.0.6723.116") # skillbox_1
    #options.set_capability("browserVersion", "latest") # skillbox_2
    options.set_capability("platformName", "windows")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


