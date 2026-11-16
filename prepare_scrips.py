import sys


def main():
    """Input a text file, and output file. Text file is of a chapter of scripture, excluding the header, this will parse
     it into a single line of text place in the output file
    """
    if len(sys.argv) == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        with open(arg1) as file:
            text = file.read()
        for character in text:
            if character in ["0", "1", "2", "3", "4", '5', '6', '7', '8', '9']:
                continue
            elif character == '\n':
                character = " "
            with open(arg2, 'a') as file:
                file.write(character)
    else:
        for file in sys.argv[1:-1]:
            with open(file) as f:
                text = f.read()
            with open(sys.argv[-1], 'a') as f:
                f.write(text)
                f.write('\n')


if __name__ == '__main__':
    main()
