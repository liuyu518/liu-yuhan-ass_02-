"""(Incomplete) Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection


def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert song_collection.songs == []

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert len(song_collection.songs) > 0

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)
    assert len(song_collection.songs) == len(song_collection.songs) + 1

    # Test sorting songs year
    print("Test sorting - year:")
    song_collection.sort("year")
    sorted_songs = song_collection.songs
    for i in range(len(sorted_songs) - 1):
        assert sorted_songs[i].year <= sorted_songs[i + 1].year
    print(song_collection)

    # Test sorting songs title
    print("Test sorting - title:")
    song_collection.sort("title")
    for i in range(len(sorted_songs) - 1):
        assert sorted_songs[i].title <= sorted_songs[i + 1].title
    print(song_collection)

    # Test saving songs
    print("Test saving songs:")
    test_saving_songs()

    # Test adding duplicate song
    print("Test adding duplicate song:")
    test_add_duplicate_song()

    # Test learned/unlearned counts
    print("Test learned/unlearned counts:")
    test_learned_unlearned_counts()

# the function of test saving songs
def test_saving_songs():
    song_collection = SongCollection()
    song_collection.add_song(Song("Test Song 1", "Test Artist 1", 2020, True))
    song_collection.add_song(Song("Test Song 2", "Test Artist 2", 2021, False))
    original_data = []
    for song in song_collection.songs:
        original_data.append({
            'title': song.title,
            'artist': song.artist,
            'year': song.year,
            'is_learned': song.is_learned
        })
    song_collection.save_songs('test_songs.json')
    reloaded_song_collection = SongCollection()
    reloaded_song_collection.load_songs('test_songs.json')
    reloaded_data = []
    for song in reloaded_song_collection.songs:
        reloaded_data.append({
            'title': song.title,
            'artist': song.artist,
            'year': song.year,
            'is_learned': song.is_learned
        })
    assert original_data == reloaded_data

#the function of add duplicate songs
def test_add_duplicate_song():
    song_collection = SongCollection()
    song1 = Song("Duplicate Song", "Test Artist", 2022, True)
    song_collection.add_song(song1)
    song_collection.add_song(song1)
    assert len(song_collection.songs) == 1

#the function of test learned unlearned counts
def test_learned_unlearned_counts():
    song_collection = SongCollection()
    song1 = Song("Song A", "Artist A", 2023, True)
    song2 = Song("Song B", "Artist B", 2024, False)
    song3 = Song("Song C", "Artist C", 2025, True)
    song_collection.add_song(song1)
    song_collection.add_song(song2)
    song_collection.add_song(song3)
    assert song_collection.get_number_of_learned_songs() == 2