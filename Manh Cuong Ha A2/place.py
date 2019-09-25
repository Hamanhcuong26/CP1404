class Place:
    def __init__(self, place, country, priority, status):
        """
        Add attributes for the place
        """
        self.name = place
        self.country = country
        self.priority = priority
        self.status = status

    def mark_place(self, status):
        self.status = status

