from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import time
import asyncio

logging.basicConfig(filename='log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
class App:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    async def execute(self):
        try:
            self.driver.get("https://www.imobiliariafigueira.com.br/")
            print("Acessou o site da imobiliaria")
            await self.accessAnnouncee()
            
        finally:
            self.driver.quit()
    
    async def accessAnnouncee(self):
      try:
        await self.driver.find_element(By.XPATH, '//*[@id="showcase_c9-10[0]_1699358865694_panel_0"]/a[1]').click()
        print("Clicou no anuncio")
        # time.sleep(5)
      except Exception as e:
        error_message = f"Erro ao acessar os anúncios"
        print(error_message, {str(e)})
        logging.error(error_message)

if __name__ == "__main__":
    app = App()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.execute())
    loop.close()
