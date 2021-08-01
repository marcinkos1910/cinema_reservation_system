from pprint import pprint
from movie import Movie
from helpers import card_printer
from cinemas import CinemaCity


def assign_movie():
    cc = CinemaCity()
    print(cc.get_num_of_seats())
    m = Movie("Fast and Furious", cc)
    # print(m.get_theater_in_cinema())
    # print(m.get_num_of_empty_seats())
    m.allocate_viewer(8, 5, "Marcin K")
    m.allocate_viewer(3, 5, "John R")
    m.allocate_viewer(1, 5, "David D")
    print(m.get_num_of_empty_seats())
    m.relocate_viewer(1, 5, 4, 5)
    # pprint(m.seats)
    m.print_card(card_printer)


if __name__ == '__main__':
    assign_movie()






