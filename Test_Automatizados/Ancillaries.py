import logging
import time
from DEPENDENCIAS import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC, wait
from capture import capture

class Ancillaries():

    def cont_vuelo(driver):
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="bbki-alp-continue-btn"]')))
        except:
            print('No existe')

    def close_seat(driver):

        try:
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="modalSeatMap"]/div/div/div/div[1]/div[2]/div')))


            seat_btn = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/header/div[1]/div/button')))
                                                           # /html/body/div[1]/div/div/div[1]/header/div[1]/div/button
            actions = ActionChains(driver)
            actions.move_to_element(seat_btn).perform()
            seat_btn.click()

        except:
            print('no puedo cerrar el botón')

    def add_bags(driver):
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="OPEN_BAGGAGES"]')))
        time.sleep(5)
        bgg = driver.find_element(By.XPATH, add_baggage)
        bgg.click()

        add23kgida1 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, add_23kgida1)))
        actions = ActionChains(driver)
        actions.move_to_element(add23kgida1).perform()
        add23kgida1.click()

        add23kgvuelta1 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, add_23kgvuelta1)))
        actions = ActionChains(driver)
        actions.move_to_element(add23kgvuelta1).perform()
        add23kgvuelta1.click()

        add23kgida2 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, add_23kgida2)))
        actions = ActionChains(driver)
        actions.move_to_element(add23kgida2).perform()
        add23kgida2.click()

        add23kgvuelta2 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, add_23kgvuelta2)))
        actions = ActionChains(driver)
        actions.move_to_element(add23kgvuelta2).perform()
        add23kgvuelta2.click()

        aceptar = driver.find_element(By.XPATH, accept_bags)
        aceptar.click()

    def add_x_bags(driver, num_bags):
        time.sleep(5)
        bgg = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, add_baggage)))
        actions = ActionChains(driver)
        actions.move_to_element(bgg).perform()
        bgg.click()

        add23kgida1 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/section/form/div/div[2]/div[2]/fieldset/div/div/div[2]/div[1]/div[1]/button[2]')))
        actions = ActionChains(driver)
        actions.move_to_element(add23kgida1).perform()
        for x in range(num_bags):
            add23kgida1.click()

        aceptar = driver.find_element(By.XPATH, accept_bags)
        aceptar.click()

    def add_x_bags_two_adults(driver, num_bags):
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="OPEN_BAGGAGES"]')))
        time.sleep(5)
        bgg = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, add_baggage)))
        bgg.click()

        add23kgida1 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/section/form/div/div[2]/div[2]/fieldset/div/div/div[2]/div[1]/div[1]/button[2]')))
        actions = ActionChains(driver)
        actions.move_to_element(add23kgida1).perform()
        for x in range(num_bags):
            add23kgida1.click()

        aceptar = driver.find_element(By.XPATH, accept_bags)
        aceptar.click()

    def add_flex(driver):
        time.sleep(10)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, add_flex)))
        flex = driver.find_element(By.XPATH, add_flex)
        flex.click()

        addflexrefund = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, flex_refund)))
        actions = ActionChains(driver)
        actions.move_to_element(addflexrefund).perform()
        addflexrefund.click()

        aceptar = driver.find_element(By.XPATH, accept_flex)
        aceptar.click()

        # cont_bton = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH,
        #                                       '/html/body/main/div[2]/div[2]/ib-breakdown-ancillaries/div/div/section/div/div/div[2]/div/button')))
        # actions = ActionChains(driver)
        # actions.move_to_element(cont_bton).perform()
        # cont_bton.click()

    def add_insurance(driver):
        seguro = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/fieldset/div[1]/div/div[1]/label/span[1]')
        actions = ActionChains(driver)
        actions.move_to_element(seguro).perform()
        seguro.click()

        selecc_persona = driver.find_element(By.XPATH, '//*[@id="selectPolicyHolder"]/div[1]/span')
        selecc_persona.click()
        pers = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-11-0"]/span')
        pers.click()

        time.sleep(2)
        num_ident = driver.find_element(By.XPATH, '//*[@id="residentDocument"]')
        num_ident.send_keys('LLLLLL99L99L999L')

        fecha1 = driver.find_element(By.XPATH, '//*[@id="PASSENGER_BIRTH_DATE"]/div[1]')
        fecha1.click()
        dia = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-12-0"]/span')
        dia.click()
        fecha2 = driver.find_element(By.XPATH, '//*[@id="PASSENGER_BIRTH_DATE"]/div[2]')
        fecha2.click()
        mes = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-13-0"]/span')
        mes.click()
        fecha3 = driver.find_element(By.XPATH, '//*[@id="PASSENGER_BIRTH_DATE"]/div[3]')
        fecha3.click()
        agno = driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-14-32"]/span')
        agno.click()
        acpt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/form/div/div/div[3]/div/div[2]/button')
        acpt.click()

        time.sleep(10)

        acept_cond = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/fieldset/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/label')
        actions = ActionChains(driver)
        actions.move_to_element(acept_cond).perform()
        acept_cond.click()

    def add_insurance_NL(driver):
        time.sleep(5)
        cont_bton = WebDriverWait(driver, 1000).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/div')))
        # actions = ActionChains(driver)
        # actions.move_to_element(cont_bton).perform()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # h2 = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/div/h2')
        # h2.location_once_scrolled_into_view
        # actions = ActionChains(driver)
        # actions.move_to_element(h2).perform()
        seguros = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/fieldset/div[1]/div/div[1]/label')
        # seguros.location_once_scrolled_into_view
        actions = ActionChains(driver)
        actions.move_to_element(seguros).perform()
        seguros.click()

        time.sleep(2)


        accept = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/fieldset/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/label')
        actions = ActionChains(driver)
        actions.move_to_element(accept).perform()
        accept.click()

    def continuar(driver):
        cont_bton = WebDriverWait(driver, 1000).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '/html/body/main/div[2]/div[2]/ib-breakdown-ancillaries/div/div/section/div/div/div[2]/div/button')))
        actions = ActionChains(driver)
        actions.move_to_element(cont_bton).perform()
        cont_bton.click()

    def close_banners(driver):
        #Modificado 07/04/2022 por fallo XPATH
        
        # WebDriverWait(driver, 120).until(
            # EC.visibility_of_element_located((By.XPATH, '//*[@id="modalSeatMap"]/div/div/div/div[1]/div[2]') | (By.XPATH,'/html/body/div[1]/div/div/div[1]/form/header/div/button')
            #                                  | (By.CLASS_NAME, 'ib-modals__button-action')))
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="OPEN_BAGGAGES"]')))
        time.sleep(5)
        # WebDriverWait(driver, 120).until(
        #     EC.visibility_of_element_located(
        #         lambda x: x.find_element(By.XPATH, '//*[@id="modalSeatMap"]/div/div/div/div[1]/div[2]')
        #                   or x.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/form/section/div/div[2]/div/fieldset/div[1]/div')
        #                   or x.find_element(By.CLASS_NAME, 'ib-modals__button-action')))
        try:
            if driver.find_element(By.XPATH, '//*[@id="modalSeatMap"]/div/div/div/div[1]/div[2]'):
                print('SEATS')
                cls_seat = driver.find_element(By.CLASS_NAME, 'ib-upgrade__button-close')
                cls_seat.click()
        except:
            print('')

        try:
            if driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/form/header'):
                texto = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/form/header').text
                print('FLEX')
                cls_flex = driver.find_element(By.CLASS_NAME, 'ib-modals__button-action')
                cls_flex.click()
        except:
            print('')

        try:
            if driver.find_element(By.CLASS_NAME, 'ib-heading').text == 'Prioridad de embarque':
                print('PRIO')
                cls_prio = driver.find_element(By.XPATH, '//*[@id="upselling-prio-modal"]/div/div/header/div/button')
                cls_prio.click
        except:
            print('')

    def MAD_MLN_2adults_x_bags(driver, n):
        # añade N maletas de 15kg en la vuelta a 2 pasajeros adultos
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="OPEN_BAGGAGES"]')))
        time.sleep(5)
        bgg = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="OPEN_BAGGAGES"]')))
        bgg.click()
        time.sleep(2)
        add = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/section/form/div/div[1]/div[2]/fieldset/div/div[2]/div[2]/div[1]/div[1]/button[2]')))
        for x in range(n):
            add.click()
        time.sleep(1)
        add2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/form/div/div[2]/div[2]/fieldset/div/div[2]/div[2]/div[1]/div[1]/button[2]')
        actions = ActionChains(driver)
        actions.move_to_element(add2).perform()
        for x in range(n):
            add2.click()
        aceptar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/form/footer/button')
        aceptar.click()

    def add_seats_2adults_confort_RT(driver):
        time.sleep(2)
        
        openSeatMap = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/div[3]/equal-height/div[1]/ib-seat-map-box/div/section/div/div[2]/div[2]/div/button')
        openSeatMap.click()
        time.sleep(5)
        seat_key = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/button')
        seat_key.click()
        standardFree = driver.find_elements(By.CLASS_NAME, 'ib-map__column--free')
        actions = ActionChains(driver)
        actions.move_to_element(standardFree[0]).perform()
        time.sleep(5)
        print(len(standardFree))
        standardFree[0].click()
        next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/button')
        next.click()
        time.sleep(1)
        standardFree[1].click()
        next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/button')
        next.click()

        time.sleep(5)
        standardFree = driver.find_elements(By.CLASS_NAME, 'ib-map__column--free')
        # WebDriverWait(driver, 50).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, standardFree[0])))

        standardFree[0].click()
        next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/button')
        next.click()
        time.sleep(1)
        standardFree[1].click()
        next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/footer/button')
        next.click()

        ok = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/section/footer/button')))
        ok.click()

    def delete_bags_from_basket(driver):
        time.sleep(5)
        # WebDriverWait(driver, 50).until(
        #     EC.visibility_of_element_located((By.XPATH,
        #                                       '//*[@id="pmt-discount"]/div')))
        open_basket = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[1]/ib-new-main-header/div[1]/div/div/div/div/ib-header/div/div/div/div/div/ib-basket/div/a/div/div/span[1]')))
        open_basket.click()
        delete_bags = driver.find_element(By.XPATH, '/html/body/main/div[1]/ib-new-main-header/div[1]/div/div/div/div/ib-header/div/div/div/div/div/ib-basket/div/div/div/div/div/div/uib-accordion/div/ib-ancillaries-baggages/section/ul/li/ul/li/div/span[2]/a/span')
        actions = ActionChains(driver)
        actions.move_to_element(delete_bags).perform()
        delete_bags.click()
        time.sleep(2)
        open_basket.click()

    def is_bag_available(driver):
        # DEF: This is a getter method to determine if bag ancillary is abailable or not

        print("Checking if bag is available...")
        # preventive sleep
        time.sleep(10)
        try:
            bgg = WebDriverWait(driver, 60).until(
                        EC.visibility_of_element_located((By.XPATH, add_baggage)))
            # capture after prev sleep and wait driver
            capture.capture_screen(driver,"screenshots","INT_001_BAG_NALP_OK")
            if bgg: return True
            else: return False

        except:
            # capture of any failure
            capture.capture_screen(driver,"screenshots","INT_001_BAG_NALP_KO")
            return False
            
            

    def is_seat_available(driver):
        # DEF: This is a getter method to determine if seat ancillary is abailable or not

        print("Checking if seat is available...")
        # preventive sleep
        time.sleep(10)
        
        try:
            # solo funciona de esta manera 
            seatav =  driver.find_element(By.XPATH, '//button[@ng-click="ibSeatMapBoxCtrl.openSeatMap()"]')    
            #seatav.click()

            #seatav = WebDriverWait(driver, 60).until(
            #            EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[2]/div[2]/div[3]/equal-height/div[1]/ib-seat-map-box/div/section/div/div[2]/div[2]/div/button')))
            # capture after prev sleep and wait driver
            capture.capture_screen(driver,"screenshots","INT_001_SEAT_NALP_OK")
            #print(seatav)
            if seatav: return True
            else: return False
        except:
            # capture of any failure
            capture.capture_screen(driver,"screenshots","INT_001_SEAT_NALP_KO")
            return False


    def is_specs_available(driver):
        # DEF: This is a getter method to determine if specs ancillary is abailable or not

        print("Checking if specs is available...")
        # preventive sleep
        time.sleep(10)
        return False

    def is_prio_available(driver):
        # DEF: This is a getter method to determine if priority ancillary is abailable or not
       
        print("Checking if prio is available...")
        # preventive sleep
        time.sleep(10)
        return False
        
    def is_flex_available(driver):
        # DEF: This is a getter method to determine if flex ancillary is abailable or not
        
        print("Checking if flex is available...")
        # preventive sleep
        time.sleep(10)
        
        try:
            
            time.sleep(10)
            WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, add_flex)))
            flex = driver.find_element(By.XPATH, add_flex)
            if flex:
                return True
            else:
                return False
        except:
            # capture of any failure
            capture.capture_screen(driver,"screenshots","INT_001_FLEX_KO")
            return False
            
         

    def is_ins_available(driver):
        # DEF: This is a getter method to determine if insurance ancillary is abailable or not
 
        print("Checking if insurance is available...")
        # preventive sleep
        time.sleep(10)
        
        try:
            time.sleep(10)
            seguro = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/ib-insurance/div/div/form/div/div/div/fieldset/div[1]/div/div[1]/label/span[1]')
            if seguro:
                return True
            else:
                return False
        except:
            # capture of any failure
            capture.capture_screen(driver,"screenshots","INT_001_PRIO_KO")
            return False



    def santander(driver):
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'lc-a19-details-btn')))
        cls_santander = driver.find_element(By.CLASS_NAME, 'lc-a19-details-btn')
        cls_santander.click()
