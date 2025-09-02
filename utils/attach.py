import allure
from allure_commons.types import AttachmentType
import os


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs(browser):
    try:
        # Пробуем получить логи браузера
        logs = browser.driver.get_log('browser')
        log_text = "".join(f"{entry['message']}\n" for entry in logs)
    except Exception:
        # Если не получилось — возвращаем заглушку
        log_text = "Browser logs are not available."

        # Прикрепляем логи к Allure
    import allure
    from allure_commons.types import AttachmentType
    allure.attach(log_text, name='browser_logs', attachment_type=AttachmentType.TEXT, extension='.log')

def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

def add_video(browser):
    selenoid_url = os.getenv("SELENOID_URL")
    video_url = f"https://{selenoid_url}/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')