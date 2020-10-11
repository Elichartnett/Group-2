from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #must pip install webdriver_manager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def sendEmail():
    driver.get("http://0.0.0.0:5000")

    userName = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    userName.send_keys("group2emailclient@gmail.com")

    password = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    password.send_keys("Group2Test")

    login = driver.find_element_by_xpath("/html/body/form/button")
    login.click()

    time.sleep(2)

    sendMail = driver.find_element_by_xpath("/html/body/div/button")
    sendMail.click()

    to = driver.find_element_by_xpath('//*[@id="sendto"]')
    to.send_keys("group2emailclient@gmail.com")

    subject = driver.find_element_by_xpath("/html/body/form/input[2]")
    subject.send_keys("Test subject")

    body = driver.find_element_by_xpath("/html/body/form/textarea")
    body.send_keys("Test body")

    send = driver.find_element_by_xpath("/html/body/form/button")
    send.click()

if __name__ == '__main__':
    for i in range(5):
        sendEmail()