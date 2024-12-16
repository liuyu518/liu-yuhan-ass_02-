"""
Name:liu Yuhan
Date Started:12/15
Brief Project Description:This is a desktop application developed based on the Kivy framework. It aims to assist users
in managing their song collections and tracking the learning status of songs. The application realizes relevant functions
with the help of custom "Song" and "SongCollection" classes. The "Song" class is used to encapsulate the key information
of each song, such as the song title, the artist, the release year, and the flag indicating whether the song has been learned
or not. The "SongCollection" class serves as a container for song objects and provides methods for adding songs to the
collection, obtaining the number of learned and unlearned songs, sorting the songs according to different attributes,
and loading and saving song data from and to a JSON file. By default, the data is stored in a file named "songs.json".
The user interface of the application adopts a horizontal layout and is divided into two main panels on the left and right,
 clearly separating different functional areas.For the left panel, there is a dropdown menu for selecting the sorting
 method. Users can sort the song list by the song title, the artist, or the release year. The menu is accompanied by
 corresponding buttons, which makes it convenient for users to trigger the dropdown menu to expand and easily choose
 their preferred sorting method. Below the sorting function, there are text input fields for entering the information of
  new songs, corresponding to the song title, the artist, and the release year respectively. After filling in the
  information, users can click the "Add Song" button to add the new song to the song collection. In addition, there is a
"Clear" button, which is used to clear the contents of these input fields when needed.For the right panel, it mainly
displays the song list in the form of buttons. Each button corresponds to a song and is color-coded according to whether
the song has been learned or not. The buttons of learned songs are displayed in green, while those of unlearned songs
are shown in red, which enables users to intuitively know the learning status of each song. At the top of the right
panel, there is a status label used to display the number of learned and unlearned songs, allowing users to quickly
understand the overall learning progress. At the bottom of the right panel, there is another status label for showing
various prompt messages related to user operations. For example, after adding a song, sorting, or toggling the learning
status of a song, the corresponding confirmation messages and supplementary explanations will be displayed here.
GitHub URL:https://github.com/liuyu518/liu-yuhan-ass_02-.git
"""

# TODO: Create your main program in this file, using the SongListApp class

# Import necessary modules and set the graphics backend for Kivy

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# Import Kivy app and UI components
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

# Import custom classes for song collection and song
from songcollection import SongCollection
from song import Song

