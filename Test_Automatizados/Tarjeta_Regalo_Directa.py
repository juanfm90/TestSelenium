import logging
import csv
import os.path
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*
from datetime import datetime

class Tarjeta_Regalo_Directa(unittest.TestCase):
    def setUp(self):
        try:
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d")
            logging.basicConfig(filename='log/'+'Tarjeta_Regalo_Directa'+'_log_'+dt_string, filemode='w', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:Tarjeta_Regalo_Directa")
            logging.info("Test_description: Comprar una tarjeta regalo directa")
        except Exception as e:
            print(f'Error configurando logger: {e}')

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver = self.driver
            driver.get("https://pree.iberia.es")
            # driver.get("https://pree.iberia.es/be/?language=fr")
            driver.delete_all_cookies()
            driver.maximize_window()
            time.sleep(5)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('webdriver: Ok')

    def acceso_tr(self):
        logging.info("==Tarjeta_Regalo_Directa.acceso_tr==")
        try:
            logging.info("Accediendo a menu tarjetas regalo")
            actions = ActionChains(self.driver)
            landing = self.driver.find_element(By.XPATH, viaja) # Abre desplegable "VIAJA"
            actions.move_to_element(landing).perform() # Se posiciona dentro de el desplegable "VIAJA"
            tr = self.driver.find_element(By.XPATH, tarjetas_regalo) # Se mueve hasta "Tarjetas Regalo"
            tr.click() #Hace click en "Tarjetas Regalo"
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, compra_TR)))
            logging.info("Dentro del menu de TR")
            compra_tr = self.driver.find_element(By.XPATH, compra_TR) # Mueve a "Compra una tarjeta regalo"
            time.sleep(0.5)
            compra_tr.click() # Click a "Compra una tarjeta regalo"
            logging.info("Click en comprar tarjeta regalo")

        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            logging.error("No se ha podido acceder a menu tarjetas regalo. Reason = "+str(e))
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Directa_ERROR_acceso_tr")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            logging.info("Tarjeta_Regalo_Directa_KO")
            slef.driver.close()
            quit()


    def select_tr_conditions(self):
        logging.info("==Tarjeta_Regalo_Directa.select_tr_conditions==")
        logging.info("Seleccionando condiciones de TR")
        try:

            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, tr_primeros)))
            tipo_tr = self.driver.find_element(By.XPATH, tr_primeros) # Mueve a tipo de tarjeta para uno mismo
            time.sleep(3)
            tipo_tr.click() # Click a tipo de tarjeta para uno mismo
            logging.info("Seleccionado tipo de tarjeta a terceros")
            logging.info("Datos de la tarjeta:")

            H2 = Datos_pasajeros.read_tr_cantidad_primeros(self) # Carga del excel el valor de la tarjeta a comprar
            if (H2.value == 50):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_50)
                time.sleep(0.5)
                cantidad.click()
            elif (H2.value == 100):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_100)
                time.sleep(0.5)
                cantidad.click()
            elif (H2.value == 300):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_300)
                time.sleep(0.5)
                cantidad.click()
            elif (H2.value == 500):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_500)
                time.sleep(0.5)
                cantidad.click()
            else:
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, otro_importe)
                cantidad.send_keys(H2.value)

            logging.info("Cantidad... "+str(H2.value))
            
            H3 = Datos_pasajeros.read_tr_email_primeros(self) # Carga email de compra
            time.sleep(0.5)
            correo_del_destinatario = self.driver.find_element(By.XPATH, email_receptor_primeros) #selecciona email de compra
            correo_del_destinatario.send_keys(H3.value) #Introduce email de compra
            logging.info("Correo destinatario... "+str(H3.value))
            
            time.sleep(0.5)
            boton_pago = self.driver.find_element(By.XPATH, ir_al_pago)
            time.sleep(0.5)
            boton_pago.click()

            time.sleep(0.5)
            boton_condiciones = self.driver.find_element(By.XPATH, aceptar_condiciones)
            time.sleep(0.5)
            boton_condiciones.click()

        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            logging.error("No se ha podido cumplimentar las condiciones de TR. Reason = "+str(e))
            logging.info("Tarjeta_Regalo_Directa_KO")
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Directa_ERROR_select_tr_conditions")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            self.driver.close()
            quit()

    def pago(self):
        logging.info("==Tarjeta_Regalo_Directa.pago==")
        try:
            Pagos.select_visa_seguro_DS3(self.driver)
            logging.info("Pago realizado con isa_seguro_DS3")
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            logging.error("No se ha podido pagar la TR. Reason = "+str(e))
            logging.info("Tarjeta_Regalo_Directa_KO")
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Directa_ERROR_pago")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            self.driver.close()
            quit()

    def comprobacion_final(self):
        logging.info("==Tarjeta_Regalo_Directa.comprobacion_final==")
        try:
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, confirmacion_compra)))
            texto = self.driver.find_element(By.XPATH, confirmacion_compra).text

            if (texto == "La compra se ha realizado correctamente"):
                print ("TEST EJECUTADO CORRECTAMENTE")
                logging.info("La compra se ha realizado correctamente")
                logging.info("TEST EJECUTADO CORRECTAMENTE")
                logging.info("Tarjeta_Regalo_Directa_OK")
            else:
                logging.info("resultado KO del TEST --> Tarjeta_Regalo_Directa_KO")
                capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Directa_ERROR_comprobacion_final")

            driver = self.driver
            river.close()
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            logging.error("Error en la comprobacion_final. Reason = "+str(e))
            logging.info("Tarjeta_Regalo_Directa_KO")
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Directa_ERROR_comprobacion_final")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            self.driver.close()
            quit() 
            
            
    def test_NALP(self):
        self.acceso_tr() #Función que accede desde la pagina principal a la compra de tarjetas
        self.select_tr_conditions() #Funcion que configura la Tarjeta Regalo
        self.pago() #Funcion que realiza el pago de la Tarjeta Regalo
        self.comprobacion_final()
        #time.sleep(50000)


if __name__ == '__main__':
    unittest.main()