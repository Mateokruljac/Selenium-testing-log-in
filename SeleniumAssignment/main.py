from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

option = Options()
option.add_argument("start-maximized")

driver = Chrome(executable_path= "SELENIUM/chromedriver.exe", options = option)
driver.get("https://www.google.com")
sleep(3)

accept_all = driver.find_elements(By.TAG_NAME,"button")
for i in range(len(accept_all)):
    result = accept_all[i]
    if "Prihvati" in result.text:
        result.click()
        sleep(2)

search = driver.find_elements(By.CLASS_NAME,"RNNXgb")
for i in range(len(search)):
    result = search[i].find_element(By.TAG_NAME,"input")
    if result:
        result.send_keys("facebook")
        result.send_keys(Keys.ENTER)
        sleep(3)

all_h3_elements = driver.find_elements(By.TAG_NAME,"h3")
for i in range(len(all_h3_elements)):
    result = all_h3_elements[i]
    if "prijava" in result.text:
        result.click()
        sleep(3)
        all_buttons = driver.find_element(By.CLASS_NAME,"_4t2a")
        all_buttons = all_buttons.find_elements(By.TAG_NAME,"button")
        for i in range(len(all_buttons)):
            if "osnovne i neobavezne" in all_buttons[i].text:
                all_buttons[i].click()
                sleep(1)     
                
        email = driver.find_element(By.ID,"email")
        email.send_keys("2323123gsdgdsgdwg11g1qgegeg1efwfe@gm3232ail.com")
        password = driver.find_element(By.ID,"pass")
        password.send_keys("maqtwweo12345668970987654")
        password.send_keys(Keys.ENTER)
        sleep(2)
        
error_message = driver.find_element(By.CLASS_NAME,"_9ay5")
assert error_message.text == "Adresa e-pošte koju ste unijeli nije povezana s korisničkim računom." 
    