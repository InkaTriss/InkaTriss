from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select

email='inka@data.com'
imie='Paulina'
nazwisko='Kozak'

birthday='29'
birthmonth='4'
birthyear='1990'
password="1234haha"
adres='Marzycielska 4a'
city='Albia'
state='Iowa'
kod_pocztowy='52531'


class APRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(4)
    def testCorrectRegistration(self):
        driver=self.driver
        # odnajdz sign in
        sign_in=driver.find_element_by_class_name('login')
        # kliknij
        sign_in.click()
        # wpisz adres e-mail
        email_input=driver.find_element_by_id('email_create')
        email_input.send_keys(email)
        # kliknij przycisk "create an account"
        create_btn = driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        # 4 Wybierz tytul
        # sleep(2)
        gender=driver.find_element_by_id('id_gender2')
        gender.click()
        # 5 wpisz imie
        imie_input=driver.find_element_by_id('customer_firstname')
        imie_input.send_keys(imie)
        # 6 wpisz nazwisko
        nazwisko_input=driver.find_element_by_id('customer_lastname')
        nazwisko_input.send_keys(nazwisko)
        # 7 Sprawdz poprawanosc adresu email
        sprawdz_email = driver.find_element_by_id('email')
        email_fact = sprawdz_email.get_attribute('value')
        assert email == email_fact
        self.assertEqual(email,email_fact)
        # 8 wpisz niepoprawne haslo
        password_input=driver.find_element_by_id('passwd')
        password_input.send_keys(password)
        # 9 wpisz date urodzenia

        day_of_birth_select=Select(driver.find_element_by_id('days'))
        day_of_birth_select.select_by_value(birthday)
        month_of_birth_select=Select(driver.find_element_by_id('months'))
        month_of_birth_select.select_by_value(birthmonth)
        year_of_birth_select=Select(driver.find_element_by_id('years'))
        year_of_birth_select.select_by_value(birthyear)

        # 10 sprawdz imie
        sprawdz_imie = driver.find_element_by_id('firstname')
        imie_fact = sprawdz_imie.get_attribute('value')
        self.assertEqual(imie,imie_fact)

        # 11 sprawdz nazwisko
        sprawdz_nazwisko = driver.find_element_by_id('lastname')
        nazwisko_fact = sprawdz_nazwisko.get_attribute('value')
        self.assertEqual(nazwisko,nazwisko_fact)

        # 12 wpisz adres
        address_input=driver.find_element_by_id('address1')
        address_input.send_keys(adres)

        # 13 wpisz nazwe miasta
        city_name_input=driver.find_element_by_id('city')
        city_name_input.send_keys(city)

        # 14 wybierz stan
        state_name_select=Select(driver.find_element_by_id('id_state'))
        state_name_select.select_by_visible_text(state)

        # 15 wpisz kod pocztowy
        post_office_number_input=driver.find_element_by_id('postcode')
        post_office_number_input.send_keys(kod_pocztowy)

        # 16 wybierz kraj

        # 17 wpisz nr telefonu
        phone_number_input=driver.find_element_by_id('')


    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main(verbosity=2)
