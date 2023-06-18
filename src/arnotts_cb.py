import account
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace XXXXX with relevant variables

class CheckOutBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.arnotts.ie/brands/XXXXX/XXXXX") #Input Product Brand and Product ID + Quantity

    def accept_cookies(self):
        button = self.driver.find_element_by_id("accept-button-id")
        button.click()

    def login(self, email, password):
        self.driver.get("https://www.arnotts.ie/login/?originalcontent=%2Faccount%2F")
        time.sleep(5)
        email_input = self.driver.find_element_by_id("login-email-id")
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element_by_id("login-password-id")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_id("login-button-id").click()
        time.sleep(3)

    def add_product_to_cart(self, link):
        self.driver.get(link)
        time.sleep(1)
        add_to_cart_button = self.driver.find_element_by_xpath('//*[@id="Add"]/div/div[1]/div/div/button')
        add_to_cart_button.click()
        time.sleep(2)

    def checkout(self):
        self.driver.get("https://www.arnotts.ie/cart/")
        time.sleep(1)
        self.driver.find_elements_by_class_name(
            "SelectionContainer-class-1"
        )[1].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name(
            "ProceedButton-class-1"
        )[0].click()

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

        submit_button = self.driver.find_element_by_xpath('//*[@id="SubmitForm"]/div/div[2]/div/button')  
        submit_button.click()

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    checkout_bot.login(account.email, account.password)
    time.sleep(30)

    checkout_bot.add_product_to_cart(
        "https://www.arnotts.ie/
 )
    checkout_bot.checkout()
    time.sleep(20)