# Define the main application class
class SongListApp(App):
    # Initialize the app and load the song collection from a JSON file
    def build(self):
        self.song_collection = SongCollection()
        self.song_collection.load_songs('songs.json')

        layout = BoxLayout(orientation='horizontal')

        left_panel = BoxLayout(orientation='vertical')

        self.sort_dropdown = DropDown()
        sort_options = ['Sort by title', 'Sort by artist', 'Sort by year']
        for option in sort_options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn, opt=option: self.sort_songs(opt))
            self.sort_dropdown.add_widget(btn)

        sort_button = Button(text='Sort by:', size_hint=(1, None), height=44)
        sort_button.bind(on_release=self.sort_dropdown.open)

        # Add the sorting button and dropdown to the left panel
        sort_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        sort_layout.add_widget(sort_button)
        sort_layout.add_widget(Label(text='Select sorting method:', size_hint_y=None, height=30))
        sort_layout.add_widget(
            Button(text='Choose sorting method', size_hint_y=None, height=44, on_release=self.sort_dropdown.open))

        left_panel.add_widget(sort_layout)

        # Create text inputs for the song title, artist, and year
        self.title_input = TextInput(hint_text='Title')
        left_panel.add_widget(self.title_input)
        self.artist_input = TextInput(hint_text='Artist')
        left_panel.add_widget(self.artist_input)
        self.year_input = TextInput(hint_text='Year')
        left_panel.add_widget(self.year_input)

        # Create a button to add a new song and bind its on_release event
        add_button = Button(text='Add Song')
        add_button.bind(on_release=self.add_song)
        left_panel.add_widget(add_button)
        clear_button = Button(text='Clear')
        clear_button.bind(on_release=self.clear_fields)
        left_panel.add_widget(clear_button)
        layout.add_widget(left_panel)

        # Create the right panel for displaying song buttons and status labels
        self.right_panel = BoxLayout(orientation='vertical')
        self.status_label_top = Label(
            text=f"To learn: {self.song_collection.get_number_of_unlearned_songs()} Learned: {self.song_collection.get_number_of_learned_songs()}")
        self.right_panel.add_widget(self.status_label_top)

        # Create buttons for each song in the collection and add them to the right panel
        self.song_buttons = []
        for song in self.song_collection.songs:
            song_button = self.create_song_button(song)
            self.song_buttons.append(song_button)
            self.right_panel.add_widget(song_button)

        # Create a status label at the bottom of the right panel
        self.status_label_bottom = Label(text='')
        self.right_panel.add_widget(self.status_label_bottom)
        layout.add_widget(self.right_panel)

        return layout

    # Method to create a button for a song
    def create_song_button(self, song):
        song_button = Button(text=str(song), background_color=(0, 1, 0, 1) if song.is_learned else (1, 0, 0, 1))
        song_button.song = song
        song_button.bind(on_release=lambda btn: self.toggle_learned(btn.song))
        return song_button

    # Method to sort songs by a given attribute
    def sort_songs(self, option):
        sort_keys = {
            'Sort by title': 'title',
            'Sort by artist': 'artist',
            'Sort by year': 'year'
        }
        actual_key = sort_keys.get(option)
        if actual_key:
            self.song_collection.songs.sort(key=lambda x: getattr(x, actual_key))
            self.update_song_buttons()
            self.update_status_labels()
            self.update_status_bottom(f"Songs sorted by: {actual_key}")
        else:
            self.update_status_bottom("Invalid sort option")

    # Method to validate the year input
    def validate_year(self, year_str):
        if not year_str.isdigit():
            return False, "Please enter a correct year number"
        year = int(year_str)
        if year <= 0:
            return False, "The number should be greater than zero"
        return True, ""

    # Method to add a new song
    def add_song(self, instance):
        title = self.title_input.text
        artist = self.artist_input.text
        year_str = self.year_input.text

        try:
            year = int(year_str)
            if year <= 0:
                self.status_label_bottom.text = "The number should >0."
                return
        except ValueError:
            self.status_label_bottom.text = "Please enter a correct year number."
            return

        song = Song(title, artist, year, False)
        self.song_collection.add_song(song)
        new_button = self.create_song_button(song)
        self.song_buttons.append(new_button)
        self.right_panel.add_widget(new_button)
        self.update_status_bottom("Added new song: " + title)
        self.update_status_labels()
        self.clear_fields()

    # Method to show a popup with song details
    def show_song_detail_popup(self, song):
        popup_content = BoxLayout(orientation='vertical', spacing=10)
        title_label = Label(text=f"Title: {song.title}")
        artist_label = Label(text=f"Artist: {song.artist}")
        year_label = Label(text=f"Year: {song.year}")
        learned_status_label = Label(text=f"Learned: {'Yes' if song.is_learned else 'No'}")
        toggle_button = Button(text="Toggle Learned Status")
        toggle_button.bind(on_release=lambda btn, s=song: self.toggle_learned(s))
        close_button = Button(text="Close")
        close_button.bind(on_release=self.close_popup)
        message_label = Label(text=f"You need to learn {song.title}")
        popup_content.add_widget(title_label)
        popup_content.add_widget(artist_label)
        popup_content.add_widget(year_label)
        popup_content.add_widget(learned_status_label)
        popup_content.add_widget(message_label)
        popup_content.add_widget(toggle_button)
        popup_content.add_widget(close_button)
        self.current_popup = Popup(title=f"Song Details: {song.title}",
                                   content=popup_content,
                                   size_hint=(None, None),
                                   size=(300, 300),
                                   auto_dismiss=False)
        self.current_popup.open()

    # Method to close the song detail popup
    def close_popup(self, instance):
        if self.current_popup:
            self.current_popup.dismiss()
            self.current_popup = None

    # Method to toggle the learned status of a song
    def toggle_learned(self, song):
        song.check_learned() if not song.is_learned else song.check_unlearned()
        for button in self.song_buttons:
            if button.song == song:
                button.background_color = (0, 1, 0, 1) if song.is_learned else (1, 0, 0, 1)
        self.update_status_bottom(f"Toggled {song.title} to {'learned' if song.is_learned else 'unlearned'}")
        self.update_status_labels()

    # Method to clear the input fields
    def clear_fields(self, instance=None):
        self.title_input.text = ''
        self.artist_input.text = ''
        self.year_input.text = ''
        self.status_label_bottom.text = 'Fields cleared'

    # Method to update the song buttons displayed on the right panel
    def update_song_buttons(self):
        for button in self.song_buttons:
            self.right_panel.remove_widget(button)
        self.song_buttons.clear()
        for song in self.song_collection.songs:
            song_button = self.create_song_button(song)
            self.song_buttons.append(song_button)
            self.right_panel.add_widget(song_button)

    # Method to update the status labels at the top of the right panel
    def update_status_labels(self):
        unlearned_count = self.song_collection.get_number_of_unlearned_songs()
        learned_count = self.song_collection.get_number_of_learned_songs()
        self.status_label_top.text = f"To learn: {unlearned_count} Learned: {learned_count}"

    # Method to update the status label at the bottom of the right panel
    def update_status_bottom(self, message):
        self.status_label_bottom.text = message

    # Method to save the song collection to a JSON file when the app is closing
    def on_stop(self):
        self.song_collection.save_songs('songs.json')
        self.update_status_bottom("Application is closing")


if __name__ == '__main__':
    SongListApp().run()