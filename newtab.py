import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class LTAutomate(unittest.TestCase):
    """
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be genarated from automation dashboard or profile section

    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based 
    """
    
#     curl --location --request POST 'https://manual-api.lambdatest.com/app/upload/realDevice' \
# --header 'Authorization: Basic <add_your_basic_auth_from_stage_username_accessKey>' \
# --form 'name="lambda1"' \
# --form 'appFile=@"/path/to/file"'
    
    def setUp(self):
        """
        Setup remote driver
        Params
        ----------
        platfrom : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
        browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
        version :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

        Result
        -------
        """
        # username: Username can be found at automation dashboard
        username="gauravkb@getfareye.com"  
        # accessToken:  AccessToken can be genarated from automation dashboard or profile section
        accessToken="DqLVVOF1ll4TTMyXXt3gslp8NZ8Ynon3vwcRd4eFTV5GLavGh9"
        # gridUrl: gridUrl can be found at automation dashboard
        gridUrl = "hub.lambdatest.com/wd/hub"
        
        desired_cap = {
            "platform" : "MacOS Catalina", 
            "browserName" : "Safari",
            "version" :  "13",
            # 'deviceName': "iPhone 12",
            # Resolution of machine
            "resolution": "1280x960", 
            "name": "LambdaTest python google search test ",
            "build": "LambdaTest python google search build",
            "network": True,
            "video": True,
            "visual": True,
            "console": True,
        }

        # URL: https://{username}:{accessToken}@beta-hub.lambdatest.com/wd/hub
        url = "https://gauravkb:DqLVVOF1ll4TTMyXXt3gslp8NZ8Ynon3vwcRd4eFTV5GLavGh9@hub.lambdatest.com/wd/hub"
        
        
        print("Initiating remote driver on platfrom: "+desired_cap["platform"]+" browser: "+desired_cap["browserName"]+" version: "+desired_cap["version"])
        self.driver = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor= url
        )

    
    def test_search_in_google(self):
        """
        Setup remote driver
        Params
        ----------
        Execute test:  navigate google.com search LambdaTest
        Result
        -------
        print title
        """
        driver = self.driver
        print("Driver initiated sucessfully.  Navigate url")
        driver.get("https://www.tutorialspoint.com/index.htm")
        # driver.find_element_by_xpath("#capabilityApp > header > div > nav > button > span").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/div[2]/a/img").click()
        # driver.find_elements_by_class_name("dz_xjzja _2minRfAM ncss-btn-primary-dark").click()
        #prints parent window title
        # print("Parent window title: " + driver.title)
        # #get current window handle
        p = driver.current_window_handle

        #get first child window
        chwd = driver.window_handles

        for w in chwd:
        #switch focus to child window
            if(w!=p):
                driver.switch_to.window(w)
            break
            time.sleep(5)
            print("Child window title: " + driver.title)
            driver.quit()

        # print("Searching lambdatest on google.com ")
        # time.sleep(8)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("lambdatest.com")
        # elem.submit()

        # print("Printing title of current page :"+driver.title)
        # driver.execute_script("lambda-status=passed")
        # print("Requesting to mark test : pass")


        time.sleep(5)


    
    def tearDown(self):
        """
        Quit selenium driver
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
