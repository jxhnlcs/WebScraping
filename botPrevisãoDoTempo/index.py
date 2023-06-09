from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
# Validar a presença de qualquer elemento
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector
from  mysql.connector import Error



def webScraping():

    option = webdriver.ChromeOptions() #Cria o obejeto com a diretrizes para o browser que sera aberto
    option.add_argument("--start-maximized") # chrome maximizado DIRETRIZ 1
    option.add_argument("--lang=pt")  # Define o idioma para português DIRETRIZ 2
    # option.add_argument("--headless")   # Chrome em modo headless invisível DIRETRIZ 3
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)# Baixa o browser executável que sera manipulado
    #Cria o obejeto que ira permitir simular sequencias de ações de mouse e teclas do servidor
    action = ActionChains(driver)
    # Acessa site específico
    driver.get('https://weather.com/weather/today/l/-12.25,-38.96?par=google') 
    time.sleep(30)  
    
webScraping()