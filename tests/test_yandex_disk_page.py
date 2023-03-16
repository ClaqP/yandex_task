from pages.yandex_disk_page import YandexPage
from src.config import Urls, Data, Names


def test_yandex_page(browser, teardown_docs):
    yandex_page = YandexPage(browser, Urls.YANDEX_URL)
    yandex_page.open()
    yandex_page.should_be_right_url()
    yandex_page.authorize(Data.MAIL, Data.PASSWORD)
    yandex_page.open_disk()
    yandex_page.create_folder(Names.FOLDER_NAME)
    yandex_page.create_file(Names.FILE_NAME)




