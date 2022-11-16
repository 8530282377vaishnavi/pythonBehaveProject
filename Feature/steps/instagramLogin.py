from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given(u'I launch the Browser')
def step_impl(context):
    context.serv = Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
    context.Driver = webdriver.Chrome(service=context.serv)


@when(' I Open the instagam Page')
def step_impl(context):
    context.Driver.get("https://www.instagram.com/accounts/login/")


@when(u' I Enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.Driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
    context.Driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)


@when(u'I click login Button')
def step_impl(context):
    context.Driver.find_element(By.XPATH, "//button[@type='submit']").submit()


@then(u'user must successfully login to the dash board page')
def step_impl(context):
    context.Driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M22 23h-6.')]").click()
