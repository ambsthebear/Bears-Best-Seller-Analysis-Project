from data import data_list


def run_analysis(books):
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book['year'] == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book['price'])
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book['name']} with a price of {highest_cost_book['price']}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    books_2018 = list(filter(lambda book: book ['year'] == 2018, book_list))
    lowest_number_of_reviews = min(books_2018, key = lambda book: book ['number_of_reviews'])
    print(f"The book with the lowest number of reviews in 2018 was " + f"{lowest_number_of_reviews['name']}" + f" with a total of {lowest_number_of_reviews['number_of_reviews']} reviews.")


def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the book list")
    nonfic_list = list(filter(lambda book: book['genre'] == 'Non Fiction', book_list))
    fic_list = list(filter(lambda book: book['genre'] == 'Fiction', book_list))
    if len(nonfic_list) > len(fic_list):
        print("The non-fiction genre has appeared the most in the bestseller book list.")
    elif len(nonfic_list) < len(fic_list):
        print("The fiction genre has appeared the most in the bestseller book list.")
    else:
        print("Both fiction and non-fiction have appeared equally in the bestseller books list.")



def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the book list, and how many times it has appeared")
    working_list = list(book_list)
    duplicate_titles = [book for book in working_list if [working_list[book['name']]].count(book) > 1]
    print(duplicate_titles)
    

# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the book list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on the book list")


analysis_three(data_list)
