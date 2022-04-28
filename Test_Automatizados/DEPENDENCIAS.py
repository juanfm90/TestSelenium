
"""
Esta clase contiene todas las rutas html
que estan asociadas a variables
"""
# -----SET UP-----
chromedriver = r'D:/Iberia_Automatica/chromedriver/chromedriver.exe'
iberia_pree = 'https://pree.iberia.es'

# -----Excel-----
filepath = "Variables.xlsx"

# -----HOME ID-----
origen1 = 'flight_origin1' #id (ciudad origen)
destino1 = 'flight_destiny1' #id (ciudad destino)
fechaIda = 'flight_round_date1' #id (fecha ida)
fechaVuelta = 'flight_return_date1' #id
botonBuscar = 'buttonSubmit1' #id
explicitWai = 'header-commons-iberia-logo-home-link' #id

# -----HOME XPATH-----
origen1_xpath = '//input[@id="flight_origin1"]' #xpath (ciudad origen)
destino1_xpath = '//*[@id="flight_destiny1"]' #xpath (ciudad destino)
aceptar_cookies = '//*[@id="onetrust-accept-btn-handler"]' #xpath (sólo en PROD)
botonRutas = '//*[@id="ticketops-seeker-button"]/span[1]' #xpath (selector ida-idavuelta-multiples)
idaVuelta = '//*[@id="ticketops-seeker-menu"]/li[1]' #xpath
soloIda = '//*[@id="ticketops-seeker-menu"]/li[2]' #xpath
multiplesTrayectos = '//*[@id="ticketops-seeker-menu"]/li[3]' #xpath
fechaIda_xpath = '//input[@id="flight_round_date1"]' #xpath (fecha ida)
fechaVuelta_xpath = '//input[@id="flight_return_date1"]' #xpath (fecha vuelta)
botonBuscar_xpath = '//button[@id="buttonSubmit1"]' #xpath (botón buscar vuelos)
pasajeros_dropdown = '//*[@id="flight_passengers1"]' #xpath (desplegable para seleccionar adultos, niños, bebés)
add_adults = '//*[@id="people-counter-1"]/ul/li[2]/div[2]/button[2]' #xpath (botón + añadir adultos)
add_children = '//*[@id="people-counter-1"]/ul/li[5]/div[2]/button[2]' #xpath (botón + añadir niños)
add_babies = '//*[@id="people-counter-1"]/ul/li[6]/div[2]/button[2]' #xpath (botón + añadir bebés)
add_young = '//*[@id="people-counter-1"]/ul/li[4]/div[2]/button[2]' #xpath (botón + añadir young adult)


# -----AVAILABILITY ID-----

vueloTuristaIda = 'bbki-slice-info-cabin-0-0-E-btn' #id
vueloTuristaVuelta = 'bbki-slice-info-cabin-1-0-E-btn' #id
botonContinuar = 'AVAILABILITY_CONTINUE_BUTTON' #id

# -----AVAILABILITY XPATH-----
ocultarInfo = '/html/body/main/div[1]/ib-new-main-header/div[2]/div[1]/div/div/div/label[2]/div[3]' #xpath (info covid)
div_ida = '//*[@id="bbki-availability-trip-info"]/div[2]' #xpath (contenedor vuelos ida)
div_vuelos_ida_seleccionada = '//*[@id="selectedSlice-0"]' #xpath (div ida una vez seleccionado un vuelo)
div_vuelta = '//*[@id="bbki-availability-trip-info"]/div[2]' #xpath (contenedor vuelos vuelta)
div_vuelos_vuelta_seleccionada = '//*[@id="selectedSlice-1"]' #xpath (div vuelta una vez seleccionado un vuelo)

radios_tarifa_ida = 'ib-box-select-radio__radio' #classname (seleccionar tarifa del div anterior, q es el vuelo seleccionado)
radios_tarifa_vuelta = 'ib-box-select-radio__radio' #classname (seleccionar tarifa del div anterior, q es el vuelo seleccionado)


# -----DATOS PASAJEROS-----
numeroTelefono = 'IBAIRP_CONTACT_FORM_PHONE' #id

