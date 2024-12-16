"""..."""


# TODO: Create your SongCollection class in this file

import json
from song import Song

"""
    The SongCollection class is used to manage a collection of songs.
    It provides methods for adding songs, loading songs from a file,
    saving songs to a file, counting the number of learned and unlearned songs,
    and sorting the songs in the collection.
    It maintains a list (self.songs) to store instances of the Song class.
    """

class SongCollection:
    def __init__(self):
        """
               Constructor of the SongCollection class.
               Initializes an empty list (self.songs) which will be used to store song objects later.
               """

        self.songs = []

    def add_song(self, song):
        """
        Adds a song to the song collection.
        """
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """
                Counts the number of unlearned songs in the song collection.

                Returns:
                An integer representing the number of unlearned songs.
                It iterates through the self.songs list and counts the songs whose is_learned attribute is False.
                """
        return sum(1 for song in self.songs if not song.is_learned)

    def get_number_of_learned_songs(self):
        """
        Counts the number of learned songs in the song collection.
        """
        return sum(1 for song in self.songs if song.is_learned)

    def load_songs(self, file_path):
        """
        Loads song data from a specified JSON file and creates corresponding Song objects
        to add them to the song collection.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for song_data in data:
                    song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
                    self.add_song(song)
            return self
        except FileNotFoundError:
            print(f"File {file_path} not found.")

    def save_songs(self, file_path):
        """
        Saves all the song information in the current song collection to a specified JSON file.
        """
        data = []
        for song in self.songs:
            data.append({
                'title': song.title,
                'artist': song.artist,
                'year': song.year,
                'is_learned': song.is_learned
            })
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def sort(self, key):
        """
        Sorts the songs in the collection based on a specified attribute.
        """
        self.songs.sort(key=lambda song: getattr(song, key))