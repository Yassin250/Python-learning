
SHOWS = [
    "BeN 10",
    "Avatar: The Last airbender",
    "The Legend of Korra",
    " Artur",
    "Kim possibel",
    "jimmy Neutron",
    "the Proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
      cleaned_shows.append(show.title().strip())

    print(', '.join(cleaned_shows))  
main()        