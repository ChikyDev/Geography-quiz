'''ESTO ES UN JUEGO'''
#Para usar este juego deberas de tener instalado python en tu ordenador
# 1. paso, abrir Simbolo del sistema
# 2. paso, buscamos el archivo donde se haya guardado
# 3. paso, ejecutamos con python3 mini_juego.py o si tienes una version mas antigua de python usaremos, python2 o python mini_juego.py#



#REGLAS DEL JUEGO:
#- Empiezas con 10 vidas
#- Cada error resta 1 vida
#- Con 3 vidas o menos aparece advertencia
#- Con 0 vidas termina el juego

import sys



vida = 10 #Tenemos una vida de 10 intentos que el usuario debera de no gastarlas todas
inicio = input('Jugamos? 🎮​: ')

inicio = inicio.lower()
if inicio == 'si': #Aqui el usuario debera de elegir si jugar
   pass
    

juego = input('Okay, entonces, este sera el juego, si respondes bien, pasaras a la siguiente pregunta y si no se te restara un punto de vida 👍​: ')


if juego == 'okay' or juego == 'vale': 

    juego = juego.lower().strip()

    #PRIMERA PREGUNTA

print('1. ⬇️​ Primera pregunta ⬇️​') #Aqui salen las preguntas a responder
print('En que continente esta España')
print('Asia')
print('Europa')
print('America')
print('Oceania')

while True:
    respuesta = input('Cual es la respuesta correcta?: ') #El usuario debera de introducir su respuesta

  

    respuesta = respuesta.lower().strip()

    if respuesta == 'europa': #Esto indica que si Europa es la seleccionada, se pasara a la siguiente ronda

        print('Es correcto ✅​, siguiente pregunta')
        print(f'Te queda {vida} vidas')
        break

    elif respuesta in ['asia', 'oceania', 'america']: #Pero aqui, si el usuario no acierta y dice una de estas 3 respuestas, se restara una vida de las 10 que tiene
        vida -= 1 #resta una vida
        print('Respuesta incorrecta ❌​')
        print(f'Te queda {vida} vidas') #Muestra las vidas restantes del usuario

    else:
        print('Parece que necesitas un repaso de geografia 🤔​')

    if vida <= 3 and vida >0: #Aqui esta indicando que cuando la vida sea menor a 3 y mayor a 0 salga el mensaje de alerta
            print(f'cuidado te quedan {vida} vidas 🥶') #Mensaje de alerta por baja vida
    elif vida == 0: #Lo que se muestra aqui, es que si vida llega a 0, se termina la partida
            print('🔴​ Game over 🔴​')
            break
    

            #SEGUNDA PREGUNTA

print('2. ⬇️ Segunda pregunta ⬇️')
print('Cual es la capital de España')
print('Madrid')
print('Barcelona')
print('Sevilla')
print('Valencia')


while True:
        respuesta_2 = input('Cual es la capital de España?: ')

        respuesta_2 = respuesta_2.lower().strip()


        if respuesta_2 == 'madrid':
            print('Respuesta correcta ✅, siguiente pregunta')
            print(f'te quedan {vida} vidas 🤗')
            break


        elif respuesta_2 in ['ba2rcelona', 'sevilla', 'valencia']:
             vida -= 1
             print('Respuesta incorrecta ❌​')
             print(f'Te queda {vida} vidas')
        

        if vida <=3 and vida >0:
             print(f'te quedan {vida} vidas 🥶')
        
        elif vida == 0:
             print('🔴 Game over 🔴')
             break
        

        #TERCERA PREGUNTA
        

print('3. ⬇️ Siguiente pregunta ⬇️')
print('Cual es el continente donde esta E.E.U.U')
print('Asia')
print('Europa')
print('America')
print('Oceania')

while True:

    respuesta_3 = input('Cual es la respuesta correcta?: ')

    respuesta_3 = respuesta_3.lower().strip()

    if respuesta_3 == 'america':
         print('Correcto! vas por buen camino ✅')
         print(f'Te quedan {vida} vidas')
         break
    
    if respuesta_3 in ['asia', 'oceania', 'europa']:
         vida -= 1
         print(f'Te quedan {vida} vidas')
    

    elif vida <= 3 and vida > 0:
         print(f'te quedan {vida} vidas 🥶')
    
    elif vida == 0:
         print('🔴 Game over 🔴')
         break

