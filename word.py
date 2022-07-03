from selenium import webdriver
import pyttsx3 as p
import time

class Meaning():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\selenium browser driver\chromedriver.exe')

    def word_meaning(self, word):
        self.word = word
        self.driver.get(url="https://www.oxfordlearnersdictionaries.com/")
        time.sleep(20)
        search2 = self.driver.find_element_by_xpath('//*[@id="q"]')
        search2.click()
        search2.send_keys(word)
        submit2 = self.driver.find_element_by_xpath('//*[@id="search-btn"]/input')
        submit2.click()
         
        try:
            result1 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li[1]/span[3]')
            result11 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li/span[1]')
            result12 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li[1]/span[2]')
        # result2 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/ol/li[2]/span[2]')
            readable_text1 = result1.text
            readable_text2 = result11.text
            readable_text3 = result12.text
        except:
            pass
       
        # readable_text2 = result2.text
        engine = p.init()
        engine.setProperty("rate", 140)
        engine.say("the meaning of " + word + "is that" + readable_text1 + "or" + readable_text2 + "or" + readable_text3)
        engine.runAndWait()

        from repeat import first1
        return first1()

# bot = Meaning()
# bot.word_meaning('photosynthesis')
