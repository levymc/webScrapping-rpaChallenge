from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time
from formInfo import formInfo

logging.basicConfig(filename='log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class App:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 0) 

    def execute(self):
      try:
          self.handleSiteAccess()
          print("Acessou o site")
          
          for i in range(len(formInfo)):
            
            self.handleInputLoop(i)
            print("Inputou todos os dados do form")
            
            time.sleep(3)
            
            self.driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
            print("Clicou no Submit")
            
            time.sleep(2)
            
            
            

      finally:
          self.driver.quit()
          
    def handleSiteAccess(self):
      try:
        self.driver.get("https://rpachallenge.com/")
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]')))
        print("Accessed RPA Chanllenge")
      except Exception as e:
        logging.error(f"Error handleSiteAccess: {e}")
    
    def handleInputLoop(self, i):
      try:
        for field in formInfo[i]:
          self.inputComplete(field['xpath'], field['value'], field['printMsg'], field['error_msg'])
      except Exception as e:
        logging.error(f"Error handleInputLoop: {e}")
    
    def inputComplete(self, xpath, text, printMsg, error_message):
      try:
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        element.send_keys(text)
        print(printMsg)
      except Exception as e:
        print(error_message, {str(e)})
        logging.error(error_message)
      

if __name__ == "__main__":
    app = App()
    app.execute()
