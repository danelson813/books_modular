from helpers.helper_functions import *
from tqdm import tqdm       # Just to provide a progress bar


def main() -> None:
    for page in tqdm(range(1, 51)):
        soup = get_soup(page)
        lst = get_list(soup)
        results_ = parse_books(lst)

        output(results_)


if __name__ == '__main__':
    main()
