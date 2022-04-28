import logging
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*

class ST_002(unittest.TestCase):

    def setUp(self):
        try:
            logging.basicConfig(filename='log/'+'ST_002'+'_log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:ST_012")
            logging.info("Test_description: ST_002 BKI Mercado GB BA No ofrece Anc")
        except Exception as e:
            print(f'Error configurando logger: {e}')

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver = self.driver
            # driver.get('https://pree.iberia.es')
            driver.get("https://pree.iberia.es/gb/?language=en")
            driver.delete_all_cookies()
            driver.maximize_window()
            time.sleep(5)
        except Exception as e:
            logging.error(f'Ha ocurrido un error al crear webdriver: {e}')
        finally:
            print('webdriver: Ok')

    def param_search(self):
        try:
            Home_search_flight.depart_location(self.driver, 'Madrid')
            Home_search_flight.dest_location(self.driver, 'Lon')
            Home_search_flight.depart_date(self.driver, 60)
            Home_search_flight.return_date(self.driver, 75)
            Home_search_flight.open_pass(self.driver)
            Home_search_flight.add_passengers(self.driver, 1, 0, 0)
            Home_search_flight.click_search(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def select_flight(self):
        try:
            Availability.ocultar_info(self.driver)
            Availability.vuelos_ida(self.driver, 'Turista', 0, 'BA')
            # Availability.results_ida(self.driver, 'Turista', 0, 'BA')
            # Availability.results_vuelta(self.driver,'Turista', 0, 'BA')
            Availability.vuelos_vuelta(self.driver, 'Turista', 0, 'BA')
            Availability.continuar(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def rellenar_datos(self):
        try:
            Datos_pasajeros.cont_vuelo(self.driver)
            # Datos_pasajeros.oneadult_onechild_onebaby_passenger(self.driver)
            Datos_pasajeros.one_adult_passenger_data(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')


    def test_ST_002(self):
        self.param_search()
        self.select_flight()
        self.rellenar_datos()
        time.sleep(1000)

if __name__ == '__main__':
    unittest.main()