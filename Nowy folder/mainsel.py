
from seleniumbase import Driver
import time

ud = "C:/Users/your user name/AppData/Local/Google/Chrome/User Data/"

driver = Driver(uc=False, browser="chrome", chromium_arg=[
    f"--user-data-dir={ud}", "--profile-directory=default"])
driver.get("https://pathofexile2.com/early-access")
time.sleep(5)
