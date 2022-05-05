import logging
import csv
import os.path
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*
from capture import capture
from datetime import datetime


class Tarjeta_Regalo_Terceros(unittest.TestCase):
    def setUp(self):

        try:
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d")
            logging.basicConfig(filename='log/'+'Sanity_013_log_Tarjeta_Regalo_Terceros', filemode='w', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            
            logging.info("Test_Name:Tarjeta_Regalo_Terceros")
            logging.info("Test_description: Comprar una tarjeta regalo para una tercera persona")
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
        logging.info("==Tarjeta_Regalo_Terceros.acceso_tr==")
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
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Terceros_ERROR_acceso_tr")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            logging.info("Tarjeta_Regalo_Terceros_KO")
            slef.driver.close()
            quit()


    def select_tr_conditions(self):
        logging.info("==Tarjeta_Regalo_Terceros.select_tr_conditions==")
        logging.info("Seleccionando condiciones de TR")
        try:

            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, tr_terceros)))
            tipo_tr = self.driver.find_element(By.XPATH, tr_terceros) # Mueve a tipo de tarjeta para terceros
            time.sleep(3)
            tipo_tr.click() # Click a tipo de tarjeta para terceros
            logging.info("Seleccionado tipo de tarjeta a terceros")
            logging.info("Datos de la tarjeta:")
            F2 = Datos_pasajeros.read_tr_cantidad_terceros(self) # Carga del excel el valor de la tarjeta a comprar
            if (F2.value == 50):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_50)
                time.sleep(0.5)
                cantidad.click()
            elif (F2.value == 100):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_100)
                time.sleep(0.5)
                cantidad.click()
            elif (F2.value == 300):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_300)
                time.sleep(0.5)
                cantidad.click()
            elif (F2.value == 500):
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, importe_500)
                time.sleep(0.5)
                cantidad.click()
            else:
                time.sleep(0.5)
                cantidad = self.driver.find_element(By.XPATH, otro_importe)
                cantidad.send_keys(F2.value)

            logging.info("Cantidad... "+str(F2.value))

            F3 = Datos_pasajeros.read_tr_email_remitente(self) # Carga email del remitente
            time.sleep(0.5)
            correo_del_remitente = self.driver.find_element(By.XPATH, email_remitente) #selecciona email del remitente
            correo_del_remitente.send_keys(F3.value) #Introduce email del remitente
            logging.info("Email remitente... "+str(F3.value))
            
            F4 = Datos_pasajeros.read_tr_email_receptor(self) # Carga email del receptor
            time.sleep(0.5)
            correo_del_destinatario = self.driver.find_element(By.XPATH, email_receptor_terceros) #selecciona email del receptor
            correo_del_destinatario.send_keys(F4.value) #Introduce email del receptor
            logging.info("Email destinatario... "+str(F4.value))
            
            F5 = Datos_pasajeros.read_tr_nombre_remitente(self) # Carga nombre del remitente
            time.sleep(0.5)
            nombre_del_remitente = self.driver.find_element(By.XPATH, nombre_remitente) #selecciona nombre del remitente
            nombre_del_remitente.send_keys(F5.value) #Introduce nombre del remitente
            logging.info("Nombre remitente... "+str(F5.value))
            
            F6 = Datos_pasajeros.read_tr_nombre_receptor(self) # Carga nombre del receptor
            time.sleep(0.5)
            nombre_del_destinatario = self.driver.find_element(By.XPATH, nombre_receptor_terceros) #selecciona nombre del receptor
            nombre_del_destinatario.send_keys(F6.value) #Introduce nombre del receptor
            logging.info("Nombre receptor... "+str(F6.value))
                        
            F7 = Datos_pasajeros.read_tr_mensaje(self)  # Carga mensaje de la tarjeta regalo
            time.sleep(0.5)
            mensaje = self.driver.find_element(By.XPATH, mensaje_personalizado)  # selecciona el campo del mensaje
            mensaje.clear()
            mensaje.send_keys(F7.value)  # Introduce el mensaje
            time.sleep(0.5)
            logging.info("Mensaje personalizado... "+str(F7.value))

            F8 = Datos_pasajeros.read_tr_impresion_check(self)
            F9 = Datos_pasajeros.read_email_impresion(self)
            if (F8.value == 'TRUE'):
                check = self.driver.find_element(By.XPATH, check_envio_remitente)
                check.click()
                time.sleep(0.5)
                email_impresion = self.driver.find_element(By.XPATH, email_recepcion_remitente)
                email_impresion.clear()
                time.sleep(0.5)
                email_impresion.send_keys(F9.value)

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
            logging.info("Tarjeta_Regalo_Terceros_KO")
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Terceros_ERROR_select_tr_conditions")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            self.driver.close()
            quit()

    def pago(self):
        logging.info("==Tarjeta_Regalo_Terceros.pago==")
        try:
            Pagos.select_visa_seguro_DS3(self.driver)
            logging.info("Pago realizado con isa_seguro_DS3")
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            logging.error("No se ha podido pagar la TR. Reason = "+str(e))
            logging.info("Tarjeta_Regalo_Terceros_KO")
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Terceros_ERROR_pago")
            logging.error("Debido a que el error es crítico se cierra el webdriver y se detiene la ejecución.")
            self.driver.close()
            quit()

    def comprobacion_final(self):
        logging.info("==Tarjeta_Regalo_Terceros.comprobacion_final==")
        try:
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, confirmacion_compra)))
            texto = self.driver.find_element(By.XPATH, confirmacion_compra).text

            if (texto == "La compra se ha realizado correctamente"):
                print ("TEST EJECUTADO CORRECTAMENTE")
                logging.info("La compra se ha realizado correctamente")
                logging.info("TEST EJECUTADO CORRECTAMENTE")
                logging.info("Tarjeta_Regalo_Terceros_OK")
            else:
                logging.info("resultado KO del TEST --> Tarjeta_Regalo_Terceros_KO")
                capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Terceros_ERROR_comprobacion_final")

            driver = self.driver
            driver.close()
            
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            logging.error("Error en la comprobacion_final. Reason = "+str(e))
            logging.info("Tarjeta_Regalo_Terceros_KO")
            capture.capture_screen(self.driver,"screenshots","Tarjeta_Regalo_Terceros_ERROR_comprobacion_final")
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
