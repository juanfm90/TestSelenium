
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


# -----TARJETAS REGALO-----
viaja = '/html/body/nav/div/div[1]/ul/li[1]/a/span' #xpath (para hacer hover en "viaja)
tarjetas_regalo = '/html/body/nav/div/div[1]/ul/li[1]/div/div/ul/li[4]/ul/li[2]/a/span' #xpath (para acceder al portal de TR)
compra_TR = '/html/body/main/section/article[1]/div/div/div/div/div/div/div/div/div/div/div[1]/a[1]' #xpath para acceder al flujo de compra TR

tr_primeros = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/fieldset/div/div/div[2]/div/div/label' #xpath selecciona tarjeta para uno mismo
tr_terceros = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/fieldset/div/div/div[1]/div/div/label' #xpath selecciona tarjeta regalo para terceros

importe_50_bk  = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[1]/div' #xpath selecciona importe 1 (50€)
importe_100_bk = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[2]/div' #xpath selecciona importe 1 (100€)
importe_300_bk = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[3]/div' #xpath selecciona importe 1 (300€)
importe_500_bk = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[4]/div' #xpath selecciona importe 1 (500€)

importe_50 = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[1]/div/div/label/span' #xpath selecciona importe 1 (50€)
importe_100 = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[2]/div/div/label/span' #xpath selecciona importe 1 (100€)
importe_300 = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[3]/div/div/label/span' #xpath selecciona importe 1 (300€)
importe_500 = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-import/fieldset/div[2]/div/div[1]/div/div[4]/div/div/label/span' #xpath selecciona importe 1 (500€)

otro_importe = '//*[@id="customAmount"]'

email_receptor_primeros = '//*[@id="shippingSenderMine"]' #xpath email para el envio del codigo en compra para uno mismo

nombre_receptor_terceros = '//*[@id="receiverName"]' #xpath nombre de receptor TR a terceros
nombre_remitente = '//*[@id="receiverRenderName"]' #xpath nombre del comprador TR a terceros
mensaje_personalizado = '//*[@id="receiverMessage"]' #xpath mensaje de la tarjeta regalo
email_receptor_terceros = '//*[@id="shippingEmailReceiver"]'  #xpath email de receptor TR a terceros
email_remitente = '//*[@id="shippingEmailRender"]' #xpath email del comprador TR a terceros
check_envio_remitente = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/ib-gift-cards-shipping-info/fieldset[1]/div[2]' #xpath selecciona el envio de la TR al comprador
email_recepcion_remitente = '//*[@id="shippingSenderRender"]' #xpath email del comprador TR (de nuevo)

ir_al_pago = '/html/body/main/div/ib-gift-cards-configuration/div/div/ib-gift-cards-configuration-form/div/div/section/div/form/div[2]/div[1]/button' #xpath Boton para continuar al pago
aceptar_condiciones = '/html/body/div[1]/div/div/footer/button'

confirmacion_compra = '/html/body/main/div/main/div/div[1]/div/div/h1/span[2]'

# -----GESTOR DE BONOS-----
gestor_bonos = 'https://acceso.pre.iberia.es/oam/server/obrareq.cgi?encquery%3DjyRfgFhEW2IdOS5OKFGs1B0pDazHGYl%2FKSif7ytvy42Y%2F1nL%2F5d9COgQ6ZvdER3VTPM%2FZvCapQz546PMUT1MM0jqqpiGttR1%2B2n%2B1%2B3Oli9byjd1hEzR42ZDczbn7AIWUYdGlws%2B4%2BtC%2BkmzB1PODid5SgXtwVrDHzlMR5iYalt%2FLQ2caZCOMrMcBPXAaR6WGOoUaeX93mS2AJVFxgNoitqkr8l%2B0KGlj26KbhckgU9tXYOh7t91c8cBY9zJVAmO7dENsg56n583v1QnJ2P6dnIin1HHazGh7uT20pZZFDyiNGYTaZIZupkA%2FRGyfWZTmmZzzxri389ECXDG1HVn3k6sFbCquk3ENfEEYDBCUDo%3D%20agentid%3DPortalpre11g_wg%20ver%3D1%20crmethod%3D2'
user_bonos = '//*[@id="username"]'
password_bonos = '//*[@id="password"]'
boton_login_bonos = '/html/body/form/div/div/div/div[2]/input[2]'

