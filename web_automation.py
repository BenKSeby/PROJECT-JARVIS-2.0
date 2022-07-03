from selenium import webdriver
import time

# class to play a music video on youtube
class Music():
    def __init__(self):
        self.name = None
        self.driver = webdriver.Chrome(executable_path=r'C:\selenium browser driver\chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

    def play(self, name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query=" + name)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]')
        video.click()
        time.sleep(300)

        from repeat import first1
        return first1()

# calling the music automation class
#bot = Music()
#bot.play("karikku")
