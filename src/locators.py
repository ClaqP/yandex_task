from selenium.webdriver.common.by import By

from src.config import Names


class YandexPageLocators:
    INPUT_SEARCH = (By.XPATH, "//input[@id='text']")
    AUTH_BTN = (By.XPATH, "//a[contains(text(),'Войти')]")
    AUTH_FORM = (By.CSS_SELECTOR, '.passp-auth-content')
    LOGIN_BTN = (By.XPATH, "//button[contains(.,'Почта')]")
    BTN_LOGIN_BY_LOGIN = (By.XPATH, "(//button[@type='button'])[1]")
    LOGIN_INPUT = (By.ID, 'passp-field-login')
    LOGIN_BTN_NEXT_STEP = (By.ID, 'passp:sign-in')
    LOGIN_PREVIEW = (By.CSS_SELECTOR, '.CurrentAccount-displayName')
    PASSWORD_INPUT = (By.ID, 'passp-field-passwd')
    SERVICES = (By.XPATH, "//a[contains(@href, 'https://yandex.ru/all')]")
    LIST_SERVICES = (By.CSS_SELECTOR, '.services-more-popup__section-content:nth-child(1)')
    DISK_SERVICE = (By.XPATH, "//div[text()='Диск']")


class YandexDiskLocators:
    MAIN = (By.CSS_SELECTOR, '.root__content-container')
    MAIN_TITLE = (By.CSS_SELECTOR, '.listing-heading__title-inner')
    CREATE_BTN = (By.CSS_SELECTOR, '.create-resource-popup-with-anchor > .Button2')
    ITEMS_TO_CREATE = (By.CSS_SELECTOR, '.create-resource-popup-with-anchor__create-items')
    ITEM_TO_CREATE = (By.CSS_SELECTOR, 'create-resource-button create-resource-popup-with-anchor__create-item')
    CREATE_POPUP_TITLE = (By.CSS_SELECTOR, '.create-resource-popup-with-anchor__title')
    FOLDER = (By.XPATH, "//button[@aria-label='Папку']")
    FILE = (By.XPATH, "//button[@aria-label='Текстовый документ']")
    LIST_ITEMS = (By.CSS_SELECTOR, '.listing-item > .listing-item__icon')
    FULL_POPUP = (By.CSS_SELECTOR, '.dialog__wrap')
    POPUP_TITLE = (By.CSS_SELECTOR, '.dialog__title')
    POPUP_INPUT = (By.CSS_SELECTOR, '.Textinput-Control:nth-child(1)')
    POPUP_BTN_CREATE = (By.CSS_SELECTOR, '.confirmation-dialog__button')
    INFO = (By.CSS_SELECTOR, '.resources-info-dropdown')
    NEW_FOLDER = (By.XPATH, f"//span[@title='{Names.FOLDER_NAME}']")
    NEW_FILE = (By.XPATH, f"//span[@title='{Names.FILE_NAME}.docx']")
    INFO_POPUP_NAME = (By.CSS_SELECTOR, '.resources-info-dropdown__name > .clamped-text')
    DELETE_BTN = (By.CSS_SELECTOR, '.groupable-buttons__visible-button_name_delete')
