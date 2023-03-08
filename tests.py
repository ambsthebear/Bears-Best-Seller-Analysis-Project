# test code tried for different analyses

# ANALYSIS THREE
    # T = 'name'
    # repeat_titles = list(map(lambda book: book[T], filter(lambda book: T in book, book_list)))
# output: all titles in the list, including duplicates.

# titles = [value for book in book_list for value in book.values('name')]
# TypeError: dict.values() takes no arguments (1 given)

    # T = 'name'
    #     titles = list(map(lambda book: book[T], filter(lambda book: T in book, book_list)))
    #     unique_titles = set(titles)
    #     top_book = {
    #         'title': '',
    #         'count': 0
    #         }
    #     for title in unique_titles:
    #         amount_of_repetitions = list(filter(lambda name: name == title, titles))
    #         print(amount_of_repetitions)

