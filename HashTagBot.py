from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
from json import load
from random import choice,randrange


class HastagBot:
    
    DriverPath = None
    CookiePath = None
    
    def __init__(self) -> None:
        self.driver = Chrome(executable_path=self.DriverPath)
        self.driver.get("https://instagram.com")
    
    
    def load_cookies(self):
        with open(self.CookiePath,'r') as IO:
            for i in load(IO):
                self.driver.add_cookie(i)
            self.driver.refresh()
        print("[+] Cookies Loaded....")

    def Hastags(self,tag):
        self.driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
        Post = self.driver.find_element_by_class_name("_9AhH0")
        sleep(randrange(2,5))
        Post.click()

    def like(self):
        try:
            section = WebDriverWait(self.driver,20).until(
                exp.presence_of_element_located((By.CLASS_NAME,"ltpMr.Slqrh"))
            )
            sleep(randrange(2,5))
            section.find_element_by_tag_name("button").click()
        except:
            print("element Not FOund !! ")
    
    def comment(self):
        
        data = lambda keys: {
            "sad": choice(["i feel u",'don"t be sad','Ohh i understand']),
            "happy": choice(["Nice Look",'Your beautiful','wow nice'])
        }.get(keys)
        
        sleep(randrange(5,8))
        TextArea = lambda timeout:WebDriverWait(self.driver,timeout).until(
            exp.element_to_be_clickable((By.CLASS_NAME,"PUqUI.Ypffh"))
        )
        TextArea(10).click()
        sleep(randrange(2,5))
        TextArea(10).send_keys(data('sad')+'\n')


    def bulk(self,number):
        for _ in range(number):
            self.like()
            sleep(randrange(2,10))
            self.comment()
            sleep(randrange(5,8))
            self.driver.find_element_by_css_selector("div.Z2Inc._7c9RR > div > div > button").click()
            sleep(randrange(2,5))



if __name__ == '__main__':
    HastagBot.CookiePath = "./Cookies/ig.json"
    HastagBot.DriverPath = "./Driver/chromedriver.exe"
    hastagbot = HastagBot()
    hastagbot.load_cookies()
    hastagbot.Hastags("sadness")
    hastagbot.bulk(10)