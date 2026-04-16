from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #этой строчкой я запускаю браузер( и сам ввожу какой)
    #headless - видимость открытия браузера
    browser = p.chromium.launch(headless=True)
    #открывает новую вкладку
    page = browser.new_page()
    #говорю какую страницу нужно отрыть
    page.goto('https://www.litres.ru/')
    #прошу сделать скриншот и даю ему название
    page.screenshot(path='../screnshots/screenshot22.png')
    #закрываю браузер
    browser.close()
