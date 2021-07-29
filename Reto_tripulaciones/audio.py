#pip3 install speech_recognition
#pip3 install pyaudio

import speech_recognition
from selenium import webdriver
from selenium.webdriver import ActionChains


# Necesita PyAudio
recog = speech_recognition.Recognizer()
micro = speech_recognition.Microphone() # Micrófono por defecto

ruta_driver = "/home/jose/Descargas/chromedriver_linux64/chromedriver" #Ruta al driver de Chrome
driver = webdriver.Chrome(ruta_driver)
driver.get("https://myablecity.herokuapp.com/")

while True:
    with micro:
        try:
            audio = recog.listen(micro, 2)
            text = recog.recognize_google(audio, language= 'es-ES')
            print(f'He reconocido: {text}')
        except Exception:
            continue

    try:

        lista_comandos = ['Acceder invitado', 'Parque', 'Discapacidad', 'Física', 
        'Grado', 'Mayor', 'Buscar', 'Primer resultado']
        '''
        if text.lower()[:6] == 'ir web':
            driver = webdriver.Chrome(ruta_driver)
            #driver.get("http://www." + text.lower()[7:] + ".com")
            driver.get("https://myablecity.herokuapp.com/")
        '''

        if text == "Acceder invitado".lower():
            driver.find_element_by_xpath('//*[@id="invitado"]').click()

        if text == "Parque".lower():
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/button[2]').click()

        if text == "Discapacidad".lower():
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/select[1]').click()

        if text == "física".lower():
            driver.find_element_by_xpath('//*[@id="motora"]').click()

        if text == "Grado".lower():
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/select[2]').click()

        if text == "Mayor".lower():
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/select[2]/option[4]').click()

        if text == "Buscar".lower():
            driver.find_element_by_xpath('/html/body/div/div/div[2]/div/button/img').click()
            
        if text == "Primer resultado".lower():
            driver.find_element_by_xpath('/html/body/div/div/div[2]/article[1]').click()

        else:
            print('Prueba otra vez')
    
    except Exception:
        continue
