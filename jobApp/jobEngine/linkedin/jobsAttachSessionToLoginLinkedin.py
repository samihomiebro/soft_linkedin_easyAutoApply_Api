
from .linkedinSeleniumBase import LinkedinSeleniumBase
import json
from urllib.parse import urlparse

'''
    attach a driver session to a previous created session from a file
'''
class jobSearchSessionAttachLinkedin:
    def __init__(self, linkedin_data, headless=False, detached= False):
        self.linked_data = linkedin_data
        self.headless = headless
        self.detached = detached
        self.loginSession = None
        self.loginSessionId = None
        self.loginCmdExecutorUrl = None
        self.searchSession = None
        self.searchSessionId = None
        self.searchCmdExecutorUrl = None
        self.server_port= None

    def createJobSearchSession(self, attachToLoginSessionFromFile=True, SessionFile="jobApp/secrets/session.json"):
     """ create a session only for job search and attach to the login session"""
     if attachToLoginSessionFromFile:
         print("attach session using json file session data")
         with open(SessionFile, "r") as f:
             data = json.load(f)
         self.server_port = self.getPortFromUrl( data["session"]["cmdExecutor"])
         temp = data["session"]["id"]
         print(f"json session id {temp}")
         print(f"json server port : {self.server_port}")
         # Create a new Chrome driver and attach it to the existing session
         self.searchSession = LinkedinSeleniumBase(self.linked_data, self.headless)
         self.searchSession.close_session()
         self.searchSession.driver.session_id  = data["session"]["id"]
         self.searchSession.driver.command_executor._url  = data["session"]["cmdExecutor"]
         # Open a new window and switch to it
         self.searchSession.driver.execute_script("window.open('','_blank');")
         self.searchSession.driver.switch_to.window(self.searchSession.driver.window_handles[0])
     return self.searchSession
    
    def getPortFromUrl(self, url)-> int : 
        print(f"parsing url {url} for port ")
        return urlparse(url).port
