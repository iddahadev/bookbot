# Bookbot

This is my first Python project. It is part of the curriculum on [boot.dev](https://www.boot.dev) to become a Backend Developer!

The project aims to parse a book (.txt file), get the word count and letter occurrences, and print them to the console.

## Features

- Words count
- Letters occurrence
- Print reports with word count and letter occurrence sorted by occurrence count

### Output

```
$ python3 main.py

--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
The 'o' character was found 25225 times
The 'i' character was found 24613 times
The 'n' character was found 24367 times
The 's' character was found 21155 times
The 'r' character was found 20818 times
The 'h' character was found 19725 times
The 'd' character was found 16863 times
The 'l' character was found 12739 times
The 'm' character was found 10604 times
The 'u' character was found 10407 times
The 'c' character was found 9243 times
The 'f' character was found 8731 times
The 'y' character was found 7914 times
The 'w' character was found 7638 times
The 'p' character was found 6121 times
The 'g' character was found 5974 times
The 'b' character was found 5026 times
The 'v' character was found 3833 times
The 'k' character was found 1755 times
The 'x' character was found 677 times
The 'j' character was found 504 times
The 'q' character was found 324 times
The 'z' character was found 243 times
--- End report ---
```

## Run Locally

Clone the project

```bash
git clone https://github.com/iddahadev/bookbot.git
```

Go to the project directory

```bash
cd bookbot
```

Create the `books` directory

```bash
mkdir books
```

Download the [test file](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) used in this project

```bash
curl https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt -o books/frankenstein.txt
```

Run the script

```bash
python3 main.py
```

You can use another text file to test the script. Just make sure to update the `main` function on `line 2`

```python3
def main():
    book_path = "books/file_name.txt"
```

## Lessons Learned

I learned how to open a file, read its content in Python, and do some basic string manipulations.

I want to rewrite the solution with Object Oriented Programming and Functional Programming.

## Feedback

As my first Python program, feedback is more than welcome! You can find me on [X (formerly Twitter)](https://www.x.com/iddahadev) or Discord (@iddahadev).
