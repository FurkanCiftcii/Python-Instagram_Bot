
from selenium.webdriver.common import keys
from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.profile=webdriver.FirefoxProfile()
        self.profile.set_preference('intl.accept_languages','en-GB')
        self.browser=webdriver.Firefox(firefox_profile=self.profile)
        self.username=username
        self.password=password

   #sign in Instagram with your profile     
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
   #With this method, you can create a list of followers as a txt file.
    def getFollowers(self):

        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)

        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followersCount=len(dialog.find_elements_by_css_selector("li"))
        print(f"firstCount :{followersCount}")
        actions=webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            actions.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount=len(dialog.find_elements_by_css_selector("li"))

            if followersCount !=newCount:
                followersCount=newCount
                print(f"updated count :{newCount}")
                time.sleep(1)
            else:
                break

        followers=dialog.find_elements_by_css_selector("li")
        
        followerList=[]
        for user in followers:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item+"\n")
    #bot follows the user entered with this method
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        
        followButton=self.browser.find_element_by_tag_name("button")
        if followButton.text!="Following":
            followButton.click()
            time.sleep(2)
        else:
            print("already following this profile")

    

instagrm=Instagram(username,password)
instagrm.signIn()
#instagrm.followUser("cristiano")
instagrm.getFollowers()       