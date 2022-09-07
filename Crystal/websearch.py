import webbrowser

def youSearch(search):
    search.replace(" ","+")

    webbrowser.open('https://www.youtube.com/results?search_query='+search, new=2)

def googSearch(search):
    search.replace("","+")
    webbrowser.open('https://www.google.com/search?q='+search, new=2)

def main():
    print("Enter your search")

    search = input()
    search = search.lower()
    if 'youtube' in search:
        search.replace('youtube ', '')
        youSearch(search)

    elif 'google' in search:
        search.replace('google ','')
        googSearch(search)

if __name__ == "__main__":
    main()
