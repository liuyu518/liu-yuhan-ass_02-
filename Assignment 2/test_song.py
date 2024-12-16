"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert default_song.is_learned is False

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print("Test initial-value song:")
    assert initial_song.title == "My Happiness"
    assert initial_song.artist == "Powderfinger"
    assert initial_song.year == 1996
    assert initial_song.is_learned is True

    # TODO: Write tests to show this initialisation works
    #Test check_learned
    print("Test check_learned method:")
    unlearned_song = Song("Unlearned", "Art", 2024, False)
    unlearned_song.check_learned()
    assert unlearned_song.is_learned is True

    # TODO: Add more tests, as appropriate, for each method
    # Test check_unlearned
    print("Test check_unlearned method:")
    unlearned_song = Song("learned", "a Art", 2025, True)
    unlearned_song.check_unlearned()
    assert unlearned_song.is_learned is False


run_tests()
