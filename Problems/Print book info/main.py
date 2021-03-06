def print_book_info(title, author=None, year=None):
    #  Write your code here
    if (author is None or author == "None") and (year is None or year == "None"):
        print('"{}"'.format(title))
    else:
        author = "" if (author is None or author == 'None') else " by {}".format(author)
        year = "" if (year is None or year == 'None') else " in {}".format(year)
        print('"{}" was written'.format(title) + author + year)
