class Movie:
    def __init__(self, title, genre, duration, seats_available):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.seats_available = seats_available

    def update_seats(self, new_seats):
        self.seats_available = new_seats

    def __str__(self):
        return f"{self.title}, {self.genre}, {self.duration}, {self.seats_available}"
    
class Ticket:
    def __init__(self, ):
    