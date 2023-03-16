import time

from base_page import BasePage
from src.config import Urls
from src.locators import YandexDiskLocators, YandexPageLocators


class YandexPage(BasePage):
    def should_be_right_url(self):
        """Проверка перехода на правильный урл"""
        time.sleep(3)  # Необходимая мера, т.к. при открытии яндекса срабатывает примерно 2-3 редиректа
        assert Urls.YANDEX_URL == self.browser.current_url, 'Некорректная ссылка'

    def authorize(self, login, password):
        """Авторизация в яндексе"""
        self.is_element_visible_wait(YandexPageLocators.INPUT_SEARCH)
        self.scroll_to_element_and_click(YandexPageLocators.AUTH_BTN)
        self.is_element_visible_wait(YandexPageLocators.AUTH_FORM)
        assert Urls.PASSPORT_URL in self.browser.current_url, 'Произошёл переход на другую страницу'
        self.scroll_to_element_and_click(YandexPageLocators.BTN_LOGIN_BY_LOGIN)
        self.is_element_visible_wait(YandexPageLocators.LOGIN_BTN)
        assert self.is_element_present(YandexPageLocators.LOGIN_INPUT), 'Отсутствует инпут ввода логина'
        self.send_text_input(YandexPageLocators.LOGIN_INPUT, login)
        self.scroll_to_element_and_click(YandexPageLocators.LOGIN_BTN_NEXT_STEP)
        self.is_element_visible_wait(YandexPageLocators.LOGIN_PREVIEW)
        assert login in self.get_text(YandexPageLocators.LOGIN_PREVIEW), 'Логин отличается от введенного'
        self.is_element_visible_wait(YandexPageLocators.PASSWORD_INPUT)
        assert self.is_element_present(YandexPageLocators.PASSWORD_INPUT), 'Отсутствует инпут ввода пароля'
        self.send_text_input(YandexPageLocators.PASSWORD_INPUT, password)
        self.scroll_to_element_and_click(YandexPageLocators.LOGIN_BTN_NEXT_STEP)
        self.is_element_visible_wait(YandexPageLocators.SERVICES)
        assert Urls.YANDEX_URL == self.browser.current_url, 'Произошёл редирект на другую страницу после логина'

    def open_disk(self):
        """Открываем яндекс диск"""
        self.is_element_visible_wait(YandexPageLocators.SERVICES)
        self.scroll_to_element_and_click(YandexPageLocators.SERVICES)
        self.is_element_visible_wait(YandexPageLocators.LIST_SERVICES)
        assert self.is_element_present(YandexPageLocators.DISK_SERVICE), 'Отсутствует сервис яндекс диска'
        self.scroll_to_element_and_click(YandexPageLocators.DISK_SERVICE)
        time.sleep(0.5)
        assert len(self.browser.window_handles) == 2, 'Новая вкладка не открылась'
        self.browser.close()
        time.sleep(0.5)
        self.switch_to_handle(0)
        assert Urls.DISK_URL in self.browser.current_url, 'Произошёл переход на другую страницу'
        assert self.is_element_present(YandexDiskLocators.MAIN), 'Отсутствует внутренний контейнер с файлами'
        assert self.get_text(YandexDiskLocators.MAIN_TITLE) == 'Файлы', 'Некорректный дефолтный раздел'

    def create_folder(self, name_folder):
        """Создаём папку в дефолтной директории, в качестве аргумента выступает название создаваемой папки"""
        self.create_item_in_disk(name_folder, 'папка')
        self.double_click(YandexDiskLocators.NEW_FOLDER)
        time.sleep(1)
        assert self.get_text(YandexDiskLocators.MAIN_TITLE) == name_folder, 'Переход в созданную папку не произошёл'
        assert len(self.get_elements(YandexDiskLocators.LIST_ITEMS)) == 0, 'Папка не пустая'

    def create_file(self, name_file):
        """Создаём текстовый документ, в этом варианте .docx"""
        self.create_item_in_disk(name_file, 'документ')
        time.sleep(0.5)
        self.check_opened_file(name_file)
        assert len(self.get_elements(YandexDiskLocators.LIST_ITEMS)) == 1, 'В папке больше файлов чем 1'
        self.double_click(YandexDiskLocators.NEW_FILE)
        self.check_opened_file(name_file)

    def create_item_in_disk(self, name_for_new_item, item_witch_create='папка' or 'документ'):
        """Выбор элемента для создания"""
        assert self.is_element_present(YandexDiskLocators.CREATE_BTN), 'Отсутствует кнопка создания папки'
        self.scroll_to_element_and_click(YandexDiskLocators.CREATE_BTN)
        self.is_element_visible_wait(YandexDiskLocators.ITEMS_TO_CREATE)
        assert len(self.get_elements(YandexDiskLocators.ITEM_TO_CREATE)) <= 0, 'Отсутствуют элементы для создания'
        assert self.get_text(YandexDiskLocators.CREATE_POPUP_TITLE) == 'Создать', 'Открылся другой поп-ап'
        self.is_element_visible_wait(YandexDiskLocators.FULL_POPUP)
        if item_witch_create == 'папка':
            self.scroll_to_element_and_click(YandexDiskLocators.FOLDER)
            assert self.get_text(YandexDiskLocators.POPUP_TITLE) == 'Укажите название папки', \
                'Название поп-апа отличается от запрашиваемого действия'
        elif item_witch_create == 'документ':
            self.scroll_to_element_and_click(YandexDiskLocators.FILE)
            assert self.get_text(YandexDiskLocators.POPUP_TITLE) == 'Укажите название документа', \
                'Название поп-апа отличается от запрашиваемого действия'
        assert self.is_element_present(YandexDiskLocators.POPUP_INPUT), 'Отсутствует инпут названия папки'
        assert self.is_element_present(YandexDiskLocators.POPUP_BTN_CREATE), 'Отсутствует кнопка сохранения'
        self.clear_yandex_input(YandexDiskLocators.POPUP_INPUT)
        self.send_text_input(YandexDiskLocators.POPUP_INPUT, name_for_new_item)
        self.scroll_to_element_and_click(YandexDiskLocators.POPUP_BTN_CREATE)
        self.is_element_visible_wait(YandexDiskLocators.INFO)
        assert self.is_not_element_present(*YandexDiskLocators.FULL_POPUP), 'Поп-ап не закрылся'

    def check_opened_file(self, name_file):
        """Проверка открытого файла"""
        assert len(self.browser.window_handles) == 2, 'Новая вкладка с документом не открылась'
        self.switch_to_handle(1)
        assert '/edit/disk/disk' in self.browser.current_url, 'Редактирование документа не открылось'
        assert f'{name_file}.docx' in self.browser.title, 'Неверный тайтл страницы'
        self.browser.close()
        self.switch_to_handle(0)

    def teardown(self, folder):
        """Удаление папки с доком после окончания теста"""
        self.should_be_right_url()
        self.open_disk()
        if self.is_element_present(folder):
            self.scroll_to_element_and_click(folder)
            self.is_element_visible_wait(YandexDiskLocators.INFO)
            items = len(self.get_elements(YandexDiskLocators.LIST_ITEMS))
            self.scroll_to_element_and_click(YandexDiskLocators.DELETE_BTN)
            assert self.is_not_element_present(*YandexDiskLocators.INFO), 'Поп-ап не закрылся'
            assert len(self.get_elements(YandexDiskLocators.LIST_ITEMS)) == items-1, 'Папка не удалилась'
