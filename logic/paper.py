#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import logging

from lib.waveshare_epd import epd7in5_V2

from PIL import Image, ImageDraw, ImageFont

# logging.ERROR for errors only
logging.basicConfig(level=logging.DEBUG)


class Paper:
    def __init__(self, pic_path, gpt_answ):
        logging.info("INIT")
        self.epd = epd7in5_V2.EPD()
        self.text = gpt_answ
        #self.bmp_path = pic_path[:-3] + "bmp"
        self.qr_code_path = pic_path[:-9] + ".bmp"

        self.font_path = "text/amtyfont.ttf"

    def sketchInit(self):
        self.epd.init()
        self.epd.Clear()

        logging.info("def font src..")
        self.font22 = ImageFont.truetype(
            self.font_path, 22
        )  # ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 96)
        self.font42 = ImageFont.truetype(self.font_path, 42)
        self.font16 = ImageFont.truetype(
            self.font_path, 16
        )  # ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 16)

        # 255: clear the frame
        self.canvas = Image.new("1", (self.epd.width, self.epd.height), 255)
        self.canvas = self.canvas.transpose(Image.ROTATE_180)
        self.sketch = ImageDraw.Draw(self.canvas)

    def sketchHelpers(self):
        logging.info("sketch corner")
        self.sketch.text((2, 2), "(0|0)", font=self.font16, fill=0)
        self.sketch.text((self.epd.width - 64, 2),
                         "(799|0)", font=self.font16, fill=0)
        self.sketch.text(
            (self.epd.width - 72, self.epd.height - 20),
            "(799|479)",
            font=self.font16,
            fill=0,
        )
        self.sketch.text((2, self.epd.height - 20),
                         "(0|479)", font=self.font16, fill=0)

        logging.info("sketch lines")
        # frame canvas
        # sketch.line((epd.width-1,0, epd.width-1, epd.height-1), fill=0)
        # sketch.line((0,epd.height-1, epd.width-1, epd.height-1), fill=0)

        factor = 80
        wdt = 0
        hgt = 0

        # vertical lines
        while wdt <= self.epd.width:
            if wdt >= self.epd.width:
                wdt = self.epd.width - 1
            self.sketch.line((wdt, 0, wdt, self.epd.height), fill=0)
            wdt += factor

        # horizontal lines
        while hgt <= self.epd.height:
            if hgt >= self.epd.height:
                hgt = self.epd.height - 1
            self.sketch.line((0, hgt, self.epd.width, hgt), fill=0)
            hgt += factor

    def sketchContent(self):
        # CONTENT?!?
        logging.info("sketch text")
        self.sketch.text((320, 16), self.text, font=self.font22, fill=0)
        
        # sketch dalleimage bmp file
        #logging.info("sketch bmp")
        #image = Image.open(self.bmp_path)
        #self.canvas.paste(image, (64,224))
        
        # sketch qr-code bmp
        logging.info("sketch qr-code")
        qr_code = Image.open(self.qr_code_path)
        self.canvas.paste(qr_code, (0,120))


    def printPaper(self):
        logging.info("load buffer..")
        self.epd.display(self.epd.getbuffer(self.canvas))
        time.sleep(2)

        logging.info("goto sleep...")
        self.epd.sleep()

    def draw(self):
        try:
            self.sketchInit()
            # self.sketchHelpers()
            self.sketchContent()
            self.printPaper()

        except IOError as e:
            logging.info(e)
