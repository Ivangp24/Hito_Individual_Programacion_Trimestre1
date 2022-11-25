import sys
class Informacion:
    print('----------!!!MÁRATULDA (BIENVENIDO) A INTERDIMENSION GALAXY TRUPAAC!!!-----------')
    print('''-Se ha adentrado a la gran tienda online más famosa del universo. Ubicada en la galaxia Andrómeda. Esta tienda vende productos galácticos de todo tipo:\n pistolas láser(Blaster), sables láser(colores a elegir), campos antigravedad, naves espaciales, pistola de portales...''') 

class Registro:
    cuenta=input('-Si posee ya un Usuario creado en nuestra página escriba "si": ').lower()
    if cuenta =='si':
        def __init__(self) -> None:
            self.nombreusuario=input('Nombre de Usuario(lenguaje terrícola): ')
            self.email=input('Email de Usuario: ')
            self.contraseña=input('Contraeña(lenguaje terrícola): ')
            self.numerotelefono=input('Número de receptor móvil planetario(número telefónico): ')
            self.planeta=input('Planeta en el que habita: ')
        def confirmacion(self):
            androide=input('MMMM... NO NOS FIAMOS DE QUE PUEDA SER UN ANDROIDE DEL IMPERIO GALÁCTICO,\nQUE INTENTE SONSACARNOS INFORMACIÓN PARA ROBARNOS... \nESCRIBA LA PALABRA SECRETA PARA COMPLETAR EL REGISTRO\n ¿CUÁL ES LA FAMOSA EXPRESIÓN DICHA POR SELDON COUPER EN THE BIG BANG THEORY?("BAZINGA") ').lower()
            if androide=='bazinga':
                print(f'trruuuu seepp yuuuuucta traaaa {self.nombreusuario}(se ha iniciado sesión con el usuario {self.nombreusuario})')
            else:
                print('TRRRUUU PAARR CHIFTIIIK!!FUERA DE NUESTRO SISTEMA MALDITO ANDROIDE!!')
                sys.exit()
    else:
        def __init__(self) -> None:
            self.nombreusuario=input('Nombre de Usuario(lenguaje terrícola): ')
            self.email=input('Email de Usuario: ')
            self.contraseña=input('Contraeña(lenguaje terrícola): ')
            self.nombre=input('Nombre real: ')
            self.apellido=input('Apellidos reales: ')
            self.identificacion=input('Código de identidicación planetario(DNI/NIF- si eres terrícola): ')
            self.numerotelefono=input('Número de receptor móvil planetario(número telefónico): ')
            self.planeta=input('Planeta en el que habita: ')
            self.direccion=input('Domicilio planetario: ')
    
        def confirmacion(self):
            robot=input('MMMM... NO NOS FIAMOS DE QUE PUEDA SER UN ROBOT ASESINO,\nQUE INTENTE CAPTURARNOS Y ECHARNOS A LOS SARLACC... \nESCRIBA LA PALABRA SECRETA PARA COMPLETAR EL REGISTRO\n ¿QUE PARTE DEL CUERPO LES BRILLA A LA FAMOSA RAZA ALIENÍGENA DE ET?("DEDO") ').lower()
            if robot=='dedo':
                print(f'-brruuuur trraasp pirrtu traaaa {self.nombreusuario} tuuihuiii piuieyhyt gaaarr {self.planeta} tuuurrr piiij {self.email}\n (Se ha guardado el nombre de usuario {self.nombreusuario} del planeta {self.planeta} y correo intercomputacional planetario {self.email}) ')
                print(f'-trruuuu seepp yuuuuucta traaaa {self.nombreusuario}(se ha iniciado sesión con el usuario {self.nombreusuario})')
            else:
                print('TRRRUUU PAARR CHIFTIIIK!!FUERA DE NUESTRO SISTEMA MALDITO ROBOT!!')
                sys.exit()

alienigena1=Registro()
alienigena1.confirmacion()

