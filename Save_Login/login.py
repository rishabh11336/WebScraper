from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Admin\\Desktop\\UserData") #Directory of folder where login data will save
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://www.doamainame.com/")