print('4. ⬇️ Siguiente pregunta ⬇️')
print('Cual es la capital de Francia 🤔')
print('Paris')
print('Madrid')
print('Lisboa')
print('Londres')


    #CUARTA PREGUNTA

while True:
     
    respuesta_4 = input('Cual es la respuesta correcta: ')

    respuesta_4 = respuesta_4.lower().strip()

    if respuesta_4 == 'paris':
        print('Correcto! que bueno eres, seguimos hacia la siguiente pregunta 💪​')
        print(f'Te quedan {vida} vidas, sigue asi!💪​')
        break
    elif respuesta_4 in ['madrid', 'lisboa', 'londres']:
        vida -= 1
        print(f'Te quedan {vida}, ten cuidado 😵‍💫​')
        print('Vuelve a intentarlo')
        
    
    elif vida <= 3 and vida >0:
        print(f'Ten cuidado, te quedan {vida} 🥶')
    elif vida == 0:
        print('🔴 Game over 🔴')
        break

    #BONUS TRACK

while True: #Este bucle lo que hace es, si el usuario desea seguir debera de responder 'si'

    print('Parece que eres un/a chico/a listo 🤓​')
    continuar = input('Seguimos con el juego? o te atreves a plantarte 🤨​: ') #Aqui el usuario debera de responder 
    continuar = continuar.lower().strip() 

    if continuar in ['si', 'venga', 'va', 'okay', 'ok']: #El usuario deberea de responder con algunas de estas respuestas que estan en la lista
        print('Que valiente!!! ⚔️​')
        break #Rompe el bucle y sigue el juego
    elif continuar == 'no':
         print('Bueno, otra vez sera, muy bien jugado!!! 😜​')
         print(f'En total te han quedado {vida} vidas 🙃​')
         sys.exit() #Este bucle es igual solo que sale el juego

    
     #QUINTA PREGUNTA
    
print('Okay seguimos con las ultimas 2 preguntas.')
print('5. ⬇️ Siguiente pregunta ⬇️')
print('Cual es el continente con mayor poblacion?')
print('Europa')
print('America')
print('Asia')
print('Oceania')

while True:

    respuesta_5 = input('Cual es la correcta?: ')
    respuesta_5 = respuesta_5.lower().strip()

    if respuesta_5 == 'asia':
        print('Toma ya!, acertaste ✅')   
        print(f'Te quedan {vida} vidas 🤗​')  
        break
    elif respuesta_5 in ['europa', 'america', 'oceania']:
         vida -= 1
         print(f'Te quedan {vida} vidas, ves con mas cuidado')
    elif vida <3 and vida >0:
         print(f'Ves con cuidado, te quedan {vida} vidas 🥶')
    elif vida == 0:
         print('🔴 Game over 🔴')
    break


        #NIVEL FINAL

print(' 🔥​Nivel final 🔥​')
print('Cual es el pais mas grande a nivel mundial')
print('China')
print('E.E.U.U')
print('Rusia')
print('India')

while True:
     
    respuesta_6 = input('Cual es la respuetsa correcta?: ')

    respuesta_6 = respuesta_6.lower().strip()

    if respuesta_6 == 'rusia':
          print('Olee, que crack eres, se ve que sabes mucho!!​👏​👏​')
          print(f'Terminaste el juego con {vida} vidas 🤗​')
          break
    
    elif respuesta_6 in ['china', 'e.e.u.u', 'estados unidos', 'india']:
          vida -= 1
          print(f'Te quedan {vida} vidas')
          print('Respuesta incorrecta, sigue probando 🤙​')
    elif vida <3 and vida >0:
         print(f'Ten cuidado te quedan {vida} vidas')
    elif vida == 0:
         print(' Ohhh vaya! parece ser que te quedaste sin vidas, pero no te desanimes, eres muy bueno/a en geografia 🤗 ')
         break    
    
    #Fin del juego