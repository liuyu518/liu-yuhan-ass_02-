"""..."""


# TODO: Create your Song class in this file


class Song:
    """"
    __init__ is the constructor of the class, which is used to initialize the
    attributes of the object when creating an instance object of the Song class.
    It accepts four parameters: title (the song title), artist (the singer),
    year (the release year), and is_learned (whether it has been learned,
    with the default value of False).
    """
    def __init__(self, title="", artist="", year=0, is_learned=False):
        self.title = title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    """
    The __str__ method is used to define the string representation form of 
    the object. It determines the string of the learning status ("learned" or "unlearned") 
    according to the is_learned attribute of the song
    """
    def __str__(self):
        learned_status = "learned" if self.is_learned else "unlearned"
        return f"{self.title} by {self.artist} ({self.year}) ({learned_status})"

    """
    It simply sets the is_learned attribute of the object to True,
    indicating that the song has been learned.
    """
    def check_learned(self):
        self.is_learned = True

    """
    Opposite to the mark_as_learned method, the mark_as_unlearned method is
    used to mark the song as unlearned. It sets the is_learned attribute of 
    the object to False.
    """
    def check_unlearned(self):
        self.is_learned = False
