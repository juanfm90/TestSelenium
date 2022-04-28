from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*

class ST_003(unittest.TestCase):

    def setUp(self):
        try:
            # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver = webdriver.Chrome(ChromeDriverManager(version="99.0.4844.35").install())
            driver = self.driver
            driver.get("https://pree.iberia.es/it/?language=it")  # url value from excel
            driver.delete_all_cookies()
            driver.maximize_window()
            time.sleep(1)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('webdriver: Ok')

    def login_search(self):
        # Home_search_flight.login_PREB(self.driver)
        Home_search_flight.login(self.driver)
        Home_search_flight.one_way(self.driver)
        Home_search_flight.depart_location(self.driver, 'Madrid')
        Home_search_flight.dest_location(self.driver, 'Santo Domingo')
        Home_search_flight.depart_date(self.driver, 55)
        Home_search_flight.open_pass(self.driver)
        Home_search_flight.add_passengers(self.driver, 1, 1, 1)
        Home_search_flight.click_search(self.driver)

    def select_flight(self):
        try:
            Availability.ocultar_info(self.driver)
            Availability.vuelos_ida(self.driver, 'Turista', 0, 'IB')
            # Availability.results_ida(self.driver,'Turista', 0, 'IB')
            Availability.continuar(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def rellenar_datos(self):
        try:
            Datos_pasajeros.cont_vuelo(self.driver)
            Datos_pasajeros.oneadult_logado_onechild_onebaby_passenger(self.driver)
            # Datos_pasajeros.cont_vuelo(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def ancillaries(self):
        try:
            # Ancillaries.close_seat(self.driver)
            Ancillaries.add_x_bags(self.driver, 8)
            Ancillaries.add_insurance(self.driver)
            Ancillaries.delete_bags_from_basket(self.driver)
            Ancillaries.add_x_bags(self.driver, 9)
            Ancillaries.continuar(self.driver)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def borrar_maletas(self):
        Pagos.delete_bags_from_basket_and_return(self.driver)
        time.sleep(20)

    def maletas(self):
        Ancillaries.add_x_bags(self.driver, 9)
        # Ancillaries.add_insurance(self.driver)
        Ancillaries.continuar(self.driver)

    def pago(self):
        Pagos.select_card_FF(self.driver)
        # Pagos.select_visa(self.driver)
        Pagos.select_visa_seguro(self.driver)
        # Pagos.

    def test_ST_003(self):
        self.login_search()
        self.select_flight()
        self.rellenar_datos()
        self.ancillaries()
        # self.borrar_maletas()
        # self.maletas()
        self.pago()
        time.sleep(1000)



if __name__ == '__main__':
    unittest.main()