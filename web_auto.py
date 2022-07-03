from selenium import webdriver

import pyttsx3 as p

# class to see the information
class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\selenium browser driver\chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()

        # the defenition the bot can read
        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()
        
        from repeat import first1
        return first1()

#bot = info()
#bot.get_info("liberty bell")
