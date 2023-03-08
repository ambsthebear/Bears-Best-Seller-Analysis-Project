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


# BONUS ANALYSIS ONE
# titles = [book['name'] for book in book_list]
#     unique_titles = set(titles)
#     authors = [book['author'] for book in book_list]
#     unique_authors = set(authors)
#     top_book = {
#         'title': '',
#         'author': '',
#         'count': 0
#         } 
#     for author in unique_authors:
#         for title in unique_titles:
#             amount_of_repetitions_title = len(list(filter(lambda name: name == title, titles)))
#             amount_of_repetitions_author = len(list(filter(lambda author: author == author, authors)))
#         if amount_of_repetitions_title and amount_of_repetitions_author > top_book['count']:
#             top_book['title'] = title
#             top_book['author'] = author
#             top_book['count'] = amount_of_repetitions_title

#OUTPUT: author did not correspond with title


# def bonus_analysis_one(book_list):
#     print("Analysis of which author has shown up on the book list the most (Distinct books only!)")
#     titles_with_authors = [(book['name'], book['author']) for book in book_list]
#     unique_books = set(titles_with_authors)
#     top_book = {
#         'title_and_author': '',
#         'count': 0
#         } 
#     for book in unique_books:
#         amount_of_repetitions_author = len(list(filter(lambda author: author == author, titles_with_authors)))
#     if amount_of_repetitions_author > top_book['count']:
#         top_book['title'] = titles_with_authors
#         top_book['count'] = amount_of_repetitions_author
#     print(f'The top author and book in our list is {top_book["title_and_author"]} and they have been a best seller {top_book["count"]} times.')

#OUTPUT: The top author and book in our list is  and they have been a best seller 550 times.

# authors_and_titles = [((book['author']), (book['name'])) for book in book_list]
#     unique_authors_distinct_books = set(authors_and_titles)
#     top_author = {
#         'author_and_book': '',
#         'count': 0
#     }
#     for author in unique_authors_distinct_books:
#         number_of_repetitions = len(list(filter(lambda book: book == author, authors_and_titles)))
#         if number_of_repetitions > top_author['count']:
#             top_author['author_and_book'] = author
#             top_author['count'] = number_of_repetitions

#OUTPUT: {'author_and_book': ('American Psychological Association', 'Publication Manual of the American Psychological Association, 6th Edition'), 'count': 10}