#!/usr/bin/python3
from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name='Paulina'
surname='Kozak'
valid_phone_number='697909233'
adres1="kozanioagmail.pl"
password= "1887gTy3"
valid_country="Polska"


class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://wizzair.com/pl-pl#/')
        #self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def testCorrectRegistration(self):
        driver=self.driver

        # odnajdz button sign in
        sign_in=WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH,'//button[@data-test="navigation-menu-signin"]')))
        sign_in.click()

        rejestracja=WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[text()= " Rejestracja "]')))
        rejestracja.click()

        imie = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, 'firstName')))
        imie.send_keys(name)

        nazwisko = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, 'lastName')))
        nazwisko.send_keys(surname)

        f = driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()

        nr_kraju = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        # WebDriverWait
        sleep(4)
        polska = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-test="PL"]')))

        polska.click()


        nr_telefonu=driver.find_element_by_name('phoneNumberValidDigits').send_keys(valid_phone_number)

        email_input=driver.find_element_by_name('email')
        email_input.send_keys(adres1)

        password_input=driver.find_element_by_name('password')
        password_input.send_keys(password)

        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj kraje
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name("label")
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            option=label.find_element_by_tag_name('strong')
            if option.get_attribute("innerText") == valid_country:

                option.location_once_scrolled_into_view

                option.click()
                break

        akceptacja=driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        akceptacja.click()

        zarejestruj=driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestruj.click()

        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        # Zapisuję widoczne błędy do listy visible_error_notices
        visible_error_notices = []
        for error in error_notices:
            # Jesli jest widoczny, to dodaj do listy
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        assert len(visible_error_notices) == 1
        # Sprawdzam treść widocznego błędu
        error_text = visible_error_notices[0].get_attribute("innerText")
        assert error_text == "Nieprawidłowy adres e-mail"


if __name__=='__main__':
    unittest.main(verbosity=2)
