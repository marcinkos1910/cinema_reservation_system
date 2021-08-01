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
