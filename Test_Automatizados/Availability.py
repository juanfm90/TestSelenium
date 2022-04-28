
import time
from DEPENDENCIAS import *
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC


class Availability():

    def ocultar_info(driver):
        ocultar = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, ocultarInfo)))
        ocultar.click()

    def vuelos_ida(driver, cabina, tarifa, operador):
        vuelos_ida = driver.find_element(By.XPATH, div_ida)
        ib = vuelos_ida.find_elements(By.TAG_NAME, "img")
        index = 0
        if (operador == 'IB'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_IB.svg"
        elif (operador == 'BA'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_BA.svg"
        elif (operador == 'YW'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_YW.svg"
        elif (operador == 'I2'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_I2.svg"
        for x in ib:
            atr = x.get_attribute("ng-src")
            print(atr)
            index = index+1
            print(str(index))
            if atr == '/iberia-web-content/iconos/avios/booking_cash_and_avios_en.png':
                index=index-1
                print(str(index))
            if (atr == img_operador):
                print(str(index))
                break
        index = int((index - 1) / 2)
        print(str(index))
        if (cabina == 'Turista'):
            botones_basica = vuelos_ida.find_elements(By.CLASS_NAME, 'ib-box-mini-fare__box--type-1')
            botones_basica[index].click()
        elif (cabina == 'Business'):
            botones_business = vuelos_ida.find_elements(By.CLASS_NAME, 'ib-box-mini-fare__box--type-3')
            botones_business[index].click()

        time.sleep(1)
        try:
            vuelos_ida = driver.find_element(By.XPATH, div_vuelos_ida_seleccionada)
            time.sleep(0.2)
        except StaleElementReferenceException:
            vuelos_ida = driver.find_element(By.XPATH, div_vuelos_ida_seleccionada)
            pass

        time.sleep(0.2)

        radios_ida = vuelos_ida.find_elements(By.CLASS_NAME, radios_tarifa_ida)
        radios_ida[tarifa].click()
        time.sleep(1)

    def vuelos_vuelta(driver, cabina, tarifa, operador):
        vuelos_vuelta = driver.find_element(By.XPATH, div_vuelta)
        ib = vuelos_vuelta.find_elements(By.TAG_NAME, "img")
        actions = ActionChains(driver)
        actions.move_to_element(ib[0]).perform()
        index = 0
        if (operador == 'IB'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_IB.svg"
        elif (operador == 'BA'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_BA.svg"
        elif (operador == 'YW'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_YW.svg"
        elif (operador == 'I2'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_I2.svg"
        for x in ib:
            atr = x.get_attribute("ng-src")
            print(atr)
            index = index + 1
            print(str(index))
            if atr == '/iberia-web-content/iconos/avios/booking_cash_and_avios_en.png':
                index = index - 1
                print(str(index))
            if (atr == img_operador):
                print(str(index))
                break
        index = int((index - 1) / 2)
        print(str(index))
        if (cabina == 'Turista'):
            botones_basica = vuelos_vuelta.find_elements(By.CLASS_NAME, 'ib-box-mini-fare__box--type-1')
            botones_basica[index].click()
        elif (cabina == 'Business'):
            botones_business = vuelos_vuelta.find_elements(By.CLASS_NAME, 'ib-box-mini-fare__box--type-3')
            botones_business[index].click()

        time.sleep(1)
        try:
            vuelos_vuelta = driver.find_element(By.XPATH, div_vuelos_vuelta_seleccionada)
            time.sleep(2)
        except StaleElementReferenceException:
            vuelos_vuelta = driver.find_element(By.XPATH, div_vuelos_vuelta_seleccionada)
            pass

        time.sleep(0.2)

        radios_ida = vuelos_vuelta.find_elements(By.CLASS_NAME, radios_tarifa_vuelta)
        radios_ida[tarifa].click()
        time.sleep(1)

    def results_ida(driver,cabina, tarifa, operador):
        global cab
        if(cabina == 'Turista'):
            cab = 2
            cab_el = 0
        elif(cabina=='Business'):
            cab = 1
            cab_el = 1
        elif (cabina == 'Business_LH'):
            cab = 0
            cab_el = 2

        if (operador == 'IB'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_IB.svg"
        elif (operador == 'BA'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_BA.svg"
        elif (operador == 'YW'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_YW.svg"
        elif (operador == 'I2'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_I2.svg"

        vuelos_ida = driver.find_element(By.XPATH, div_ida)
        ib = vuelos_ida.find_elements(By.TAG_NAME, "img")
        miIndex = 0
        for x in ib:
            miIndex = miIndex + 1

            atr = x.get_attribute("ng-src")
            print(atr)

            if (atr == img_operador):
                miIndex = miIndex - 1
                # print(str(miIndex))
                break
        if (miIndex >= 3):
            botones = vuelos_ida.find_elements(By.TAG_NAME, "button")
            # print(len(botones))
            select = int(miIndex)  # /3 #+5
            # print(str(select))
            int(select)
            time.sleep(1)
            botones[int(select) - cab].click() #-2 para turista, -1 para business
        else:
            botones = vuelos_ida.find_elements(By.TAG_NAME, "button")
            botones[2+cab_el].click() #2 para turista, 3 para business
        # print(str(miIndex))


        try:
            vuelos_ida = driver.find_element(By.XPATH, div_vuelos_ida_seleccionada)
            time.sleep(0.2)
        except StaleElementReferenceException:
            vuelos_ida = driver.find_element(By.XPATH, div_vuelos_ida_seleccionada)
            pass

        time.sleep(0.2)

        radios_ida = vuelos_ida.find_elements(By.CLASS_NAME, radios_tarifa_ida)
        radios_ida[tarifa].click()

        URL = driver.current_url
        var = URL.split("/")[-1]
        print("Quadrigam: " + var)
        bool = False
        if(var == 'availability'):
            bool= True
        else:
            bool= False

        print(bool)


    def results_vuelta(driver, cabina, tarifa, operador):
        global cab
        if(cabina == 'Turista'):
            cab = 2
            cab_el = 0
        elif(cabina=='Business'):
            cab = 1
            cab_el = 1
        elif (cabina == 'Business_LH'):
            cab = 0
            cab_el = 2

        if (operador == 'IB'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_IB.svg"
        elif (operador == 'BA'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_BA.svg"
        elif (operador == 'YW'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_YW.svg"
        elif (operador == 'I2'):
            img_operador = "/iberia-web-content/iconos/aerolineas/logo_pos_I2.svg"


        time.sleep(2)
        vuelos_vuelta = driver.find_element(By.XPATH, div_vuelta)
        ib = vuelos_vuelta.find_elements(By.TAG_NAME, "img")

        actions = ActionChains(driver)
        actions.move_to_element(ib[0]).perform()


        miIndex = 0
        for x in ib:
            miIndex = miIndex + 1

            atr = x.get_attribute("ng-src")
            print(atr)
            if (atr == img_operador):
                miIndex = miIndex - 1
                # print(str(miIndex))
                break


        if (miIndex >= 3):
            botones = vuelos_vuelta.find_elements(By.TAG_NAME, "button")
            # for element in vuelos_vuelta.find_elements(By.TAG_NAME, "button"):
            #     print(element.text)
            select = int(miIndex)  # /3 #+5
            # print(str(select))
            int(select)
            time.sleep(1)
            botones[int(select) - cab].click() #-2 para turista, -1 para business
        else:
            botones = vuelos_vuelta.find_elements(By.TAG_NAME, "button")
            # print(len(botones))
            # for element in vuelos_vuelta.find_elements(By.TAG_NAME, "button"):
            #     print(element.text)
            botones[2+cab_el].click() #2 para turista, 3 para business

        # print(str(miIndex))

        try:
            vuelos_vuelta = driver.find_element(By.XPATH, div_vuelos_vuelta_seleccionada)
            time.sleep(2)
        except StaleElementReferenceException:
            vuelos_vuelta = driver.find_element(By.XPATH, div_vuelos_vuelta_seleccionada)
            pass

        radios_vuelta = vuelos_vuelta.find_elements(By.CLASS_NAME, radios_tarifa_vuelta)
        radios_vuelta[tarifa].click()
        time.sleep(0.2)

    def continuar(driver):
        # WebDriverWait(driver, 15).until(
        #     EC.visibility_of_element_located((By.ID, botonContinuar)))
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        btn_cont = driver.find_element(By.ID, botonContinuar)
        # driver.execute_script("arguments[0].scrollIntoView();", btn_cont)
        btn_cont.location_once_scrolled_into_view
        actions = ActionChains(driver)
        actions.move_to_element(btn_cont).perform()
        btn_cont.click()
