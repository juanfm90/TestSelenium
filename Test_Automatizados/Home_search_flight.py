
import unittest
import time
from DEPENDENCIAS import *
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC


class Home_search_flight():
    def cookies(driver):
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH,"//*[@id='onetrust-accept-btn-handler']")))
        cookies = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        cookies.click()
        time.sleep(0.5)

    def login(driver):
        open_login = driver.find_element(By.XPATH, '//*[@id="publicUser"]/a[2]/span')
        open_login.click()

        iframe = driver.find_element(By.CLASS_NAME, 'inte_loginIframe')
        driver.switch_to.frame(iframe)

        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="loginPage:theForm:loginEmailInput"]')))
        user = driver.find_element(By.XPATH, '//*[@id="loginPage:theForm:loginEmailInput"]')
        user.send_keys('7600919')
        print('Usuario FF Platino: 7600919')

        pasword = driver.find_element(By.XPATH, '//*[@id="loginPage:theForm:loginPasswordInput"]')
        pasword.send_keys('Password1')

        submit = driver.find_element(By.XPATH, '//*[@id="loginPage:theForm:loginSubmit"]')
        submit.click()
        driver.switch_to.parent_frame()

        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="loggedUserName"]'), 'Pankaj Tailor'))
        time.sleep(3)

    def login_PREB(driver):
        open_login = driver.find_element(By.XPATH, '//*[@id="publicUser"]/a[2]/span')
        open_login.click()
        time.sleep(5)

        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginPage:theForm:loginEmailInput"]')))

        user = driver.find_element(By.XPATH, '//*[@id="loginPage:theForm:loginEmailInput"]')
        user.send_keys('7600919')
        print('Usuario FF Platino: 7600919')

        pasword = driver.find_element(By.XPATH, '//*[@id="loginPage:theForm:loginPasswordInput"]')
        pasword.send_keys('Password1')

        submit = driver.find_element(By.XPATH, '//*[@id="loginPage:theForm:loginSubmit"]')
        submit.click()
        driver.switch_to.parent_frame()

        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="loggedUserName"]'), 'Pankaj Tailor'))
        time.sleep(3)

    def one_way(driver):
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ticketops-seeker-button"]/span[2]')))
        one_way = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="ticketops-seeker-button"]/span[2]')))
        one_way.click()
        select_one_way= driver.find_element(By.XPATH, '//*[@id="ui-id-13"]/span')
        select_one_way.click()

    def depart_location(driver, origen):
        try:

            # cookies = self.driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
            # cookies.click()
            # time.sleep(0.5)
            WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, origen1_xpath)))
            depart_from = driver.find_element(By.XPATH, origen1_xpath)
            depart_from.clear()
            depart_from.send_keys(origen)
            depart_from.send_keys(Keys.ENTER)
            # wait = WebDriverWait(driver, 2)
            time.sleep(0.1)
            print(origen)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def dest_location(driver, destino):
        going_to = driver.find_element(By.XPATH, destino1_xpath)
        going_to.send_keys(destino)
        going_to.send_keys(Keys.ENTER)
        time.sleep(0.1)
        print(destino)

    def depart_date(driver, dias):
        date_depart = driver.find_element(By.XPATH, fechaIda_xpath)
        depDate = date.today() + timedelta(days=dias)
        print('Fecha Ida: '+depDate.strftime('%d%m%Y'))
        date_depart.send_keys(depDate.strftime('%d%m%Y'))
        time.sleep(0.1)

    def return_date(driver, dias):
        date_return = driver.find_element(By.XPATH, fechaVuelta_xpath)
        retDate = date.today() + timedelta(days=dias)
        print('Fecha Vuelta: '+retDate.strftime('%d%m%Y'))
        date_return.send_keys(retDate.strftime('%d%m%Y'))
        date_return.click()
        time.sleep(0.1)

    def depart_date_format(driver, dias):
        date_depart = driver.find_element(By.XPATH, fechaIda_xpath)
        depDate = date.today() + timedelta(days=dias)
        print('Fecha Ida: '+depDate.strftime('%m%d%Y'))
        date_depart.send_keys(depDate.strftime('%m%d%Y'))
        time.sleep(0.1)

    def return_date_format(driver, dias):
        date_return = driver.find_element(By.XPATH, fechaVuelta_xpath)
        retDate = date.today() + timedelta(days=dias)
        print('Fecha Vuelta: '+retDate.strftime('%m%d%Y'))
        date_return.send_keys(retDate.strftime('%m%d%Y'))
        date_return.click()
        time.sleep(0.1)

    def open_pass(driver):
        passengers = driver.find_element(By.XPATH, pasajeros_dropdown)
        passengers.click()
        time.sleep(0.5)

    def add_passengers(driver, num_adults, num_infants, num_babies):
        n_adults = driver.find_element(By.XPATH, add_adults)
        n_infants = driver.find_element(By.XPATH, add_children)
        n_babies = driver.find_element(By.XPATH, add_babies)
        for x in range(num_adults - 1):
            n_adults.click()
        for x in range(num_infants):
            n_infants.click()
        for x in range(num_babies):
            n_babies.click()
        passengers = driver.find_element(By.XPATH, "//*[@id='flight_passengers1']")
        time.sleep(0.5)
        print('Adultos: ' + str(num_adults) + ' Niños: ' + str(num_infants), 'Bebés: '+ str(num_babies))
        passengers.click()

    def click_search(driver):
        search = driver.find_element(By.XPATH, botonBuscar_xpath)
        time.sleep(1)
        search.click()