class Compra(Registro):
    def lista(self):
        productos=['pistola de portales','espada laser','nave espacial','blaster','campo antigravedad','neuralizador','gema del infinito','androide','botas propulsoras espaciales','ojo bionico','galaxia de bolsillo','juego de realidad virtual']
        print('''Los productos que tenemos disponibles actualmente son:\n -Pistola de portales(industrias Rick Sánchez)\n -Espada laser(proveniente del Gran Templo Jedi: Coruscant)\n -Nave espacial (modelo X-Wing T-65B)\n -Blaster (DH-15)\n -Campo antigravedad (1009-X)\n -Neuralizador(proveniente de la empresa Men In Black SL)\n -Gema del infinito(Sin especificar)\n -Androide (R99)\n -Botas propulsoras espaciales\n -Ojo bionico(rayos X incorporado)\n -Galaxia de bolsillo (localizada en el cinturón de Orión, Perdida, proveniencia: "SIN IDENTIFICAR")\n -Juego de realidad virtual(Roy a life well lived-Blips and Chitz)''')
        precios=[400000,1000000,50000000,25000,200000,10000,500000000,400000,15000,5000,1000000000,20000]
        muestra=[]
        cesta = []
        while True: 
            if len(cesta)!= 0:
                print("___________________________________")
                print("\nEsta es tu cesta de la compra actual: \n")
                for i in cesta:
                    print("   ---> "+i+"\n")

                print("___________________________________")
                print("Subtotal: "+str(sum(muestra)))
                print("___________________________________")

            seleccion=input('''
            1. Añada los productos que quiera comprar
            2. Borrar productos añadidos anteriormente
            3. Pago
            Escriba un número del 1 al 3 para elegir la funcionalidad que desea realizar ''')
            
            

            if seleccion=='1':
                nombreproducto=input('Producto galáctico que desea añadir al carrito: ').lower()
                if nombreproducto in productos:
                    catalogo=productos.index(nombreproducto)
                    
                    cesta.append(nombreproducto)
                    
                    precio=precios[catalogo]
                    print(f'Este producto cuesta {precio}€, sin IVA intergaláctico incluido.') 
                    muestra.append(precio)
                    
                else:
                    print('weuuuiuiuuuhh tar taarr!!!! No vendemos baratijas ni productos mediocres, elija bien lo que desee y escribalo correctamente, maldito Chiftik.')
            elif seleccion=='2':
                nombre=input('Nombra al producto que quiera aniquilar de la lista ').lower()
                if nombre not in cesta: 
                    print('mmm yar yaar, espabila y fijate en lo que escribes. Escriba producto añadido anteriormente para aniquilarlo.')  
                else:
                    precio=precios[productos.index(nombre)]
                    cesta.remove(nombre)
                    muestra.remove(precio)
            elif seleccion=='3':
                preciototal=sum(muestra)
                print('El IVA intergaláctico dependerá del planeta en el que habite.')
                print('''Nuestro sistema de envío planetario no está adecuado para todos los planetas del universo.\nSi habitas en uno de los siguientes, y desea que se lo enviemos a dicho planeta, tendrás el IVA intergaláctico que le corresponde:\n -Tierra\n -Abydos\n -Arrakis\n -Crematoria\n -Krypton\n -Acheron\n -Aura\n -Solaris\n -Tatooine\n -Coruscant\n -Genesis\n -Pandora\n De no ser así, tendrá un IVA de un "45%", definido por los Predators que manejan el sistema de envío por contrabando.''')
                planeta=input('¿En que planeta habita? ').lower()
                if planeta=='tierra':
                    print('El IVA intergaláctico de su planeta es del 25%')
                    precioiva=preciototal*1.25
                elif planeta=='abydos':
                    print('El IVA intergaláctico de su planeta es del 15%')
                    precioiva=preciototal*1.15
                elif planeta=='arrakis':
                    print('El IVA intergaláctico de su planeta es del 35%')
                    precioiva=preciototal*1.35    
                elif planeta=='crematoria':
                    print('El IVA intergaláctico de su planeta es del 11%')
                    precioiva=preciototal*1.11
                elif planeta=='krypton':
                    print('El IVA intergaláctico de su planeta es del 18%')
                    precioiva=preciototal*1.18
                elif planeta=='acheron':
                    print('El IVA intergaláctico de su planeta es del 8%')
                    precioiva=preciototal*1.08
                elif planeta=='aura':
                    print('El IVA intergaláctico de su planeta es del 22%')
                    precioiva=preciototal*1.22
                elif planeta=='solaris':
                    print('El IVA intergaláctico de su planeta es del 31%')
                    precioiva=preciototal*1.31     
                elif planeta=='tatooine':
                    print('El IVA intergaláctico de su planeta es del 38%')
                    precioiva=preciototal*1.38
                elif planeta=='coruscant':
                    print('El IVA intergaláctico de su planeta es del 5%')
                    precioiva=preciototal*1.05
                elif planeta=='genesis':
                    print('El IVA intergaláctico de su planeta es del 20%')
                    precioiva=preciototal*1.20              
                elif planeta=='pandora':
                    print('El IVA intergaláctico de su planeta es del 28%')
                    precioiva=preciototal*1.28
                else:
                    print('Este planeta no pertenece a nuestra red de envío planetario, por lo que su pedido será enviado por los Predators por contrabando(IVA 45%!!!)')
                    precioiva=preciototal*1.45
                
                print(f'El precio final con IVA incluido es de {precioiva}€')
                print('Aceptamos unicamente estos tipos de moneda para el pago:\n -Euro\n -Wupiupi\n -Credito Imperial\n -Darsek\n -Lita\n -Latinum')
                
                moneda=input('Tu moneda es: ').lower()
                if moneda=='euro':
                    pagofinal=precioiva
                    print(f'El precio de la compra es de {pagofinal}€')
                elif moneda=='wupiupi':
                    pagofinal=precioiva*1.40
                    print(f'El precio de la compra es de {pagofinal} Wupiupis')
                elif moneda=='credito imperial':
                    pagofinal=precioiva*0.60
                    print(f'El precio de la compra es de {pagofinal} Creditos Imperiales')
                elif moneda=='darsek':
                    pagofinal=precioiva*1.15
                    print(f'El precio de la compra es de {pagofinal} Darseks')
                elif moneda=='lita':
                    pagofinal=precioiva*0.85
                    print(f'El precio de la compra es de {pagofinal} Litas')
                elif moneda=='latinum':
                    pagofinal=precioiva*0.05
                    print(f'El precio de la compra es de {pagofinal} Barras de Latinum')
                else:
                    print('Truuuaarr saapppp mirr!! (No aceptamos chatarra!!)')

                comprobacion=input('Escriba "SI" si está seguro de su compra: ').lower()
                if comprobacion=='si':
                    print(f'El precio final es: {pagofinal}')
                    print('Se ha realizado el pago correctamente, San athchomari yeraan!')
                    print(f'Se ha enviado un TRXPD(PDF) de la factura a su correo inter computacional {self.email}')
                    print(f'Se ha enviado un mensaje(SMS) a su código de comunicador {self.numerotelefono} y un correo inter computacional a {self.email} con el seguimiento de su producto.')
                    print('Dos días Numenorianos después....................................................................')
                    print('Su compra ha salido de nuestras instalaciones')
                    print('Cuatro días Numenorianos despues.................................................................')
                    print(f'La compra está entrando en la atmosfera de {self.planeta}, preparese para recibir un impacto en su habitat en 3,2,1..............')
                    print('Ki aleta yeni!!(es broma!!), no sufras por tu hogar, el repartidor está en la puerta. JUAS JUAS JUAS!!')
                    print('San athchomari yeraan. Esperamos su proxima compra con entusiasmo, pequeño Ewok!!')
                    break
                else:
                    print('MMM Chiftik... seguro que no quieres realizar la compra? Te dejamos volver a seleccionar alguno de nuestros únicos productos. Vuelve a inicar sesión y piense bien lo que quiere, Graddakh!')
                    break   


                
                
                

compra1=Compra
compra1.lista(self=alienigena1)
