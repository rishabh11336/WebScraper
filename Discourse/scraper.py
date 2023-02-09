# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# Navigate to the login page
login_url = "https://discourse.onlinedegree.iitm.ac.in/login"
driver.get(login_url)

# Input the username and password and submit the form
username = "<email>"
password = "<password>"

submit_button = driver.find_element(by=By.XPATH, value="/html/body/section/div/div[2]/div[2]/div[2]/div/div/div[2]/button")
submit_button.click()
username_input = driver.find_element(by=By.XPATH, value="/html/body/section/div/div[5]/div/div/div/div[4]/div[1]/div[1]/form/div[1]/div[1]/input")
password_input = driver.find_element(by=By.XPATH, value="/html/body/section/div/div[5]/div/div/div/div[4]/div[1]/div[1]/form/div[1]/div[2]/input")
submit_button = driver.find_element(by=By.XPATH, value="/html/body/section/div/div[5]/div/div/div/div[4]/div[1]/div[1]/div[2]/button")


username_input.send_keys(username)
password_input.send_keys(password)
submit_button.click()
time.sleep(6)
# Navigate to the page to scrape
scrape_url = "https://discourse.onlinedegree.iitm.ac.in/u?asc=true&order=likes_received&period=all"
driver.get(scrape_url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[6]/td[1]/div/div[2]/div[1]/span[1]/a")))


a=10000
for i in range(420):
    driver.execute_script("window.scrollTo(0, {});".format(a))
    time.sleep(3)
    a += 10000
    print(i)
    print("****************")


# Extract the HTML content of the page
html_content = driver.page_source

time.sleep(6)
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

time.sleep(6)

usernames = soup.find_all("span", class_="username bold")
name_margin = soup.find_all("span", class_="name margin")
numbers = soup.find_all("span", class_="number")
time_read = soup.find_all("span", class_="time-read")


L = len(usernames)

with open("file1.csv", "w", encoding="utf-8") as f:
    f.write("Username,Name,<3Received,<3Given,Topic Created,Replies Posted,Topics Viewed,Posts Read,Days Visited,Time Read")
    for i in range(L):
        f.write("{},{},{},{},{},{},{},{},{},{}".format(usernames[i].text.strip().encode("UTF-8", errors="ignore").decode("UTF-8", errors="ignore"), name_margin[i].text.strip().encode("UTF-8", errors="ignore").decode("UTF-8", errors="ignore"), numbers[(7*i)].text, numbers[(7*i)+1].text, numbers[(7*i)+2].text, numbers[(7*i)+3].text, numbers[(7*i)+4].text, numbers[(7*i)+5].text, numbers[(7*i)+6].text, time_read[i].text) + "\n")
# Extract data from soup and store it in a structured format

# Close the browser
driver.quit()
