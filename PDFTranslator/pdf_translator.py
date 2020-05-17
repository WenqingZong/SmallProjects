from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from googletrans import Translator
from json import JSONDecodeError
from sys import argv
import os


def red_print(string: str) -> None:
    """
    Print a message in red.
    :param string: The string to print.
    :return: None
    """
    print("\033[1;31m", end="")
    print(string)
    print("\033[0m", end="")


TEMP = "temp.txt"


def extract_text(input_file: str) -> None:
    """
    Extract text from the named pdf file, and save result to temp.txt.
    :param input_file: The pdf file to extract
    :return: None
    """
    outfp = open(TEMP, "w", encoding="utf-8")
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, outfp, laparams=LAParams())
    try:
        with open(input_file, 'rb') as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.get_pages(fp):
                interpreter.process_page(page)
    except FileNotFoundError:
        red_print("The file " + input_file + " doesn't exist, program exit!")
        exit()
    finally:
        device.close()
        outfp.close()


def read_temp() -> list:
    """
    Read text from temp.txt, and save each paragraphs into a list.
    :return: list containing all paragraphs.
    """
    with open(TEMP, "r", encoding="utf-8") as file:
        paragraph = ""
        paragraphs = []
        # Sometimes, word is split into two lines, e.g, the ending of line 1:exp-, the beginning of line 2: lore
        word_is_split_into_two_lines = False
        for line in file:
            # Two paragraphs are split by an empty new line.
            if line != "\n":
                line = line.lstrip()
                if word_is_split_into_two_lines:
                    # If word is split into two lines, the beginning of line 2 should be concat to the ending of line 1
                    # The last character of line 1 is "\n"
                    paragraph = paragraph[:-1]
                    word_is_split_into_two_lines = False
                else:
                    paragraph = paragraph[:-1] + " "
                # pdf contains these special character for better reading experience, but we need to convert them back.
                line = line.replace("ﬁ", "fi")
                line = line.replace("ﬀ", "ff")
                line = line.replace("’", "'")
                if len(line) > 2 and line[-2] == "-":
                    # If a word is split into two lines, then the ending of line 1 is "-\n", we need to delete "-".
                    line = line[:-2] + "\n"
                    word_is_split_into_two_lines = True
                paragraph += line
            else:
                paragraphs.append(paragraph)
                paragraph = ""
    return paragraphs


def translate_to_chinese(paragraphs: list, output_file: str = "") -> None:
    """
    Translate the given list, which containing many paragraphs, into Chinese. If no output file is given, then results
    will be shown on stdout.
    :param output_file: The name of the output file, default is empty. If not given, results will be shown on stdout.
    :param paragraphs: A list containing many paragraphs.
    :return: None
    """

    def pretty_write(file, string: str, is_chinese: bool, limit: int = 120) -> None:
        """
        Write a long string to a file, the max length of one line of specified by length.
        :param file: The file to write to.
        :param is_chinese: Indicates if this string is in chinese.
        :param string: The long string to write.
        :param limit: The length limit.
        :return: None
        """
        if is_chinese:
            write_so_far = 0
            for i in range(len(string)):
                # A chinese character is longer than one english character.
                if write_so_far <= limit * 0.6:
                    file.write(string[i])
                    write_so_far += 1
                else:
                    file.write("\n")
                    file.write(string[i])
                    write_so_far = 1
            file.write("\n")
        else:
            words = string.split(" ")
            length_so_far = 0
            for word in words:
                length_so_far += len(word) + 1

                if length_so_far <= limit:
                    file.write(word + " ")
                else:
                    length_so_far = 0
                    file.write("\n")

    translator = Translator()
    if output_file == "":
        # Print result to stdout.
        for paragraph in paragraphs:
            translation = translator.translate(paragraph, dest="zh-CN")
            print(translation.origin, translation.text, "\n")
    else:
        # Write result to the named file.
        with open(output_file, "w", encoding="utf-8") as output:
            for paragraph in paragraphs:
                translation = translator.translate(paragraph, dest="zh-CN")
                pretty_write(output, translation.origin, False)
                pretty_write(output, translation.text, True)
                output.write("\n")


# Example usage: python3 lab10-cryptosystems.pdf
if __name__ == "__main__":
    extract_text(argv[1])
    print("Extraction finished, result is written to " + TEMP)
    paragraphs = read_temp()
    os.remove(TEMP)
    print("Reading finished, " + TEMP + " removed")
    output_file = input("The output file name? If you want to see output shown on stdout, then just press <enter>: ")
    try:
        translate_to_chinese(paragraphs, output_file)
    except JSONDecodeError:
        red_print("\nGoogle API sets a temporary limitation to this IP! This happens because you've already send too "
                  "many queries.\nWait a long time or change to another network, then everything will work again.")
