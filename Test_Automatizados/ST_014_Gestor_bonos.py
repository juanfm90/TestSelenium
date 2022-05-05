import logging
import csv
import os.path
import time

from Home_search_flight import*
from Availability import*
from Datos_pasajeros import*
from Ancillaries import*
from Pagos import*
import random
import re
from datetime import datetime

#from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager

class Gestor_de_bonos(unittest.TestCase):

    def setUp(self):
        try:
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d")
            logging.basicConfig(filename='log/'+'Sanity_014_log_Gestor_Bonos', filemode='w', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            #logging.basicConfig(filename='log/'+'Gestor_Bonos'+'_log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] [%(levelname)-8s] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            logging.info("Test_Name:Gestor_Bonos")
            logging.info("Test_description: Gestion generacion de bonos")
        except Exception as e:
            print(f'Error configurando logger: {e}')

        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver = self.driver
            driver.get('https://webpre.corp.iberia.es/gestorbonos')
            driver.maximize_window()
            time.sleep(3)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        finally:
            print('webdriver: Ok')

    def login_gestor(self):
        logging.info("==Gestor_bonos.login_gestor==")
        try:
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, user_bonos)))
            user = self.driver.find_element(By.XPATH, user_bonos) # Selecciona campo para introducir usuario
            time.sleep(0.5)
            user.send_keys('386363') # Introduce usuario (ADMIN)

            password = self.driver.find_element(By.XPATH, password_bonos) # Selecciona campo para introducir password
            time.sleep(0.5)
            password.send_keys('Bonos2022Bonos') # Introduce password
            time.sleep(2)
            loggin = self.driver.find_element(By.XPATH, boton_login_bonos) # Selecciona boton para loggin
            loggin.click() # Selecciona Loggin

        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def crear_campaña(self):
        logging.info("==Gestor_bonos.crear_campana==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, pestaña_campaña)))
        campaña = self.driver.find_element(By.XPATH, pestaña_campaña)  # Selecciona la pestaña para acceder a la campaña
        campaña.click()  # Selecciona campaña

        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, boton_campaña)))
        crear_campaña = self.driver.find_element(By.XPATH, boton_campaña)  # Selecciona boton para crear la campaña
        crear_campaña.click()  # Selecciona crear nueva campaña



    def configuracion_campaña (self):
        logging.info("==Gestor_bonos.configuracion_campana==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, codigo_campaña)))
        codigo = self.driver.find_element(By.XPATH, codigo_campaña)  # Selecciona el campo del codigo
        time.sleep(0.5)
        global random_code
        random_code = random.randint(100000000, 999999999) # genera un numero aleatorio para el codigo de campaña
        codigo.send_keys(random_code) # introduce codigo

        time.sleep(0.5)
        centro_presupuestario = self.driver.find_element(By.XPATH, campaña_centro_presupuestario)
        time.sleep(0.5)
        centro_presupuestario.send_keys('u') #Selecciona centro presupuestario (letra inicial)

        cuenta_contable = self.driver.find_element(By.XPATH, campaña_cuenta_contable)
        time.sleep(0.5)
        cuenta_contable.send_keys('u') #Selecciona cuenta contable (letra inicial)

        motivo = self.driver.find_element(By.XPATH, campaña_motivo) #Seleccion motivo
        time.sleep(0.5)
        motivo.send_keys('p') #Selecciona motivo (letra inicial)

        submotivo = self.driver.find_element(By.XPATH, campaña_submotivo) #Seleccion submotivo
        time.sleep(0.5)
        submotivo.send_keys('p') #Selecciona submotivo (letra inicial)
        time.sleep(0.5)
        F13 = Datos_pasajeros.read_bonos_campaña_tipo(self) #Recogemos tipo de bono referido en la campaña
        self.driver.execute_script("window.scrollTo(0, 370)") #Accedemos a campos con el scroll
        time.sleep(1)
        if (F13.value == "Bp"):
            tipo_campaña_bp = self.driver.find_element(By.XPATH, campaña_bp)
            tipo_campaña_bp.click()
            F15 = Datos_pasajeros.read_bonos_campaña_cantidad_porcentual(self)
            time.sleep(0.5)
            cantidad_bp = self.driver.find_element(By.XPATH, campaña_cantidad_porcentual)
            cantidad_bp.send_keys(F15.value)
            F17 = Datos_pasajeros.read_bonos_campaña_numero_usos(self)
            numero_usos_bp = self.driver.find_element(By.XPATH, campaña_numero_usos)
            numero_usos_bp.send_keys(F17.value)
        elif (F13.value == "Bf"):
            tipo_campaña_bf = self.driver.find_element(By.XPATH, campaña_bf)
            tipo_campaña_bf.click()
            F14 = Datos_pasajeros.read_bonos_campaña_cantidad_total(self)
            F16 = Datos_pasajeros.read_bonos_campaña_cantidad_marketing(self)
            time.sleep(0.5)
            cantidad_bf = self.driver.find_element(By.XPATH, campaña_cantidad_fija)
            cantidad_bf.send_keys(F14.value)
            time.sleep(0.5)
            cantidad_marketing_bf = self.driver.find_element(By.XPATH, campaña_cantidad_marketing)
            cantidad_marketing_bf.send_keys(F16.value)
            time.sleep(0.5)
            moneda_bf = self.driver.find_element(By.XPATH, campaña_moneda)
            moneda_bf.send_keys('e')
            time.sleep(0.5)
            F17 = Datos_pasajeros.read_bonos_campaña_numero_usos(self)
            numero_usos_bf = self.driver.find_element(By.XPATH, campaña_numero_usos)
            numero_usos_bf.send_keys(F17.value)
        elif (F13.value == "Tr"):
            tipo_campaña_tr = self.driver.find_element(By.XPATH, campaña_tr)
            tipo_campaña_tr.click()
            F14 = Datos_pasajeros.read_bonos_campaña_cantidad_total(self)
            F16 = Datos_pasajeros.read_bonos_campaña_cantidad_marketing(self)
            time.sleep(0.5)
            cantidad_tr = self.driver.find_element(By.XPATH, campaña_cantidad_fija_tr)
            cantidad_tr.send_keys(F14.value)
            time.sleep(0.5)
            cantidad_marketing_tr = self.driver.find_element(By.XPATH, campaña_cantidad_marketing_tr)
            cantidad_marketing_tr.send_keys(F16.value)
            time.sleep(0.5)
            moneda_tr = self.driver.find_element(By.XPATH, campaña_moneda_tr)
            moneda_tr.send_keys('e')
            time.sleep(0.5)

        time.sleep(3)
        guardar_campaña = self.driver.find_element(By.XPATH, campaña_boton_guardar)
        guardar_campaña.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1080)")
        time.sleep(1)
        final_campaña = self.driver.find_element(By.XPATH, campaña_boton_final)
        final_campaña.click()


    def comprobacion_creacion_campaña(self):
        logging.info("==Gestor_bonos.comprobacion_creacion_campana==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, campaña_creacion_confirmacion)))
        texto_confirmacion = self.driver.find_element(By.XPATH, campaña_creacion_confirmacion).text
        print("***************RESULTADOS**********************")
        if (texto_confirmacion == "La campaña ha sido creada correctamente"):
            print ("LA CAMPAÑA SE HA CREADO CORRECTAMENTE")
        else:
            print("ERROR EN LA CREACION DE LA CAMPAÑA")
        time.sleep(1)

    def acceso_creacion_bono(self):
        logging.info("==Gestor_bonos.acceso_creacion_bono==")
        bono = self.driver.find_element(By.XPATH, pestaña_bono)  # Selecciona la pestaña para acceder a la pestaña de bono
        bono.click()  # Selecciona bonos

        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, boton_campaña)))
        crear_campaña = self.driver.find_element(By.XPATH, boton_campaña)  # Selecciona boton para crear el bono
        crear_campaña.click()  # Selecciona crear nuevo bono

    def configuracion_bono(self):
        logging.info("==Gestor_bonos.configuracion_bono==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, bono_codigo_aleatorio)))
        codigo_aleatorio = self.driver.find_element(By.XPATH, bono_codigo_aleatorio)  # Selecciona boton para crear el bono
        codigo_aleatorio.click()  # Selecciona crear nuevo bono

        time.sleep(0.5)
        numero_bonos = self.driver.find_element(By.XPATH, bono_numero_bonos)  # Selecciona el campo del numero de bonos a crear
        numero_bonos.send_keys('1') # Introrduce numero de bonos

        time.sleep(0.5)
        self.driver.execute_script("window.scrollTo(0, 400)") #baja la ventana un tercio para ver los campos
        seleccion_campaña = self.driver.find_element(By.XPATH, bono_campaña)  # Selecciona la campaña asociada al bono
        seleccion_campaña.send_keys(random_code) #introduce codigo de la campaña previamente creada
        time.sleep(1)

        guardar_bono = self.driver.find_element(By.XPATH, campaña_boton_guardar) #Selecciona boton para guardar y accede a la vista previa
        guardar_bono.click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 1080)") #baja la ventana hasta abajo para acceder al boton de creacion
        time.sleep(1)
        final_bono = self.driver.find_element(By.XPATH, bono_boton_final) #Confirma la creacion del bono
        final_bono.click()
        time.sleep(2)

    def comprobacion_creacion_bono(self):
        logging.info("==Gestor_bonos.comprobacion_creacion_bono==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, bono_creacion_confirmacion))) # espera a la pestaña de bonos general
        texto_confirmacion = self.driver.find_element(By.XPATH, bono_creacion_confirmacion).text #Recoge el mensaje de confirmacion

        print("*****************************************")
        print(texto_confirmacion)
        time.sleep(1)

    def busqueda_bono(self):
        logging.info("==Gestor_bonos.busqueda_bono==")
        acceso_busqueda = self.driver.find_element(By.XPATH, pestaña_busqueda) #Acceso a pestaña de busqueda
        acceso_busqueda.click()

        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, buscar_codigo_bono))) #espera carga de pestaña
        buscar_bono_por_campaña = self.driver.find_element(By.XPATH, buscar_tipo_codigo_bono) #pasamos a buscar por campaña los bonos
        buscar_bono_por_campaña.send_keys('c')
        time.sleep(1)
        codigo_busqueda = self.driver.find_element(By.XPATH, buscar_codigo_bono)
        codigo_busqueda.send_keys(random_code) #Introducimos el codigo de la campaña previamente creada
        #codigo_busqueda.send_keys(285451328)
        time.sleep(1)
        lanzar_busqueda = self.driver.find_element(By.XPATH, buscar_boton_buscar) #lanza la busqueda
        lanzar_busqueda.click()

        time.sleep(1)
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, buscar_id_bono)))
        id_bono = self.driver.find_element(By.XPATH, buscar_id_bono).text #Seleccionamos el Id del bono para obtener su codigo XPATH unico
        global path_codigo
        path_codigo = '//*[@id="'+id_bono+'BonoCC"]' #Codigo XPATH del primer bono de la lista
        codigo_del_bono = self.driver.find_element(By.XPATH, path_codigo)
        codigo_del_bono.click() #Click en el codigo bono para que este se desofusque
        time.sleep(2)

        F13 = Datos_pasajeros.read_bonos_campaña_tipo(self)
        if (F13.value == "Bp" or F13.value == "Bf") :
            editar_bp = self.driver.find_element(By.XPATH, buscar_editar_bono_bp) #Acceso a edicion de Bf o Bp
            editar_bp.click()
        elif (F13.value == 'Tr'):
            editar_tr = self.driver.find_element(By.XPATH, buscar_editar_bono_tr) #Acceso a edicion de Tr
            editar_tr.click()

    def editar_bono(self):
        logging.info("==Gestor_bonos.editar_bono==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, ventana_editar))) #Esperamos carga de pestaña edicion

        codigo_del_bono = self.driver.find_element(By.XPATH, path_codigo) #Click en el codigo bono para que este se desofusque
        codigo_del_bono.click()
        time.sleep(2)

        tipo_de_bono = self.driver.find_element(By.XPATH, ventana_editar_tipo_bono).text #En funcion del tipo de bono a editar se permite la modificacion de diferentes parametros
        self.driver.execute_script("window.scrollTo(0, 400)") #Bajamos a los campos editables
        if (tipo_de_bono == "Bono Porcentual"):
            edicion_porcentual = self.driver.find_element(By.XPATH, campaña_cantidad_porcentual) #Edicion cantidad porcentual
            F20 = Datos_pasajeros.read_bonos_edicion_cantidad_porcentual(self)
            edicion_porcentual.clear()
            edicion_porcentual.send_keys(F20.value)
            time.sleep(0.5)
            edicion_num_usos_bp = self.driver.find_element(By.XPATH, campaña_numero_usos)  #Edicion numero de usos
            F23 = Datos_pasajeros.read_bonos_edicion_numero_usos(self)
            edicion_num_usos_bp.clear()
            edicion_num_usos_bp.send_keys(F23.value)
        elif (tipo_de_bono == "Bono fijo"):
            edicion_total = self.driver.find_element(By.XPATH, campaña_cantidad_fija)  #Edicion cantidad total
            F21 = Datos_pasajeros.read_bonos_edicion_cantidad_total(self)
            edicion_total.clear()
            edicion_total.send_keys(F21.value)
            time.sleep(0.5)
            edicion_marketing = self.driver.find_element(By.XPATH, campaña_cantidad_marketing)  #Edicion cantidad marketing
            F22 = Datos_pasajeros.read_bonos_edicion_cantidad_total(self)
            edicion_marketing.clear()
            edicion_marketing.send_keys(F22.value)
            time.sleep(0.5)
            edicion_num_usos = self.driver.find_element(By.XPATH, campaña_numero_usos)  #Edicion numero de usos
            F23 = Datos_pasajeros.read_bonos_edicion_numero_usos(self)
            edicion_num_usos.clear()
            edicion_num_usos.send_keys(F23.value)
        elif (tipo_de_bono == "Tarjeta regalo"):
            edicion_total_tr = self.driver.find_element(By.XPATH, campaña_cantidad_fija_tr) # #Edicion cantidad total
            F21 = Datos_pasajeros.read_bonos_edicion_cantidad_total(self)
            edicion_total_tr.clear()
            edicion_total_tr.send_keys(F21.value)
            time.sleep(0.5)
            edicion_marketing_tr = self.driver.find_element(By.XPATH, campaña_cantidad_marketing_tr) #Edicion cantidad marketing
            F22 = Datos_pasajeros.read_bonos_edicion_cantidad_marketing(self)
            edicion_marketing_tr.clear()
            edicion_marketing_tr.send_keys(F22.value)

        time.sleep(2)
        vista_previa_edicion = self.driver.find_element(By.XPATH, campaña_boton_guardar) #Guarda y accede a vista previa
        vista_previa_edicion.click()

        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, bono_boton_final))) #Confirma cambios
        guardar_edicion = self.driver.find_element(By.XPATH, bono_boton_final)
        guardar_edicion.click()

        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, edicion_texto_comentario))) #Solitud de comentario
        texto_comentario = self.driver.find_element(By.XPATH, edicion_texto_comentario)
        date = datetime.now()
        fecha = date.strftime("%m/%d/%Y, %H:%M:%S") #Creacion de fecha en formato string
        comentario_añadir = 'Esta modificacion corresponte a las pruebas automaticas con fecha '+fecha+'.'
        texto_comentario.send_keys(comentario_añadir) #Introduccion de comentario

        time.sleep(2)
        guardar_comentario = self.driver.find_element(By.XPATH, edicion_guardar_comentario) #Comentario guardado
        guardar_comentario.click()

    def comprobacion_edicion_bono(self):
        logging.info("==Gestor_bonos.comprobacion_edicion_bono==")
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, bono_creacion_confirmacion))) #Esperamos ventana de busqueda
        texto_confirmacion_edicion = self.driver.find_element(By.XPATH, bono_creacion_confirmacion).text #Obtencion de mensaje de confirmacion de la edicion
        time.sleep(2)
        print("*****************************************")
        if (texto_confirmacion_edicion == "El bono ha sido modificado correctamente"):
            print("EL BONO SE HA MODIFICADO CORRECTAMENTE")
            logging.info("EL BONO SE HA MODIFICADO CORRECTAMENTE. ST_014_Gestor_bonos_OK")
        else:
            print("SE HA PRODUCIDO UN ERROR EN LA MODIFICACION DEL BONO")
            logging.error("SE HA PRODUCIDO UN ERROR EN LA MODIFICACION DEL BONO. ST_014_Gestor_bonos_KO")
        print("*****************************************")
        time.sleep(1)
        
        
        
    def test_gestor_bonos(self):
        self.login_gestor() #Funcion que realiza el login en el gestor
        self.crear_campaña() #Accede a la pestaña de campaña
        self.configuracion_campaña() #Configura los detalles de la campaña
        self.comprobacion_creacion_campaña()
        self.acceso_creacion_bono()#Accede a la pestaña de bono
        self.configuracion_bono() #Configura los detalles del bono
        self.comprobacion_creacion_bono() #Comprueba creacion del bono
        self.busqueda_bono()#Busca bono creado
        self.editar_bono()#Edita el bono creado previamente
        self.comprobacion_edicion_bono()#Comprueba la edicion del bono




if __name__ == '__main__':
    unittest.main()