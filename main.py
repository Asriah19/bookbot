def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
        return book_text
    
def get_word_count(path_to_book):
    with open(path_to_book, "r", encoding="utf-8") as f:
        book_text = f.read()
        book_word_arr = book_text.split()
        word_count = len(book_word_arr)
        print(f"{word_count} words found in the document")
        

    
def main():
    string_to_log = get_book_text("books/frankenstein.txt")
    get_word_count("books/frankenstein.txt")

main()