
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select

# #change as per requirement
# chrome_path = r"C:\Users\HP\Downloads\Automation using Python\driver_temp\chromedriver.exe"
# email = "abc@example.com"
# password  = "123456"
# url = "https://www.browserstack.com/users/sign_in?utm_source=google&utm_medium=cpc&utm_platform=paidads&utm_content=668803176719&utm_campaign=Search-Brand-APAC-Navigational&utm_campaigncode=Core+9301910&utm_term=e+browserstack"

# print("process Started")

# op = Options()
# #op.binary_location = chrome_path    #chrome binary location specified here
# op.add_argument("--start-maximized") #open Browser in maximized mode
# #op.add_argument("--no-sandbox") #bypass OS security model
# op.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
# op.add_experimental_option("excludeSwitches", ["enable-automation"])
# op.add_experimental_option('useAutomationExtension', False)
# op.headless = False # change to true if we want to hide the browser
# s = Service(chrome_path)

# with  webdriver.Chrome(service=s, options=op) as d:
#     d.get(url)
#     d.find_element(By.ID, "user_email_login").send_keys(email)
#     d.find_element(By.ID, "user_password").send_keys(password)
#     time.sleep(5)
#     # d.find_element(By.ID, "user_submit").click()
#     # time.sleep(5)  # wait
#     d.find_element(By.ID, "dev-menu-toggle").click()
#     wait = WebDriverWait(d, 10)
#     document_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Documentation']")))



# print ("Done")


# ----------------------------------

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# change as per requirement
chrome_path = r"C:\Users\HP\Downloads\Automation using Python\driver_temp\chromedriver.exe"
email = "abc@example.com"
password = "123456"
url = "https://www.browserstack.com/users/sign_in?utm_source=google&utm_medium=cpc&utm_platform=paidads&utm_content=668803176719&utm_campaign=Search-Brand-APAC-Navigational&utm_campaigncode=Core+9301910&utm_term=e+browserstack"

print("Process Started")

op = Options()
op.add_argument("--start-maximized")
op.add_argument("--disable-dev-shm-usage")
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('useAutomationExtension', False)
op.headless = False
s = Service(chrome_path)

with webdriver.Chrome(service=s, options=op) as d:
    d.get(url)
    d.find_element(By.ID, "user_email_login").send_keys(email)
    d.find_element(By.ID, "user_password").send_keys(password)
    d.find_element(By.ID, "user_submit").click()

    # Give some time for the page to load after logging in
    time.sleep(5)

    # Open the dropdown by clicking the toggle
    d.find_element(By.ID, "dev-menu-toggle").click()

    # Wait for the "Documentation" link to be clickable
    wait = WebDriverWait(d, 10)
    documentation_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Documentation")))
    documentation_link.click()

print("Done")