nombrePasajero = '//*[@id="name_0"]' #xpath
apellidoPasajero = '//*[@id="first_surname_0"]' #xpath
nombre2adulto = '//*[@id="name_1"]' #xpath
apellido2adulto = '//*[@id="first_surname_1"]'
contactoEmail = '//*[@id="IBAIRP_CONTACT_FORM_EMAIL"]' #xpath
repetirEmail = '//*[@id="IBAIRP_CONTACT_FORM_REPEATED_EMAIL"]' #xpath
tel_xpath = '//*[@id="IBAIRP_CONTACT_FORM_PHONE"]' #xpath
botonConsentimiento = '/html/body/main/div[2]/main/ib-ui-notice/div/div/button/span[2]' #xpath
boletinNoticias = '//*[@id="bbki-passenger-info-passengers-contact-form"]/fieldset/fieldset/div/div/div/div[2]/div/div[6]/label' #xpath

# -----ANCILLARIES-----
cerrarFlexibilidad = '/html/body/div[1]/div/div/div[1]/form/footer/button' #xpath
cerrarSeleccionAsientos  = '/html/body/div[1]/div/div/div[1]/header/div[1]/div/button' #xpath

add_baggage = '/html/body/main/div[2]/div[2]/div[2]/equal-height/div[2]/ib-baggages-box/div/section/div/div[2]/div[2]/div/button' #xpath
add_23kgida1 = '/html/body/div[1]/div/div/div/section/form/div/div[1]/div[2]/fieldset/div/div[1]/div[2]/div/div[1]/button[2]' #xpath
add_23kgvuelta1 = '/html/body/div[1]/div/div/div/section/form/div/div[1]/div[2]/fieldset/div/div[2]/div[2]/div/div[1]/button[2]' #xpath
add_23kgida2 = '/html/body/div[1]/div/div/div/section/form/div/div[2]/div[2]/fieldset/div/div[1]/div[2]/div/div[1]/button[2]' #xpath
add_23kgvuelta2 = '/html/body/div[1]/div/div/div/section/form/div/div[2]/div[2]/fieldset/div/div[2]/div[2]/div/div[1]/button[2]' #xpath
accept_bags = '/html/body/div[1]/div/div/div/section/form/footer/button' #xpath
add_flex = '//*[@id="anc-components-card-button-section"]/div/div/button' #xpath
flex_refund = '/html/body/div[1]/div/div/div/form/section/div/div[2]/div/fieldset/div[2]/div/div[1]/label/span[1]' #xpath
accept_flex = '/html/body/div[1]/div/div/div/form/footer/button' #xpath

# -----PAGOS-----
paisEmision = ''
tipoTarjeta = '//*[@id="pmt-gcc-fields-card-type-cmb-box"]/div[1]/span/span[1]' #xpath
tarjetaVisa = '//*[@id="ui-select-choices-row-3-0"]/span/span' #xpath
probarClick = '//*[@id="pmt-nav-tab-credit-card-tab"]/fieldset' #xpath
numeroTarjeta = 'creditCardNumberIbPay' #ID
nombreTitular = '//*[@id="name"]' #xpath
apellidoTitular = '//*[@id="surnames"]' #xpath
tarjetaMes = '//*[@id="EXPIRY_DATE"]/div[1]/div[1]/span/span[1]' #xpath
tarjetaDia = '//*[@id="EXPIRY_DATE"]/div[2]/div[1]/span/span[1]' #xpath
aceptar_term = '//*[@id="pmt-breakdown"]/fieldset/section/div[1]/div[1]/label' #xpath
pagar = '//*[@id="pmt-total-price-pay-btn"]' #xpath
pnr = '/html/body/main/div[2]/main/div[1]/equal-height[1]/div/div/div/div/div[1]/div/div/span' #xpath

# -----MMB-----
tus_vuelos = '/html/body/nav/div/div[1]/ul/li[2]/a/span' #xpath (para hacer hover en "tus vuelos)
MMB_btn = '/html/body/nav/div/div[1]/ul/li[2]/div/div/ul/li[3]/ul/li[2]/a/span' #xpath para abrir MMB
apellido_mmb = '//*[@id="ANONYMOUS_LOGIN_INPUT_SURNAME"]' #xpath apellido para recuperar reserva
pnr_mmb = '//*[@id="ANONYMOUS_LOGIN_INPUT_PNR"]' #xpath pnr para recuperar reserva
bnt_cont_mmb = '//*[@id="ANONYMOUS_LOGIN_BOTON"]' #xpath botón continuar


# -----GESTOR DE BONOS-----
user_bonos = '//*[@id="username"]'
password_bonos = '//*[@id="password"]'
boton_login_bonos = '/html/body/form/div/div/div/div[2]/input[2]'

pestaña_campaña = '/html/body/header/div/nav/div[2]/div/ul/li[3]/a'