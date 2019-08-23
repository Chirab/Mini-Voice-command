import speech_recognition as sr
import subprocess
import sys
import os

r = sr.Recognizer()
mic = sr.Microphone()

def open_spotify():
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    app = 'Spotify'
    os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))

## close application not working..
def close_spotify():
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    app = 'Spotify'
    os.system('killall ' + d + '/%s.app' % app.replace(' ', '\ '))

def say(text):
    subprocess.call(['say', text])

def createFile():
    fichier = open("main.c", "w")
    fichier.write("int main() {\n\treturn (0)\n}")
    fichier.close()

def main():
    a = 1
    while a == 1:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                print('Transcripting...')
                try:
                    transcript = r.recognize_google(audio, language="fr-FR")
                    print(transcript)
                    if transcript == 'Bonjour':
                        say('Bonjour')
                    if transcript == 'quitte':
                        a = 0
                        if a == 0:
                            sys.exit()
                    if transcript == 'fichier':
                        say('ecriture de fichier')
                        createFile()
                    if transcript == 'test':
                        say('program is working')
                    if transcript == 'Spotify':
                        say('je lance spotify')
                        open_spotify()
                    ##if transcript == 'close Spotify':
                      ##  say('je ferme spotify')
                        ##close_spotify()
                except sr.UnknownValueError:
                    say('Je ne comprend pas')

if __name__ == "__main__":
        main()