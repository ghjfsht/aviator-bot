from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_latest_coef():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://1wxvsd.life/casino/play/spribe_aviator")

    driver.implicitly_wait(10)

    elem = driver.find_element(By.CSS_SELECTOR, 
        "body > app-root > app-game > div > div.main-container > div.w-100.h-100 > div > div.game-play > div.result-history.disabled-on-game-focused > app-stats-widget > div > div.payouts-wrapper > div > div:nth-child(9)"
    )
    coef = float(elem.text.replace("x", ""))
    driver.quit()
    return coef
