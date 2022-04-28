import time
import unittest
from DEPENDENCIAS import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class iberia_automatica(unittest.TestCase):

    def setUp(self):
        try:
            #self.driver = webdriver.Chrome(executable_path=r'D:/Iberia_Automatica/chromedriver/chromedriver.exe')
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.maximize_window()
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('webdriver: Ok')

    def test_buscar_vuelo(self):
        try:
            driver = self.driver
            driver.get(iberia_pree)
            time.sleep(1)
            destino = driver.find_element(By.ID,destino1)
            time.sleep(1)
            destino.send_keys('Bilbao')
            destino.send_keys(Keys.RETURN)
            boton_rutas = driver.find_element(By.XPATH,botonRutas)
            boton_rutas.click()
            solo_ida = driver.find_element(By.XPATH,soloIda)
            solo_ida.click()
            fecha_ida = driver.find_element(By.ID,fechaIda)
            fecha_ida.send_keys('14032022')
            driver.find_element(By.ID,botonBuscar).click()

            try:
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,ocultarInfo)))
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')

            ocultar_info = self.driver.find_element(By.XPATH,ocultarInfo)
            ocultar_info.click()
            vuelo_turista_ida = self.driver.find_element(By.ID,vueloTuristaIda)
            vuelo_turista_ida.click()
            time.sleep(1)

            try:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #scroll
                time.sleep(2)
                continuar = driver.find_element(By.ID, botonContinuar)
                continuar.click()
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, nombrePasajero)))
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            finally:
                print('Fin funcion scroll')

            nombre_pasajero = driver.find_element(By.XPATH,nombrePasajero)
            nombre_pasajero.send_keys('adulto1')
            apellido_pasajero = driver.find_element(By.XPATH,apellidoPasajero)
            apellido_pasajero.send_keys('test')

            try:
                localizar = driver.find_element(By.XPATH,'//*[@id="name_0"]').location_once_scrolled_into_view
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            finally:
                print('Fin funcion scroll')

            contacto_email = driver.find_element(By.XPATH, contactoEmail)
            contacto_email.send_keys('panel.iduran@iberia.es')
            repetir_email = driver.find_element(By.XPATH, repetirEmail)
            repetir_email.send_keys('panel.iduran@iberia.es')
            numero_telefono = driver.find_element(By.ID, numeroTelefono)
            numero_telefono.send_keys('111222333')
            boletin_noticias = driver.find_element(By.XPATH, boletinNoticias)
            boletin_noticias.click()
            continuar = driver.find_element(By.ID, botonContinuar)
            continuar.click()

            #Ancillaries
            try:
                try:
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, cerrarSeleccionAsientos)))
                    time.sleep(3)
                    cerrar_seleccion_asientos = driver.find_element(By.XPATH, cerrarSeleccionAsientos)
                    cerrar_seleccion_asientos.click()
                except:
                    pass
                try:
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, cerrarFlexibilidad )))
                    time.sleep(3)
                    cerrar_flexibilidad = driver.find_element(By.XPATH, cerrarFlexibilidad)
                    cerrar_flexibilidad.click()
                except:
                    pass
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # scroll
                time.sleep(2)
                continuar = driver.find_element(By.XPATH, botonContinuar_2)
                continuar.click()
                print('Ancillaries: Ok')
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, tipoTarjeta)))
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            finally:
                print('Fin funcion scroll')
            
            #Pago
            try:
                localizar = driver.find_element(By.XPATH,'//*[@id="bonusCollapse"]/div/div/div/button').location_once_scrolled_into_view
                time.sleep(2)
                tipo_tarjeta = driver.find_element(By.XPATH,tipoTarjeta)
                tipo_tarjeta.click()
                tarjeta_visa = driver.find_element(By.XPATH,tarjetaVisa)
                tarjeta_visa.click()
                time.sleep(2)
                numero_tarjeta = driver.find_element(By.XPATH, numeroTarjetaFrame)     # Revisar
                driver.switch_to.frame(numero_tarjeta)
                numero_tarjeta = driver.find_element(By.XPATH, numeroTarjeta)
                numero_tarjeta.send_keys('4012999999999999')
                driver.switch_to.parent_frame()
                nombre_titular = driver.find_element(By.XPATH, nombreTitular)
                nombre_titular.send_keys('adulto')
                apellido_titular = driver.find_element(By.XPATH, apellidoTitular)
                apellido_titular.send_keys('test')
                tarjeta_mes = driver.find_element(By.XPATH, tarjetaMes)
                tarjeta_mes.click()
                tarjeta_mes_numero= driver.find_element(By.XPATH, tarjetaMesNumero)
                tarjeta_mes_numero.click()
                tarjeta_anyo = driver.find_element(By.XPATH, tarjetaAnyo)
                tarjeta_anyo.click()
                tarjeta_anyo_2 = driver.find_element(By.XPATH, tarjetaAnyo_2)
                tarjeta_anyo_2.click()
                cvv = driver.find_element(By.XPATH, cvvFrame)
                driver.switch_to.frame(cvv)
                cvv = driver.find_element(By.XPATH, cvv)
                cvv.send_keys('123')
                driver.switch_to.parent_frame()
                try:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # scroll
                    time.sleep(2)
                except Exception as e:
                    print(f'Ha ocurrido un error: {e}')

                terminos = driver.find_element(By.XPATH, '//*[@id="pmt-breakdown"]/fieldset/section/div[1]/div[1]/label')
                terminos.click()
                time.sleep(1)
                aceptar_pagar = driver.find_element(By.ID, 'pmt-total-price-pay-btn')
                aceptar_pagar.click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, )))   #revisar
                time.sleep(3)

            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            finally:
                print('Fin del Proceso')

        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('Proceso completado')


    def test_comfirmar_vuelo(self):
        """"
        try:
            driver = self.driver
            driver.execute_script("window.open(' ');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(iberia_pree)
            gestion_reserva = driver.find_element(By.XPATH, gestionReserva)
            gestion_reserva.click()

            time.sleep(200)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        """


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()