pestaña_campaña = '/html/body/header/div/nav/div[2]/div/ul/li[3]/a'
boton_campaña = '/html/body/div[1]/div[2]/div/a'
codigo_campaña = '//*[@id="codigoCampanya"]'
campaña_centro_presupuestario = '//*[@id="centroPresupuestario"]'
campaña_cuenta_contable = '//*[@id="cuentaContable"]'
campaña_motivo = '//*[@id="motivo"]'
campaña_submotivo = '//*[@id="submotivo"]'
campaña_bp = '/html/body/div[1]/form/div[2]/div[2]/div[2]/div[1]/div/ul/li[1]/a'
campaña_bf = '/html/body/div[1]/form/div[2]/div[2]/div[2]/div[1]/div/ul/li[2]/a'
campaña_tr = '/html/body/div[1]/form/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/a'
campaña_cantidad_porcentual = '//*[@id="cantidadPorcentual"]'
campaña_cantidad_fija = '//*[@id="cantidadFija"]'
campaña_cantidad_marketing = '//*[@id="cantidadFijaMarketing"]'
campaña_cantidad_fija_tr = '//*[@id="cantidadTarjetaRegalo"]'
campaña_cantidad_marketing_tr = '//*[@id="cantidadTarjetaRegaloMarketing"]'
campaña_moneda = '//*[@id="moneda"]'
campaña_moneda_tr = '//*[@id="monedaTarjetaRegalo"]'
campaña_numero_usos = '//*[@id="numUsos"]'
campaña_boton_guardar = '//*[@id="buttonCargar"]'
campaña_boton_final = '//*[@id="buttonCampanyaForm"]'
campaña_creacion_confirmacion = '/html/body/div[1]/div[2]'

pestaña_bono = '/html/body/header/div/nav/div[2]/div/ul/li[4]/a'
bono_codigo_aleatorio = '/html/body/div[1]/form/div[2]/div[1]/div[2]/div/div/div[2]/label[3]'
bono_numero_bonos = '//*[@id="numeroBono"]'
bono_campaña = '//*[@id="idCampanya"]'
bono_boton_final = '/html/body/div[1]/form/div[4]/div/div/div[3]/button[1]'
bono_creacion_confirmacion = '//*[@id="message-success"]'

pestaña_busqueda = '/html/body/header/div/nav/div[2]/div/ul/li[1]/a'
buscar_bono ='/html/body/div[1]/form/div[1]/div/div/label[1]'
buscar_campaña = '/html/body/div[1]/form/div[1]/div/div/label[2]'
buscar_signos_bono = '//*[@id="desplegableSignosCodigoBono"]'
buscar_codigo_bono = '//*[@id="campoCodigoBono"]'
buscar_tipo_codigo_bono = '//*[@id="desplegableCodigoBono"]'
buscar_boton_buscar = '/html/body/div[1]/form/div[4]/div[2]/div/button'
buscar_id_bono = '/html/body/div[1]/div[2]/form/div/div/div/table/tbody/tr/td[2]'
buscar_editar_bono_tr = '/html/body/div[1]/div[2]/form/div/div/div/table/tbody/tr/td[10]/a[2]'
buscar_editar_bono_bp = '/html/body/div[1]/div[2]/form/div/div/div/table/tbody/tr[1]/td[10]/a[3]'

ventana_editar = '//*[@id="editBonoForm"]'
ventana_editar_tipo_bono = '/html/body/div[1]/form/div[2]/div[2]/div[2]/div[3]/div/ul/li/a'
edicion_texto_comentario = '//*[@id="textoComentarioCrear"]'
edicion_guardar_comentario = '//*[@id="botonCrearComentario"]'