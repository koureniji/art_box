from .com import Com
from .text import Text
import textwrap as tr

# ^^ import Pic() and Text() Formater classes ^^


# Data manager class
# - paramter: source file path as String
class Data:
    # 'Konstruktor' - only called on Object creation
    def __init__(self, txt_path):
        self.txt_path = txt_path

        ######################################
        # DEBUG output
        print("data.init [[CHECK]]")
        ######################################

    # the only function "Display.new_pic()" needs to call to generate prompt, text and download JPG + BMP
    # RETURNS: downloaded picture path <String>
    #       // Text Output for Display <String>
    def newData(self):
        # creates txt Object with parameter txt_path
        txt = Text(self.txt_path)

        self.prompt, self.pic_path, self.output, self.artist = txt.newText()

        # creates pic Object with parameter created above
        pic = Com(self.prompt, self.pic_path)
        self.gpt_answer = pic.communicate()
        self.gpt_answer = tr.fill(self.gpt_answer, width=45)
        ######################################
        # DEBUG output
        print("data.generateData [[CHECK]]")
        ######################################

        return self.pic_path, self.output, self.artist, self.gpt_answer
