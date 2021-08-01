def card_printer(movie_title, theater, seat):
    text = f'| {movie_title}, {theater}, {seat} |'
    frame = f'{"*" * len(text)}'
    empty_frame = f'|{" " * (len(text) - 2)}|'

    banner = [frame, empty_frame, text, empty_frame, frame]
    banner_txt = "\n".join(banner)
    print(banner_txt)