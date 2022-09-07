import webbrowser #for opening up wikipedia 
import wikipedia
import pyttsx3

alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def wikiOpen(go):
    url = wikipedia.page(go).url
    webbrowser.open(url, new=2)

def wikiSearch(go):
    print(go)
    try:
        result  = wikipedia.summary(go, sentences = 2)
        print(result)
        talk(result)
        
            
    except Exception as e:
        print("not specific enough")
        pass

def main():
    go = input("What do you want to look up on Wikipedia? ")
    if('open wikipedia' in go):
        go = go.replace('open wikipedia ', '')
        wikiOpen(go)
    elif('wikipedia' in go):
        go = go.replace('wikipedia ', '')
        wikiSearch(go)

if __name__ == "__main__":
    main()
