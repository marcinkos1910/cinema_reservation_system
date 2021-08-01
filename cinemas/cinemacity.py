import random


class CinemaCity:
    @staticmethod
    def get_cinema_name():
        return "Cinema city"

    @staticmethod
    def get_theater():
        return str(random.randint(1, 6))

    @staticmethod
    def get_seating_plan():
        return range(1, 11), range(1, 21)

    def get_num_of_seats(self):
        row, place = self.get_seating_plan()
        print(row, place)
        return len(row) * len(place)