"""
Name: Manh Cuong Ha
Date: 26/05/2019
Brief Project Description:
This program is created so that the users can manage their places data and keep them updated with their places status to
see whether the user has visited a specific place or not. The users can also add new place to their places data.
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from placelist import PlaceList


class PlacesToVisitApp(App):
    def __init__(self, **kwargs):
        """
        Install all the needed widgets for the interface of kivy app
        """
        super().__init__(**kwargs)
        self.place_list = PlaceList()

        # Top place status label and bottom place status label
        self.top_place_status_label = Label(text="", id="count_label")
        self.bottom_place_status_label = Label(text="")
        # Sorting label
        self.sort_by_label = Label(text="Sort by:")
        # Make Country as the default sorting method
        self.spinner = Spinner(text='Country', values=('Country', 'Place', 'Priority', 'Visited'))
        self.add_new_place_label = Label(text="Add New Place...")
        self.place_name_label = Label(text="Name:")
        self.place_name_text_input = TextInput(write_tab=False, multiline=False)
        self.place_country_label = Label(text="Country:")
        self.place_country_text_input = TextInput(write_tab=False, multiline=False)
        self.place_priority_label = Label(text="Priority:")
        self.place_priority_text_input = TextInput(write_tab=False, multiline=False)

        # Add place and clear labels
        self.add_place_button = Button(text='Add Place')
        self.clear_button = Button(text='Clear')

    def build(self):
        """
        Open the kivy app and implement all widgets
        """
        self.title = "Places to Visit 2.0 by Manh Cuong Ha"
        self.root = Builder.load_file('app.kv')
        self.place_list.load_places()
        self.place_list.sort('Country')
        self.left_panel_widgets()
        self.right_panel_widgets()
        return self.root

    def left_panel_widgets(self):
        """
        Build and arrange the left side panel widgets
        """
        self.root.ids.left_panel.add_widget(self.sort_by_label)
        self.root.ids.left_panel.add_widget(self.spinner)
        self.root.ids.left_panel.add_widget(self.add_new_place_label)
        self.root.ids.left_panel.add_widget(self.place_name_label)
        self.root.ids.left_panel.add_widget(self.place_name_text_input)
        self.root.ids.left_panel.add_widget(self.place_country_label)
        self.root.ids.left_panel.add_widget(self.place_country_text_input)
        self.root.ids.left_panel.add_widget(self.place_priority_label)
        self.root.ids.left_panel.add_widget(self.place_priority_text_input)
        self.root.ids.left_panel.add_widget(self.add_place_button)
        self.root.ids.left_panel.add_widget(self.clear_button)
        self.root.ids.top_panel.add_widget(self.top_place_status_label)

        # Click control for sorting spinner, add place button and clear button
        self.spinner.bind(text=self.sort_place)
        self.add_place_button.bind(on_release=self.error_checker)
        self.clear_button.bind(on_release=self.clear_text)

    def right_panel_widgets(self):
        """
        Build and arrange the left side panel widgets
        """
        # Set the top place status label
        self.top_place_status_label.text = "To visit: " + str(self.place_list.count_unvisited_places()) + ". Visited: " + str(
                                          self.place_list.count_visited_places())

        # Check all places on the list whether it's visited or unvisited and set the coloring of the places
        for place in self.place_list.places:
            if place[0].status == 'n':
                place_coloring = Button(text='"' + place[0].name + '"' + " by " + place[0].country + " (" + str(
                                place[0].priority) + ") " "(Visited)", id=place[0].name)
                place_coloring.background_color = [88, 89, 0, 0.3]
            else:
                place_coloring = Button(text='"' + place[0].name + '"' + " by " + place[0].country + " (" + str(
                                place[0].priority) + ")", id=place[0].name)
                place_coloring.background_color = [0, 88, 88, 0.3]

            # Set the status of the pressed place button
            place_coloring.bind(on_release=self.status_manager)
            self.root.ids.right_panel.add_widget(place_coloring)

    def sort_place(self, *args):
        """
        Sort the places according to the user's choice
        """
        self.place_list.sort(self.spinner.text)
        self.root.ids.right_panel.clear_widgets()
        self.right_panel_widgets()

    def status_manager(self, button):
        """
        Organize the status of the selected place
        """
        # Button control for different place status
        if self.place_list.check_place(button.id).status == 'n':
           self.place_list.check_place(button.id).status = 'v'
           self.root.ids.bottom_panel.text = "You still need to visit " + str(self.place_list.check_place(button.id).name)
        else:
           self.place_list.check_place(button.id).status = 'n'
           self.root.ids.bottom_panel.text = "You have visited " + str(self.place_list.check_place(button.id).name)

        # Update the sorting layout
        self.sort_place()
        self.root.ids.right_panel.clear_widgets()
        self.right_panel_widgets()

    def clear_text(self, *args):
        """
        Clear all text fields
        """
        self.place_name_text_input.text = ""
        self.place_country_text_input.text = ""
        self.place_priority_text_input.text = ""
        self.root.ids.bottom_panel.text = ""

    def error_checker(self, *args):
        """
        To check if the input is valid or not
        """
        # Display error message for invalid input
        if str(self.place_name_text_input.text).strip() == '' or str(self.place_country_text_input.text).strip() == '' or str(
                self.place_priority_text_input.text).strip() == '':
            self.root.ids.bottom_panel.text = "All fields must be completed"
        else:
            try:
                # Ensure the user did not enter negative numbers
                if int(self.place_priority_text_input.text) < 0:
                    self.root.ids.bottom_panel.text = "Please enter a valid number"
                # Add the new place info to the list if there is no error
                else:
                    self.place_list.add_new_place(self.place_name_text_input.text, self.place_country_text_input.text,
                    int(self.place_priority_text_input.text))
                    self.place_list.sort(self.spinner.text)
                    self.clear_text()
                    self.root.ids.right_panel.clear_widgets()
                    self.right_panel_widgets()
            # Error check for the priority input
            except ValueError:
                self.root.ids.bottom_panel.text = "Please enter a valid number"

    def stop(self):
        # Save all the data when the app is closed
        self.place_list.save_file()


PlacesToVisitApp().run()