import time

import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import pytest
import pyautogui





@given(u'I am on the Demo Login Page')
def demopage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'I fill the account information for account StandardUser into the Username field and the Password field')
def credentails(context):
    context.driver.get("https://www.saucedemo.com/v1/")
    time.sleep(4)



    context.driver.find_element(By.NAME,"user-name").send_keys("standard_user");
    context.driver.find_element(By.NAME,"password").send_keys("secret_sauce");

    screenshot = pyautogui.screenshot()
    screenshot.save('C:\\Users\\mages\\PycharmProjects\\pythonProject\\report\\valid_Username_valid_Password.png')

@when(u'I click the Login Button')
def loginButton(context):
    time.sleep(4)

    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(4)

@then(u'I am redirected to the Demo Main Page')
def redirectMainPage(context):
    assert "/inventory.html" in context.driver.current_url

@then(u'I verify the App Logo exists')
def logoExist(context):
    time.sleep(4)

    app_logo=context.driver.find_element(By.XPATH,"//div[@class='app_logo']")


    if app_logo.is_displayed:
        print("User verifies App Logo")
    else:
        print("User Unable to see App Logo")
    assert app_logo.is_displayed()
    screenshot = pyautogui.screenshot()
    screenshot.save('C:\\Users\\mages\\PycharmProjects\\pythonProject\\report\\Successful Login.png')

@when(u'I fill the account information for account LockedOutUser into the Username field and the Password field')
def invalidCredentials(context):
    time.sleep(4)
    context.driver.get('https://www.saucedemo.com/v1')

    context.driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    #desktop_web_driver.find_element(By.CSS_SELECTOR, '.btn_action').click()
    screenshot = pyautogui.screenshot()
    screenshot.save('C:\\Users\\mages\\PycharmProjects\\pythonProject\\report\\invalidUserName_invalidPassword.png')


@then(u'I verify the Error Message contains the text "Sorry, this user has been banned"')
def errorMessage(context):
    time.sleep(4)

    assert context.driver.find_element(By.CSS_SELECTOR, '.error-button').is_displayed()
    screenshot = pyautogui.screenshot()
    screenshot.save('C:\\Users\\mages\\PycharmProjects\\pythonProject\\report\\error_message_shown.png')


@given(u'I am on the inventory page')
def the_inventory_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/v1/")
    context.driver.maximize_window()


    time.sleep(4)
    context.driver.find_element(By.NAME, "user-name").send_keys("standard_user");
    context.driver.find_element(By.NAME, "password").send_keys("secret_sauce");
    context.driver.find_element(By.ID, "login-button").click()

    screenshot = pyautogui.screenshot()
    screenshot.save('C:\\Users\\mages\\PycharmProjects\\pythonProject\\report\\inventoryPage.png')


@when(u'user sorts products from low price to high price')
def products_from_low_price_to_high_price(context):
    sort = "Price (low to high)"
    context.driver.implicitly_wait(10)
    dropdown_element = context.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text(sort)


@when(u'user adds lowest priced product')
def adds_lowest_priced_product(context):
    time.sleep(4)

    product_prices = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
    lowest_price = float("inf")
    lowest_price_add_to_cart_button = None

    for price_element in product_prices:
        price_text = price_element.text
        price = float(price_text.replace("$", ""))
        if price < lowest_price:
            lowest_price = price
            time.sleep(2)
            lowest_price_add_to_cart_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='ADD TO CART'])[1]")) )
    lowest_price_add_to_cart_button.click()
    time.sleep(2)


@when(u'user clicks on cart')
def clicks_on_cart(context):
    context.driver.find_element(By.XPATH,"//div[@id='shopping_cart_container']").click()
    time.sleep(2)

    print("k")


@when(u'user clicks on checkout')
def clicks_on_checkout(context):
    context.driver.find_element(By.XPATH, "//a[text()='CHECKOUT']").click()
    time.sleep(2)


@when(u'user enters first name John')
def enters_first_name_john(context):
    context.driver.find_element(By.ID, "first-name").send_keys("John");
    time.sleep(2)



@when(u'user enters last name Doe')
def enters_last_name_doe(context):
    context.driver.find_element(By.ID, "last-name").send_keys("Doe");
    time.sleep(2)



@when(u'user enters zip code 123')
def enters_zip_code(context):
    context.driver.find_element(By.ID, "postal-code").send_keys("123");
    time.sleep(2)



@when(u'user clicks Continue button')
def clicks_continue_button(context):
    context.driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(2)



@then(u'I verify in Checkout overview page if the total amount for the added item is $8.63')
def total_amount_for_the_added_item_is(context):
    expected_total_amount = "Total: $8.63"

    actual_total_amount_element = context.driver.find_element(By.XPATH, "//div[text()='8.63']")
    actual_total_amount = actual_total_amount_element.text
    time.sleep(2)

    print(actual_total_amount)
    if actual_total_amount == expected_total_amount:
        print("User verifies the total amount for the added item is $8.63")
    else:
        print("User unable to verify the total amount for the added item is $8.63")

    unittest.TestCase().assertEqual(actual_total_amount, expected_total_amount)
    time.sleep(2)



@when(u'user clicks Finish button')
def clicks_finish_button(context):
    context.driver.find_element(By.XPATH,"//a[text()='FINISH']").click()
    time.sleep(2)

    print("k")


@then(u'Thank You header is shown in Checkout Complete page')
def shown_in_checkout_complete_page(context):

    thankYou =context.driver.find_element(By.XPATH,"//div[@class='app_logo']")


    if thankYou.is_displayed():
      print("Thank you Header is Displayed")
      screenshot = pyautogui.screenshot()
      screenshot.save('C:\\Users\\mages\\PycharmProjects\\pythonProject\\report\\Thank You header is shown in Checkout Complete page.png')




