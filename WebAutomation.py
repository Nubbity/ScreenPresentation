"""Kiitos ja anteeks kaikille
    En tiiä yhtää miks mä ryhdyin tätä mutta helvetisti aamuja jos joudut muokkaaman tätä
    En jaksanu kommentoijja mihinkää käytä vaikka chatGPT sil mäki tein puolet(melkee)"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import datetime


SCROLL_SPEED= 10 #Sopiva on noin 0.1
STANDING_TIME = 5 #Olisko esimerkiksi 30s?
FOLDER_PATH = "C:/Users/hynni/Downloads/"
SHUTDOWN_TIME = 20

class Driver:
    def __init__(self) -> None:

        self.driver = self.openDriver()
        self.presentationCycle()
        self.driver.quit()
        return
    def presentationCycle(self):
        set_time = datetime.time(hour = SHUTDOWN_TIME)
        exceptionCounter  = 0
        while datetime.datetime.now().time() < set_time:
            try:
                self.estiemDriver()
                self.foodDriver()
                self.contentDriver()
                exceptionCounter = 0
                if not self.driver.current_url:
                    raise Exception
            except Exception:
                if exceptionCounter > 3:
                    ##os.system("reboot") ##Only on linux
                    exit()
                exceptionCounter+=1
                pass
        return
    def openDriver(self):
        options = Options()
        options.add_argument("--start-fullscreen")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        driver = webdriver.Chrome(options=options)
        
        return driver 
    def estiemDriver(self):
        self.driver.get("https://estiem.org/events")
        self.initEstiem()
        self.scrollPageBottom()
        self.driver.get("https://estiem.org")
        self.initEstiem()
        self.driver.execute_script("document.body.style.zoom='140%'")
        self.scrollElement()
        time.sleep(STANDING_TIME)
    def foodDriver(self):
    
        self.driver.get("https://skinfo.dy.fi/")
        time.sleep(STANDING_TIME)
        return
    def contentDriver(self):
        
        files = os.listdir(FOLDER_PATH)
        allowed_extensions = [".mp4", ".avi", ".mov", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".jpg"]
        media_files = [f for f in files if os.path.splitext(f)[1].lower() in allowed_extensions]
        print(media_files)
        for file in media_files:
            file_path = os.path.join(FOLDER_PATH, file)
            self.driver.get("file:///" + file_path)
            time.sleep(STANDING_TIME)
        return
    def scrollPageBottom(self):
        bottom=False
        a=0
        while not bottom:
            height = self.driver.execute_script("return document.documentElement.scrollHeight")
            self.driver.execute_script(f"window.scrollTo(0, {a});")
            if a > height:
                bottom=True
            a+=SCROLL_SPEED

        print("Sivu käyty läpi")    
        return
    def scrollElement(self):
        element = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    def removeElement(self, elementName):
        element = self.driver.find_element(By.XPATH, elementName)
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
    def initEstiem(self):
        elementList = ("/html/body/div[1]/div[1]/div[1]", "/html/body/div[1]/div[3]")
        for i in elementList:
            self.removeElement(i)




apina = Driver()