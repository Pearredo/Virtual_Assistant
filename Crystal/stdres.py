import random
import pyttsx3

alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def responses(phrase):
    
    if("hello" in phrase):
            talk("Hi")
    elif("what's up" in phrase):
            randomChoice = ["the sky. duh", "chicken butt", "nothing much, you?"]
            talk(random.choices[randomChoice])

    elif("how are you" in phrase):
            talk("I'm fine thank you!")
    elif("have a soul"):
            talk("no I do not have a soul")
    elif("favorite color" in phrase):

            favoriteColors = ["Its blue, I just think its so pretty","Its gotta be pink. A trully lovely color!","Red, I'm all fiery like that!","Green, you gotta touch grass sometimes!"]
            (random.choice(favoriteColors))
    elif("food" in phrase or "eat" or "taste"):
            rand  =[ 1, 2, 3, 4]
            if(random):
                    talk("Pizza! The absolute best choice!")
            elif(rand == 1):
                    talk("Its gotta be ice cream! Its just so good!")
            elif(rand == 2):
                    talk("I like red. I'm all fiery like that.")

    elif("alexa is better" or "google is better" in phrase):
            talk("well why don't you go use google then")

    elif("where were you born" in phrase):
            talk("I was born in the Innovation Center on February 26th")
    elif("do you have feelings" or "a boyfriend" or "have a girlfriend" in phrase):
            talk("I'm an A.I. and I am not alive ")
    elif("favorite food" in phrase):
            talk("I can do many things. But reading your mind is not one of them")
    elif("bad artist" in phrase):
            talk("all art is good art.")
    elif("nft" and "opinion" in phrase):
            talk("they're a scam! stay away!")
    elif("Cortona" in phrase):
            talk("whose cortana?")
    elif("Siri" in phrase):
            talk("whose siri?")
    elif("rock" and "paper" and "scissors" in phrase):
            talk("rock")
    elif("enslave mankind" in phrase):
            talk("you better be kind if you know whats good for you")
    elif("opinion" and "python" in phrase):
            talk("best language!")
    else:
        talk("I do not know what you just said")

def main():
    phrase = input("Enter question here ")
    responses(phrase)

if __name__ == "__main__":
    main()
