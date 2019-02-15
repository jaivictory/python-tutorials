# line 1,2 start with usual command line argument handling.
import sys
script, encoding, error = sys.argv
# l-6 main meat of this code function conveniently called "main"
# this will called at the end of this script to get things going.
def main(language_file, encoding, errors):
    line = language_file.readline()#read 1 line from language file
    """ if statement let you make decision in ur python code,you can
test the truth of a variable and based on that truth, READLINE
function will return an empty string when it reaches end of the file
and if line simply tests for empty strings. As long as readline give us
something this will be true and the code under line 16,17 will run,when
it is false,python will skip lines 16,17"""
# in line 17 we calling function inside function(main)
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# defination for print_line function which does actually encoding for language.txt file.
#simple stripping of the trailing \n on the line string
# cooked_string variable from raw_bytes
def print_line(line, encoding, errors):
        next_lang = line.strip()
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes,"<===>",cooked_string)


languages = open("languages.txt",encoding="utf-8")

main(languages, encoding, error)



