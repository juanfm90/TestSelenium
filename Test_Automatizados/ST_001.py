import logging
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*

class ST_001(unittest.TestCase):

    def setUp(self):
        try:
            logging.basicConfig(filename='log/'+'ST_001'+'_log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:ST_001")
            logging.info("Test_description: ST_001 BKI MAD-SDQ")
        except Exception as e:
            print(f'Error configurando logger: {e}')

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver = self.driver
            driver.get("https://pree.iberia.es")
            # driver.get("https://preb.iberia.es")
            driver.delete_all_cookies()
            driver.maximize_window()
            time.sleep(5)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('webdriver: Ok')

    def param_search(self):
        try:
            Home_search_flight.depart_location(self.driver, 'Madrid')
            Home_search_flight.dest_location(self.driver, 'Santo Domingo')
            Home_search_flight.depart_date(self.driver, 55)
            Home_search_flight.return_date(self.driver, 65)
            Home_search_flight.open_pass(self.driver)
            Home_search_flight.add_passengers(self.driver, 2, 0, 0)
            Home_search_flight.click_search(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def select_flight(self):
        try:
            Availability.ocultar_info(self.driver)
            Availability.vuelos_ida(self.driver, 'Turista', 0, 'IB')
            Availability.vuelos_vuelta(self.driver, 'Turista', 0, 'IB')
            # Availability.results_ida(self.driver, 'Turista', 0, 'IB')
            # Availability.results_vuelta(self.driver, 'Turista', 0, 'IB')

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
        try:
            # Ancillaries.cont_vuelo(self.driver)
            # Ancillaries.close_banners(self.driver)
            # Ancillaries.close_seat(self.driver)
            Ancillaries.add_bags(self.driver)
            Ancillaries.add_flex(self.driver)
            Ancillaries.continuar(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def pagar_CC(self):
        try:
            Pagos.select_visa(self.driver)
            Pagos.pagar(self.driver)
            Pagos.get_pnr(self.driver)
            Pagos.write_excel_file(self.driver, 'C1')
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')


    def test_ST_001(self):
        self.param_search() #Función q indica los parámetros de búsqueda de vuelo
        self.select_flight()
        self.rellenar_datos()
        self.ancillaries()
        self.pagar_CC()
        time.sleep(1000)

if __name__ == '__main__':
    unittest.main()