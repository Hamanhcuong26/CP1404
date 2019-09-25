from place import Place


class PlaceList:
    def __init__(self, ):
        """
        Start place object as empty
        """
        self.places = []

    def load_places(self):
        """
        Load all places from places.csv and arrange each place's attribute
        """
        file_read = open('places_backup.csv', 'r')
        for place in file_read:
            place_string = place.split(",")
            self.places.append(
                [Place(place_string[0], place_string[1], int(place_string[2]), place_string[3].strip())])

        file_read.close()

    def sort(self, sort_by):
        """
        Sort the place according to the user's choice then by title
        """
        if sort_by == "Country":
            self.places.sort(key=lambda i: (i[0].country, i[0].name))
        elif sort_by == "Place":
            self.places.sort(key=lambda i: i[0].name)
        elif sort_by == "Priority":
            self.places.sort(key=lambda i: (i[0].priority, i[0].name))
        else:
            self.places.sort(key=lambda i: (i[0].status, i[0].name))

    def add_new_place(self, name, country, priority):
        """
        Add the new place to the place list
        """
        self.places.append([Place(name, country, priority, 'y')])

    def check_place(self, name):
        """
        Return the selected place to user
        """
        for place in self.places:
            if place[0].name == name:
                return place[0]

    def count_unvisited_places(self):
        """
        Check the place list and count the number of places that still need to be visited
        """
        unvisited_places = 0
        for place in self.places:
            if place[0].status == 'y':
                unvisited_places += 1
        return unvisited_places

    def count_visited_places(self):
        """
        Check the place list and count the number of visited places
        """
        visited_places = 0
        for place in self.places:
            if place[0].status == 'n':
                visited_places += 1
        return visited_places

    def save_file(self):
        """
        Save all the changes from the user to places.csv
        """
        file_write = open('places_backup.csv', 'w')
        for place in self.places:
            file_write.write(
                place[0].name + "," + place[0].country + "," + str(place[0].priority) + "," + place[
                    0].status + "\n")

        file_write.close()