from behave import *
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
    context.Driver=webdriver.Chrome(service=context.serv_obj)

@when('Open orange HRM homepage')
def OpenHomepage(context):
      context.Driver.get("https://opensource-demo.orangehrmlive.com/")



@Then('verify that the logo present on home page')
def verifylogo(context):
    status=context.Driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
    assert status is True
print("vaishnavi")


@Then('close Browser')
def closeBrowser(context):
    context.Driver.close()



launchBrowser()
verifylogo()
closeBrowser()
print("vaishnavi")
print("ajinkya")
"my name is vaishnavi"