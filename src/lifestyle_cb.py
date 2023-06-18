import account
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace XXXXX with relevent variables

class CheckOutBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.lifestylesports.com/ie/XXXXX") #Input Product ID and Quantity

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password):
        self.driver.get("https://www.lifestylesports.com/ie/login?original=%2Fie%2Faccount")
        time.sleep(5)
        email_input = self.driver.find_element_by_id("mms-login-form__email")
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_id("mms-login-form__password")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_id("mms-login-form__login-button").click()
        time.sleep(3)

    def add_product_to_cart(self, link):
        self.driver.get(link)
        time.sleep(1)
        add_to_cart_button = self.driver.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
        add_to_cart_button.click()
        time.sleep(2)

    def checkout(self):
        self.driver.get("https://www.lifestylesports.com/ie/cart")
        time.sleep(1)
        self.driver.find_elements_by_class_name(
            "SelectGroupstyled__SelectGroupItemContainer-sc-1iooaif-0"
        )[2].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name(
            "ContinueButton__StyledContinue-fh9abp-0"
        )[1].click()
        payment_method = Select(self.driver.find_element_by_id('XXXXX'))  
        payment_method.select_by_visible_text('XXXXX') 

        # Fill out the form
    first_name = self.driver.find_element_by_id('first-name-id')  
    first_name.send_keys('FIRSTNAME')

    last_name = self.driver.find_element_by_id('last-name-id')  
    last_name.send_keys('LASTNAME')

    address = self.driver.find_element_by_id('address-id')  
    address.send_keys('ADDRESS')

    city = self.driver.find_element_by_id('city-id')
    city.send_keys('CITY')

    state = self.driver.find_element_by_id('state-id')
    state.send_keys('STATE')

    zip_code = self.driver.find_element_by_id('zip-code-id')
    zip_code.send_keys('ZIPCODE')

    phone_number = self.driver.find_element_by_id('phone-number-id')
    phone_number.send_keys('PHONE')

    email = self.driver.find_element_by_id('email-id')  
    email.send_keys('EMAIL')

    payment_method = self.driver.find_element_by_id('payment-method-id')  
    payment_method.select_by_visible_text('PAYMENTMETHOD')  

    card_number = self.driver.find_element_by_id('card-number-id')  
    card_number.send_keys('CARDNUMBER')

    expiry_date = self.driver.find_element_by_id('expiry-date-id')  
    expiry_date.send_keys('EXPIRYDATE')

    cvv = self.driver.find_element_by_id('cvv-id')  
    cvv.send_keys('CVV')

    submit_button = self.driver.find_element_by_xpath('//*[@id="Submit"]/div/div/div[2]/div/button')  
    submit_button.click()

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    checkout_bot.login(account.email, account.password)
    time.sleep(30)

    checkout_bot.add_product_to_cart(
        "https://www.lifestylesports.com/ie/XXXXX" 
    )
    checkout_bot.checkout()
    time.sleep(20)