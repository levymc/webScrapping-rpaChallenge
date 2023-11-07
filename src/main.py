from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time
import asyncio

logging.basicConfig(filename='log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class App:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 0) 

    def execute(self):
      try:
          self.driver.get("https://rpachallenge.com/")
          self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]')))
          print("Access RPA Chanllenge")
          
          self.inputComplete('//*[@ng-reflect-name="labelPhone"]', '16997330060', "Clicou no Phone Number", "Error to interact with PhoneNumber")
          print("Preencheu o Phone Number")
          self.inputComplete('//*[@ng-reflect-name="labelAddress"]', '98 North Road', "Clicou no Address", "Error to interact with Address")
          print("Preencheu o Address")
          self.inputComplete('//*[@ng-reflect-name="labelFirstName"]', 'Levy', "Clicou no FirstName", "Error to interact with FirstName")
          print("Preencheu o FirstName")
          self.inputComplete('//*[@ng-reflect-name="labelLastName"]', 'Cruz', "Clicou no labelLastName", "Error to interact with labelLastName")
          print("Preencheu o labelLastName")
          self.inputComplete('//*[@ng-reflect-name="labelCompanyName"]', 'LMC Factory', "Clicou no labelCompanyName", "Error to interact with labelCompanyName")
          print("Preencheu o labelCompanyName")
          self.inputComplete('//*[@ng-reflect-name="labelEmail"]', 'levymcruz@gmail.com', "Clicou no labelEmail", "Error to interact with labelEmail")
          print("Preencheu o labelEmail")
          self.inputComplete('//*[@ng-reflect-name="labelRole"]', 'Analyst', "Clicou no labelRole", "Error to interact with labelRole")
          print("Preencheu o labelRole")
          time.sleep(5)
          
      finally:
          self.driver.quit()
    
    def inputComplete(self, xpath, text, printMsg, error_message):
      try:
        phoneNumberInput = self.driver.find_element(By.XPATH, xpath)
        phoneNumberInput.click()
        phoneNumberInput.send_keys(text)
        print(printMsg)
      except Exception as e:
        print(error_message, {str(e)})
        logging.error(error_message)
      
    
    # def clickPhoneNumberInput(self):
    #   try:
    #     phoneNumberInput = self.driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]')
    #     phoneNumberInput.click()
    #     phoneNumberInput.send_keys('16997330060')
    #     print("Clicou no Phone Number")
    #   except Exception as e:
    #     error_message = f"Erro ao acessar os anúncios"
    #     print(error_message, {str(e)})
    #     logging.error(error_message)

if __name__ == "__main__":
    app = App()
    app.execute()
