import logging
import csv
import os.path
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*

class NALP(unittest.TestCase):
    def setUp(self):
        try:
            logging.basicConfig(filename='log/'+'NALP'+'_log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:NALP")
            logging.info("Test_description: Llegar a la NALP")
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
            Home_search_flight.depart_date(self.driver, 35)
            Home_search_flight.return_date(self.driver, 45)
            Home_search_flight.open_pass(self.driver)
            Home_search_flight.add_passengers(self.driver, 2, 0, 0)
            Home_search_flight.click_search(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def select_flight(self):
        try:
            Availability.ocultar_info(self.driver)
            Availability.results_ida(self.driver, 'Turista',0, 'IB') # 0 Para basica- 1 para optima- IB-Iberia-BA-British
            Availability.results_vuelta(self.driver,'Turista', 0, 'IB') # 0 Para clase turista- 1 para Business- IB-Iberia-BA-British
            Availability.continuar(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def rellenar_datos(self):
        try:
            Datos_pasajeros.cont_vuelo(self.driver)
            Datos_pasajeros.two_adults_passenger_data(self.driver)
            # Datos_pasajeros.cont_vuelo(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def ancillaries(self):
        Ancillaries.close_banners(self.driver)

    def test_NALP(self):
        self.param_search() #Función q indica los parámetros de búsqueda de vuelo
        self.select_flight()
        self.rellenar_datos()
        self.ancillaries()
        time.sleep(500000)

if __name__ == '__main__':
    unittest.main()