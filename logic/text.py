import random
import json
import time

# ^^ import Pic() and Text() Formater classes ^^

###############
# - todo -
# - make get type function


# Data manager class
# - paramter: source file path as String
class Text:
    ######################################
    # DEBUG output
    print("logic.NewText")
    ######################################

    # 'Konstruktor' - only called on Object creation
    # add type - list of json identifiers
    def __init__(self, txt_path) -> None:
        self.txt_path = txt_path
        self.type = ["tech", "operator", "mood", "lyrics", "output", "artist"]

    # loads text source in class-variable
    def loadTxtSource(self):
        file = open(self.txt_path)
        self.source = json.load(file)

        ######################################
        # DEBUG output
        print("data.loadTxtSource [[CHECK]]")
        ######################################

    # handles all randomness in a request
    # - random tech, artist, mood for prompt
    # - random text passage
    def makeRandom(self):
        # array for results
        self.ids = []
        # for each item in type-list -> random item-position in each type 0 -> x
        for tag in self.type:
            max = len(self.source[tag])
            min = 0
            self.ids.append(random.randrange(min, max, 1))
        ######################################
        # DEBUG output
        print("data.makeRandom [[CHECK]]" + str(self.ids))
        ######################################

    # creates prompt to input into DALL-E
    def makePrompt(self):

        self.tech = self.source[self.type[0]][self.ids[0]]
        # print("tech: ... " + self.tech)
        self.operator = self.source[self.type[1]][self.ids[1]]
        # print("artist: ... " + self.artist)
        self.mood = self.source[self.type[2]][self.ids[2]]
        # print("mood: ... " + self.mood)
        self.text = self.source[self.type[3]][self.ids[3]]
        # print("text: ... " + self.text)

        # create prompt based on returns above
        self.prompt = (
            "Describe "
            + self.tech
            + " as a "
            + self.mood
            + " interpretation of '"
            + self.text
            + "'. Be unique. Try to be different and creative."
        )

        ######################################
        # DEBUG output
        print("data.makePrompt [[CHECK]]")
        print(self.prompt)
        ######################################

    # creates name to save pic as
    def makePicName(self):
        name = (
            self.tech
            + "_"
            + self.mood
            + "_"
            + str(self.ids[3])
            + "-"
            + str(round(time.time()))
        )
        self.pic_name = name.lower().replace(" ", "_")

    # creates path to save pic in
    def makePicPath(self):
        self.pic_path = "pics/" + self.pic_name + ".jpg"

    # gets text for display output from source
    def makeTxtOutput(self):
        # in source json -> of type "german" -> get srandom entry[english]
        self.txt_out = self.source[self.type[4]][self.ids[3]]
        self.artist = self.source[self.type[5]][self.ids[5]]

    # the only function that needs to be called by Data() to get prompt, pic download path and output text
    # RETURNS: prompt for DALL-E to generate picture <String>
    #       // picture path <String>
    #       // Text Output for Display <String>
    def newText(self):
        self.loadTxtSource()
        self.makeRandom()
        self.makePrompt()
        self.makeTxtOutput()
        self.makePicName()
        self.makePicPath()

        ######################################
        # DEBUG output
        print("... prompt: ..." + self.prompt)
        print("... pic_path: ..." + self.pic_path)
        print("... txt_out (lyrics): ..." + self.txt_out)
        print("... artist: ..." + self.artist)
        ######################################

        return self.prompt, self.pic_path, self.txt_out, self.artist


# txt = Text("text/boxes.json")
# a, b, c, d = txt.newText()
