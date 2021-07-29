#pip3 install speech_recognition
#pip3 install pyaudio

import speech_recognition
from selenium import webdriver
from text_to_speech import text_to_speech # Esta función es la que "lee" el texto
import time


# Necesita PyAudio
recog = speech_recognition.Recognizer()
micro = speech_recognition.Microphone() # Micrófono por defecto

ruta_driver = "/home/jose/Descargas/chromedriver_linux64/chromedriver" #Ruta al driver de Chrome
driver = webdriver.Chrome(ruta_driver)
driver.get("https://myablecity.herokuapp.com/")

def listen():
    '''
    Esta función es la que va a devolver el texto transcrito
    '''
    with micro:
        try:
            audio = recog.listen(micro, 2)
            text = recog.recognize_google(audio, language= 'es-ES')
            print(f'He reconocido: {text}')
            return text
        except Exception:
            return

# Esto por si quieres mensaje de bienvenida
text_to_speech('Bienvenido a my able city')

while True:
    text = listen()
    if text == "Acceder como invitado".lower():
        driver.find_element_by_xpath('//*[@id="invitado"]').click()
        text_to_speech('Has accedido como invitado')
        time.sleep(3)
        text_to_speech('¿Qué discapacidad tienes?')
        while True:
            text = listen()
            if text == 'Física'.lower():
                driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/select[1]').click()
                driver.find_element_by_xpath('//*[@id="motora"]').click()
                driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/select[1]').click()
                
                time.sleep(1)
                text_to_speech('Qué quieres buscar')

                while True:
                    text = listen()
                    if text == 'Museo'.lower():
                        driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/button[1]').click()

                        text_to_speech('Quieres iniciar la busqueda')

                        while True:
                            text = listen()
                            if text == 'Si'.lower():
                                driver.find_element_by_xpath('/html/body/div/div/div[2]/div/button/img').click()
                                text_to_speech('Búsqueda completada. Estos son los resultados')
                                time.sleep(3)
                                
                                # Estas lineas de aquí abajo son para leer las opciones que ha encontrado en la busqueda
                                # lo he dejado comentado porque es muy lento, pero si quieres dejarlo solo tienes que
                                # descomentar

                                #list_e = [elemen for elemen in driver.find_elements_by_class_name('tamanio')]
                                #list_w = [words.text for words in list_e]
                                #for word in list_w:
                                #    text_to_speech(word)
                                #    time.sleep(4)

                                text_to_speech('Qué opción quieres mirar?')

                                while True:
                                    text = listen()
                                    if text == 'Primera opción'.lower():
                                        driver.find_element_by_xpath('/html/body/div/div/div[2]/article[1]/img').click()
                                        break