from artwork import get_artworks


def main():
    artwork = input("Artwork: ")

    artworks = get_artworks(query=artwork, limit=3)

    for artwork in artworks:
        print(f" {artwork}")


main()


# Creating Modules and Packages with artwork.py