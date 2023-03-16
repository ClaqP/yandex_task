import allure
from percy import percy_snapshot
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открытие браузера/окна"""
        self.browser.get(self.url)

    def close(self):
        """Закрытие таба/браузера"""
        self.browser.close()

    def scroll_to_element_and_click(self, locator, timeout=5):
        """Скролл к элементу и клик по нему"""
        element = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator), message=f"Не удается найти элементы по локатору {locator}")
        ActionChains(self.browser).move_to_element(element).perform()
        element.click()

    def is_element_present(self, locator, timeout=10):
        """Проверка что, элемент присутсвует на странице"""
        self.browser.implicitly_wait(timeout)
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        """Проверка что, элемент не присутствует на странице"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def screen(self, filename):
        """Скриншот текущего отображения страницы"""
        self.browser.save_screenshot(f"./screenshot/{filename}.png")
        allure.attach.file(f"./screenshot/{filename}.png", name=f'{filename}',
                           attachment_type=allure.attachment_type.PNG)
        percy_snapshot(self.browser, filename, widths=[1920], percy_css="div#scb-widgets {visibility: hidden;}")

    def send_keys(self, how, what, keys, timeout=10):
        """Отправка данных"""
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((how, what)), 'Время ожидания истекло')
        self.scroll_to_element(how, what)
        self.browser.find_element(how, what).send_keys(keys)

    def is_element_visible_wait(self, locator, timeout=15):
        """Ожидание видимости элемента"""
        try:
            WebDriverWait(self.browser, timeout, ignored_exceptions=StaleElementReferenceException).until(
                EC.visibility_of_element_located(locator), 'Время ожидания истекло')
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, how, what):
        """Скролл к элементу"""
        elem = self.browser.find_element(how, what)
        self.browser.execute_script("return arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", elem)

    def send_text_input(self, locator, text):
        """Вставка текста в инпут"""
        element = self.browser.find_element(*locator)
        ActionChains(self.browser).move_to_element(element).perform()
        element.send_keys(text)

    def switch_to_handle(self, handle):
        """Переключение между окнами"""
        self.browser.switch_to.window(self.browser.window_handles[handle])

    def clear_yandex_input(self, locator):
        """Очистка инпута через кнопки"""
        self.send_text_input(locator, Keys.CONTROL + "a")
        self.send_text_input(locator, Keys.DELETE)

    def double_click(self, locator):
        """Двойной клик"""
        element = self.browser.find_element(*locator)
        ActionChains(self.browser).double_click(element).perform()

    def get_text(self, locator):
        """Получаем текст из элемента"""
        element = self.browser.find_element(*locator)
        ActionChains(self.browser).move_to_element(element).perform()
        text = element.text
        return text

    def get_elements(self, locator):
        """Получаем список элементов"""
        elements = self.browser.find_elements(*locator)
        return elements
