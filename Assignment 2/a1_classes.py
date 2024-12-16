"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to

from songcollection import SongCollection
from song import Song

FILENAME = "songs.json"


def main():
    """... complete this and all docstrings."""
    print("Song List 1.0 - by Liu Yuhan")

    # load songs with a suitable function
    song_collection = SongCollection()
    song_collection.load_songs(FILENAME)
    print(f"{len(song_collection.songs)} songs loaded.")

    # Follow the menu pattern
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            # display songs with a suitable function
            display_songs_func(song_collection)
        elif choice == "A":
            # Add new song with a suitable function
            add_new_song(song_collection)
        elif choice == "C":
            # Complete a song with a suitable function
            complete_a_song(song_collection)
        else:
            print("Invalid menu choice.")
        display_menu()
        choice = input(">>> ").upper()
        # Complete a song with a suitable function
    song_collection.save_songs(FILENAME)
    print("Make some music!")

def display_menu():
    """display main menu"""
    print("Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")


# display songs with a suitable function
def display_songs_func(song_collection):
    """display songs as right format"""

    #sort songs by year and title
    sorted_songs = sorted(song_collection.songs, key=lambda song: (song.year, song.title))

     #get the max length
    max_title_length = max(len(song.title) for song in sorted_songs)
    max_artist_length = max(len(song.artist) for song in sorted_songs)

    #output alignment
    for index, song in enumerate(sorted_songs):
        learned_status = '*' if not song.is_learned else ' '
        print(f"{index + 1}. {learned_status} {song.title.ljust(max_title_length)} - {song.artist.ljust(max_artist_length)} ({song.year})")

    #count the number of unlearned songs
    print(f"{song_collection.get_number_of_learned_songs()} songs learned, {song_collection.get_number_of_unlearned_songs()} songs still to learn.")

#Add new song with a suitable function
def add_new_song(song_collection):
    """add new song with right input"""

    print("Enter details for a new song.")

    #about title
    title = input("Title: ")
    while title =="":
        print("Input can not be blank.")
        title = input("Title: ")

    #about artist
    artist = input("Artist: ")
    while artist == "":
        print("Input can not be blank.")
        artist = input("Artist: ")

    #about year
    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:
                print("Number must be > 0.")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number.")

    #add new songs successfully
    song = Song(title, artist, year)
    song_collection.add_song(song)
    print(f"{title} by {artist} ({year}) added to song list.")

# Complete a song with a suitable function
def complete_a_song(song_collection):
    """complete s song that market learned"""

    print("Enter the number of a song to mark as learned.")
    sorted_songs = sorted(song_collection.songs, key=lambda song: (song.year, song.title))

    #determine whether the input is correct
    while True:
        try:
            song_number = int(input(">>> ")) - 1

            #some wrong input
            if song_number >= len(sorted_songs):
                print("Invalid song number.")
                continue
            if song_number < 0:
                print("Number must be > 0.")
                continue

            #the int is right
            song = sorted_songs[song_number]
            if song.is_learned:
                print(f"You have already learned {song.title}.")
                # Return to the main menu if the song is already learned
                return
            else:
                for original_song in song_collection.songs:
                    if original_song.title == song.title and original_song.artist == song.artist and original_song.year == song.year:
                        original_song.is_learned = True
                        print(f"{song.title} by {song.artist} learned.")
                        # Return to the main menu after marking the song as learned
                        return
                print("Song not found in the list.")
        #some other wrong input
        except ValueError:
            print("Invalid input not an int.")
            continue



if __name__ == '__main__':
    main()