import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

APP_URL = "https://appapppy-ddz7iigzsyuuywbn5wbfne.streamlit.app/nifty_fno_pro_terminal_v7_3"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    print(f"Opening {APP_URL}")
    driver.get(APP_URL)
    time.sleep(10)

    # Agar app so raha hai to "wake up" button dhundo aur click karo
    buttons = driver.find_elements(
        By.XPATH, "//button[contains(., 'get this app back up')]"
    )
    if buttons:
        print("App so raha tha - wake up button click kar rahe hain...")
        buttons[0].click()
        time.sleep(60)  # app ko start hone ka time do
    else:
        print("App pehle se jaag raha hai.")

    # Thoda aur ruko taaki session properly register ho
    time.sleep(20)
    print("Page title:", driver.title)
    print("Done!")
finally:
    driver.quit()
