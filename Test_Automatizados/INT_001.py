import logging
import csv
import os.path
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*
from datetime import datetime
from capture import capture


class INT_001(unittest.TestCase):
    def setUp(self):
        try:
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d")
            logging.basicConfig(filename='log/'+'INT_001'+'_log_'+dt_string, filemode='w', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:INT_001 - integrity_PREE")
            logging.info("Test_description: Comprobar estado de ancillaries en PREE")
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

    def param_search(self):
        try:
            # Home_search_flight.cookies(self.driver)
            Home_search_flight.depart_location(self.driver, 'Madrid')
            Home_search_flight.dest_location(self.driver, 'Bilbao')
            Home_search_flight.depart_date(self.driver, 65)
            Home_search_flight.return_date(self.driver, 65)
            Home_search_flight.open_pass(self.driver)
            Home_search_flight.add_passengers(self.driver, 2, 0, 0)
            # Flight info capture:
            capture.capture_screen(self.driver,"screenshots","INT_001_1_flightinfo")
            Home_search_flight.click_search(self.driver)
        except Exception as e:
            print(f'Error in param_search: {e}')
            capture.capture_screen(self.driver,"screenshots","INT_001_1_ERROR_param_search")
            logging.error('Error in param_search: {e}')

    def select_flight(self):
        try:
            Availability.ocultar_info(self.driver)
            Availability.results_ida(self.driver, 'Turista',0, 'IB') # 0 Para basica- 1 para optima- IB-Iberia-BA-British
            # Captura ida
            capture.capture_screen(self.driver,"screenshots","INT_001_1_ida")
            Availability.results_vuelta(self.driver,'Turista', 0, 'IB') # 0 Para clase turista- 1 para Business- IB-Iberia-BA-British
            # Captura vuelta
            capture.capture_screen(self.driver,"screenshots","INT_001_1_vuelta")
            Availability.continuar(self.driver)
        except Exception as e:
            print(f'Error in select_flight: {e}')
            capture.capture_screen(self.driver,"screenshots","INT_001_1_ERROR_select_flight")
            logging.error('Error in select_flight: {e}')

    def rellenar_datos(self):
        try:
            Datos_pasajeros.cont_vuelo(self.driver)
            Datos_pasajeros.two_adults_passenger_data(self.driver)
            # Datos_pasajeros.cont_vuelo(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
            capture.capture_screen(self.driver,"screenshots","INT_001_1_ERROR_rellenar_datos")
            logging.error('Error in rellenar_datos: {e}')

    def checkancillariesstatus(self):
        
        if(Ancillaries.is_bag_available(self.driver)): logging.info("ANC_BAG_OK")
        else: logging.info("ANC_BAG_KO")
        #logging.info(self.driver.page_source)
        if(Ancillaries.is_seat_available(self.driver)): logging.info("ANC_SEAT_OK")
        else: logging.info("ANC_SEAT_KO")

    def test_INT_001(self):
        self.param_search() #Función q indica los parámetros de búsqueda de vuelo
        self.select_flight()
        self.rellenar_datos()

        # Capture of NALP
        #capture.capture_screen(self.driver,"screenshots","INT_001_1_NALP")

	# Check if bagg is available
        self.checkancillariesstatus()

        time.sleep(10)

if __name__ == '__main__':
    unittest.main()
