from pathlib import Path

def word_count(path):
    '''Count the aproximate number of words in a file.'''

    filename_display = path.name

    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {filename_display} doesn't exist.")
    else:
        #Count the aproximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename_display} has about {num_words} words.")

filenames = ["alice.txt", "frankenstein.txt", "moby_dick.txt", "lupin.txt" , "romeo_and_juliet.txt"]

for filename in filenames:
    path = Path(f"books/{filename}")
    word_count(path)