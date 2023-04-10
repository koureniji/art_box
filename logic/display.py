import tkinter as tk
import textwrap as tr
from PIL import Image, ImageTk, ImageFont


from logic.paper import Paper
from logic.data import Data


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Window settings
        self.geometry("1440x900")
        self.title("display")

        # first view params
        self.jpg_path = "pics/a_painting_rushed_0-1681121314.jpg"
        self.image = self.load_image()
        self.lyrics = "And the people in the houses \nAll went to the university \nWhere they were put in boxes \nAnd they came out all the same"
        self.artist = "Little Boxes - The Dorian Wood Guilt Trip"
        self.gpt_answer = "This painting is a whimsical interpretation of the familiar phrase 'Little boxes on the hillside'. The image is of a rolling hill, covered in a patchwork of colorful shapes, ranging from triangles and rectangles to circles and stars. The different shapes are made up of a rainbow of bright colors, from bright pinks to vibrant blues, giving the painting a cheery and animated atmosphere. The figures on the hillside are painted in a very haphazard, rushed style. Every shape is unique and uniquely colorful, creating a stimulating scene. The sense of haste and liveliness is maintained by the haze of scribbles behind the shapes, representing their hurried placement on the hillsides. Despite the vibrancy of their shapes and colors, the figures are all the same size, showing that underneath the cheerful chaos, there is in fact uniformity."
        self.gpt_answer = tr.fill(self.gpt_answer, width=45)
        # keys
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.toggle_fullscreen)
        self.bind("<space>", self.new_pic)
        self.bind("q", self.quit_program)

    def toggle_fullscreen(self, event=None):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))

    def quit_program(self, event=None):
        self.quit()

    def new_pic(self, event=None):
        print("new image trigered")

        data = Data("text/boxes.json")
        self.jpg_path, self.lyrics, self.artist, self.gpt_answer = data.newData()
        print("new Data arrived")

        self.image = self.load_image()
        print("image loaded in variable")

        self.image_label.configure(image=self.image)
        self.image_label.image = self.image                         # type: ignore
        print("new image set")

        # lyrics = wrap_text(unf_lyrics, 30)
        self.lyrics_label.configure(text=self.lyrics)
        self.lyrics_label.text = self.lyrics                        # type: ignore
        print("new lyrics set" + self.lyrics)

        self.artist_label.configure(text=self.artist)
        self.artist_label.text = self.artist                        # type: ignore
        print("new artist set" + self.artist)

        self.update()

        self.draw_paper()

    def load_image(self):
        image = Image.open(self.jpg_path)
        image = image.resize((852, 852))  # , Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return image

    def draw_paper(self):
        eink = Paper(self.jpg_path, self.gpt_answer)
        eink.draw()

    def draw_LCD(self):
        self.left_frame = tk.Frame(
            self, width=876, height=900, background="white")
        self.left_frame.pack(side="left")

        self.image_label = tk.Label(self.left_frame,
                                    image=self.image, bg="white")
        self.image_label.place(x=22, y=22)

        self.right_frame = tk.Frame(
            self, width=564, height=900, background="white")
        self.right_frame.pack(side="right")

        self.lyrics_label = tk.Label(
            self.right_frame, text=self.lyrics, font=("American Typewriter", 22), fg="black", bg="white")
        self.lyrics_label.place(x=34, y=342)

        self.artist_label = tk.Label(
            self.right_frame, text=self.artist, font=("American Typewriter", 14), fg="black", bg="white")
        self.artist_label.place(x=170, y=512)

        self.dalle_label = tk.Label(
            self.right_frame, text="by DALL-E 2 ?", font=("American Typewriter", 14), fg="grey", bg="white")
        self.dalle_label.place(x=6, y=849)
