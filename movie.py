from pprint import pprint
import random


class Movie:
    def __init__(self, movie_title, cinema):
        self.movie_title = movie_title
        self.cinema = cinema
        rows, places = self.cinema.get_seating_plan()
        self.seats = [None] + [{place: None for place in places} for _ in rows]

    def get_theater_in_cinema(self):
        return f'{self.cinema.get_cinema_name()}, Theater: {self.cinema.get_theater()}'

    def _parse_seat(self, row, place):
        rows, places = self.cinema.get_seating_plan()

        try:
            row_val = int(row)
        except ValueError:
            raise ValueError(f'{row} is not a number')

        if row_val not in rows:
            raise ValueError(f'Row number out of seating range: {row}')

        try:
            place_val = int(place)
        except ValueError:
            raise ValueError(f'{place} is not a number')

        if place_val not in places:
            raise ValueError(f'Place number out of seating range: {place}')

        return row_val, place_val

    def allocate_viewer(self, row, place, viewer):
        row_to_assign, place_to_assign = self._parse_seat(row, place)

        if self.seats[row_to_assign][place_to_assign] is not None:
            raise ValueError(f'Seat R:{row} P:{place} is already taken')
        self.seats[row_to_assign][place_to_assign] = viewer

    def relocate_viewer(self, row, place, row_to, place_to):
        row_from, place_from = self._parse_seat(row, place)

        if self.seats[row_from][place_from] is None:
            raise ValueError(f'No passenger assigned to R:{row_from} P:{place_from}')

        self._parse_seat(row_to, place_to)

        if self.seats[row_to][place_to] is not None:
            raise ValueError(f'Seat R:{row_to} P:{place_to} is already taken')

        self.seats[row_to][place_to] = self.seats[row_from][place_from]
        self.seats[row_from][place_from] = None

    def get_num_of_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None) for row in self.seats if row is not None)

    def get_viewers(self):
        for idx, row in enumerate(self.seats):
            if row is not None:
                for place, viewer in row.items():
                    if viewer is not None:
                        # yield viewer, f'Row:{idx} Place:{place}'
                        yield f'Row:{idx} Place:{place}'

    def print_card(self, printer):
        for seat in self.get_viewers():
            printer(self.movie_title, self.get_theater_in_cinema(), seat)


def card_printer(movie_title, theater, seat):
    text = f'| {movie_title}, {theater}, {seat} |'
    frame = f'{"*" * len(text)}'
    empty_frame = f'|{" " * (len(text) - 2)}|'

    banner = [frame, empty_frame, text, empty_frame, frame]
    banner_txt = "\n".join(banner)
    print(banner_txt)







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


cc = CinemaCity()
print(cc.get_num_of_seats())
m = Movie("Fast and Furious", cc)
# print(m.get_theater_in_cinema())
# print(m.get_num_of_empty_seats())
m.allocate_viewer(8, 5, "Marcin K")
m.allocate_viewer(3, 5, "John R")
m.allocate_viewer(1, 5, "David D")
# print(m.get_num_of_empty_seats())
# m.relocate_viewer(1, 5, 4, 5)
# # pprint(m.seats)
m.print_card(card_printer)






