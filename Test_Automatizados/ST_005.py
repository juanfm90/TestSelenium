import logging
from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*

class ST_005(unittest.TestCase):
    def setUp(self):
        try:
            logging.basicConfig(filename='log/'+'ST_005'+'_log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:ST_005")
            logging.info("Test_description: ST_005 BKI MAD-MLN")
        except Exception as e:
            print(f'Error configurando logger: {e}')

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver = self.driver
            # driver.get("https://preb.iberia.es/nl/?language=nl")  # url value from excel
            driver.get('https://pree.iberia.es/nl/?language=en')
            driver.delete_all_cookies()
            driver.maximize_window()
            time.sleep(5)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('webdriver: Ok')

    def param_search(self):
        try:
            # Pagos.write_excel_file(self.driver)
            Home_search_flight.depart_location(self.driver, 'Madrid')
            Home_search_flight.dest_location(self.driver, 'Melilla')
            # Home_search_flight.depart_date(self.driver, 75)
            # Home_search_flight.return_date(self.driver, 125)
            Home_search_flight.depart_date_format(self.driver, 77)
            Home_search_flight.return_date_format(self.driver, 103)
            Home_search_flight.open_pass(self.driver)
            Home_search_flight.add_passengers(self.driver, 2, 0, 0)
            Home_search_flight.click_search(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def select_flight(self):
        try:
            Availability.ocultar_info(self.driver)
            Availability.vuelos_ida(self.driver, 'Turista', 2, 'YW')
            Availability.vuelos_vuelta(self.driver, 'Turista', 2, 'YW')
            # Availability.results_ida(self.driver, 'Turista', 2, 'YW') # 0 Para tarifa basic - 1 para optima etc- IB-Iberia-BA-British
            # Availability.results_vuelta(self.driver, 'Turista', 2, 'YW') # 0 Para clase turista- 1 para Business- IB-Iberia-BA-British
            Availability.continuar(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def rellenar_datos(self):
        try:
            # Datos_pasajeros.cont_vuelo(self.driver)
            Datos_pasajeros.two_adults_passenger_data(self.driver)
            # Datos_pasajeros.cont_vuelo(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def ancillaries(self):
        try:
            Ancillaries.add_insurance_NL(self.driver)
            Ancillaries.MAD_MLN_2adults_x_bags(self.driver, 8)
            Ancillaries.add_seats_2adults_confort_RT(self.driver)
            Ancillaries.delete_bags_from_basket(self.driver)
            Ancillaries.MAD_MLN_2adults_x_bags(self.driver, 9)

            Ancillaries.continuar(self.driver)
        except:
            print('No se ha podido añadir maletas')

    def pagos(self):
        # Pagos.select_visa(self.driver)
        try:
            Pagos.select_visa_seguro(self.driver)
            Pagos.pagar(self.driver)
            Pagos.get_pnr(self.driver)
            Pagos.write_excel_file(self.driver, 'C5')
        except:
            print('ERROR')




    def test_ST_005(self):
        self.param_search() #Función q indica los parámetros de búsqueda de vuelo
        self.select_flight()
        self.rellenar_datos()
        self.ancillaries()
        self.pagos()
        time.sleep(10000)

if __name__ == '__main__':
    unittest.main()