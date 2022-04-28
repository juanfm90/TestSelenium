import time
from DEPENDENCIAS import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

class Pagos():

    def select_visa(driver):
        time.sleep(5)
        # WebDriverWait(self.driver, 50).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, '//*[@id="pmt-credit-card-tab-generic-credit-card-fields-1"]/div[2]/div[1]')))
        # dropdown1 = WebDriverWait(self.driver, 50).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="pmt-credit-card-tab-generic-credit-card-fields-1"]/div[2]/div[1]')))
        # dropdown1.click()
        #
        # cards = dropdown1.find_elements(By.CLASS_NAME, 'ib-select__list-txt')
        # cards[0].click()

        time.sleep(1)
        WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="ibdc-number-frame"]')))

        iframe2 = driver.find_element(By.XPATH, '//*[@id="ibdc-number-frame"]')
        driver.switch_to.frame(iframe2)


        num_card = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="number"]')))
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(num_card, 5, 5)
        
        num_card.send_keys('4012999999999999')

        driver.switch_to.parent_frame()

        nom_card = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
        actions = ActionChains(driver)
        actions.move_to_element(nom_card).perform()
        nom_card.send_keys('HANSOLO')

        surname_card = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="surnames"]')))
        actions = ActionChains(driver)
        actions.move_to_element(surname_card).perform()
        surname_card.send_keys('HANSOLO')

        open_month = driver.find_element(By.XPATH, '//*[@id="EXPIRY_DATE"]/div[1]/div[1]/span')
        open_month.click()
        month = driver.find_element(By.CLASS_NAME, 'ib-select-date__action--month')
        list = month.find_elements(By.CLASS_NAME, 'ib-select-date__list-txt')
        list[1].click()
        
        open_year = driver.find_element(By.XPATH, '//*[@id="EXPIRY_DATE"]/div[2]/div[1]/span')
        open_year.click()
        
        year = driver.find_element(By.CLASS_NAME, 'ib-select-date__action--year')
        list2 = year.find_elements(By.CLASS_NAME, 'ib-select-date__list-txt')
        list2[3].click()

        iframe3 = driver.find_element(By.XPATH, '//*[@id="ibdc-cvv-frame"]')
        driver.switch_to.frame(iframe3)

        cvv = driver.find_element(By.XPATH, '//*[@id="cvv"]')
        cvv.send_keys('123')

        driver.switch_to.parent_frame()

        acpt = driver.find_element(By.XPATH, aceptar_term)
        acpt.click()





    def select_visa_PREB(driver):
        time.sleep(5)
        # WebDriverWait(self.driver, 50).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH, '//*[@id="pmt-credit-card-tab-generic-credit-card-fields-1"]/div[2]/div[1]')))
        # dropdown1 = WebDriverWait(self.driver, 50).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="pmt-credit-card-tab-generic-credit-card-fields-1"]/div[2]/div[1]')))
        # dropdown1.click()
        #
        # cards = dropdown1.find_elements(By.CLASS_NAME, 'ib-select__list-txt')
        # cards[0].click()

        time.sleep(1)
        WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="ibdc-number-frame"]')))

        iframe2 = driver.find_element(By.XPATH, '//*[@id="ibdc-number-frame"]')
        driver.switch_to.frame(iframe2)


        num_card = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="number"]')))
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(num_card, 5, 5)
        num_card.send_keys('4012999999999999')

        driver.switch_to.parent_frame()

        nom_card = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
        actions = ActionChains(driver)
        actions.move_to_element(nom_card).perform()
        nom_card.send_keys('HANSOLO')

        surname_card = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="surnames"]')))
        actions = ActionChains(driver)
        actions.move_to_element(surname_card).perform()
        surname_card.send_keys('HANSOLO')

        open_month = driver.find_element(By.XPATH, '//*[@id="EXPIRY_DATE"]/div[1]/div[1]/span')
        open_month.click()
        exp_month = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-4-4"]/span/span')
        exp_month.click()
        open_year = driver.find_element(By.XPATH, '//*[@id="EXPIRY_DATE"]/div[2]/div[1]/span')
        open_year.click()
        exp_year = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-5-3"]')
        exp_year.click()

        iframe3 = driver.find_element(By.XPATH, '//*[@id="ibdc-cvv-frame"]')
        driver.switch_to.frame(iframe3)

        cvv = driver.find_element(By.XPATH, '//*[@id="cvv"]')
        cvv.send_keys('123')

        driver.switch_to.parent_frame()

        acpt = driver.find_element(By.XPATH, aceptar_term)
        acpt.click()
        





    def select_visa_seguro(driver):
        time.sleep(5)
        time.sleep(1)
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="ibdc-number-frame"]')))

        iframe2 = driver.find_element(By.XPATH, '//*[@id="ibdc-number-frame"]')
        driver.switch_to.frame(iframe2)

        num_card = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="number"]')))
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(num_card, 5, 5)
        num_card.send_keys('4918018734634624')

        driver.switch_to.parent_frame()

        nom_card = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))
        actions = ActionChains(driver)
        actions.move_to_element(nom_card).perform()
        nom_card.send_keys('HANSOLO')

        surname_card = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="surnames"]')))
        actions = ActionChains(driver)
        actions.move_to_element(surname_card).perform()
        surname_card.send_keys('HANSOLO')

        open_month = driver.find_element(By.XPATH, '//*[@id="EXPIRY_DATE"]/div[1]/div[1]/span')
        open_month.click()

        month = driver.find_element(By.CLASS_NAME, 'ib-select-date__action--month')
        list = month.find_elements(By.CLASS_NAME, 'ib-select-date__list-txt')
        list[1].click()
        open_year = driver.find_element(By.XPATH, '//*[@id="EXPIRY_DATE"]/div[2]/div[1]/span')
        open_year.click()

        year = driver.find_element(By.CLASS_NAME, 'ib-select-date__action--year')
        list2 = year.find_elements(By.CLASS_NAME, 'ib-select-date__list-txt')
        list2[3].click()

        iframe3 = driver.find_element(By.XPATH, '//*[@id="ibdc-cvv-frame"]')
        driver.switch_to.frame(iframe3)

        cvv = driver.find_element(By.XPATH, '//*[@id="cvv"]')
        cvv.send_keys('737')

        driver.switch_to.parent_frame()

        acpt = driver.find_element(By.XPATH, aceptar_term)
        acpt.click()



    def delete_bags_from_basket_and_return(driver):
        time.sleep(5)
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="pmt-discount"]/div')))
        open_basket = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[1]/ib-new-main-header/div[1]/div/div/div/div/ib-header/div/div/div/div/div/ib-basket/div/a/div/div/span[1]')))
        open_basket.click()
        delete_bags = driver.find_element(By.XPATH, '/html/body/main/div[1]/ib-new-main-header/div[1]/div/div/div/div/ib-header/div/div/div/div/div/ib-basket/div/div/div/div/div/div/uib-accordion/div/ib-ancillaries-baggages/section/ul/li/ul/li/div/span[2]/a/span')
        actions = ActionChains(driver)
        actions.move_to_element(delete_bags).perform()
        delete_bags.click()
        time.sleep(2)
        open_basket.click()
        time.sleep(1)
        driver.execute_script("window.history.go(-1)")



    def select_card_FF(driver):
        WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="pmt-nav-tab-credit-card-tab"]/fieldset/div/div[2]/div[1]/label')))
        select_other_card = driver.find_element(By.XPATH, '//*[@id="pmt-nav-tab-credit-card-tab"]/fieldset/div/div[2]/div[1]/label')
        select_other_card.click()



    def pagar(driver):
        pago = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, pagar)))
        actions = ActionChains(driver)
        actions.move_to_element(pago).perform()
        pago.click()



    def get_pnr(driver):
        final_pnr = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, pnr)))
        print(final_pnr.text)
        return final_pnr.text



    def write_excel_file(self, cell):
        final_pnr = Pagos.get_pnr(self)
        bk = openpyxl.load_workbook('Variables.xlsx')
        s = bk.active
        s[cell] = final_pnr
        bk.save("Variables.xlsx")