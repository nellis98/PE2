def main():
    book_titles = []
    count = 0
    while count < 10:
        title = input(f"Enter book title {count+1}: ")
        book_titles.append(title.title())
        count += 1
    sorted_list = sorted(book_titles)
    print("Sorted list of book titles: ")
    for book in sorted_list:
        print(book)
main()