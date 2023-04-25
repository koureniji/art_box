import openai
import requests
import qrcode

from PIL import Image
import numpy as np

print("gogogo")


class Com:
    # api-key
    def __init__(self, prompt, pic_path):
        self.que = prompt
        self.pic_path = pic_path
        self.url = "labs.openai.com"
        # open_ai_API-Key
        self.key = "xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

        # Da-Vinci parameters
        self.creativity = 1  # 0 = min; 1 = max
        self.max_tokens = 175  # how many tokens  on answer
        self.double_gpt = True
        # DALL-E parameters
        self.pic_size = "1024x1024"  # picture resolution "512x512" // "1024x1024"
        self.pic_n = 1  # number of pictures

    def gpt_request(self):
        openai.api_key = self.key
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.que,
            temperature=self.creativity,
            max_tokens=self.max_tokens,
        )
        ans = resp.choices[0].text  # type: ignore
        self.dalle_prompt = ans.replace("\n", "")
        ######################################
        # DEBUG output
        print("######################################")
        print("#########GPT Answer is")
        print("######################################")
        print(self.dalle_prompt)
        ######################################

    def gpt_request_2nd(self):
        openai.api_key = self.key
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt="Describe following more creativley abstract: '" + self.dalle_prompt + "'",
            temperature=self.creativity,
            max_tokens=self.max_tokens,
        )
        ans = resp.choices[0].text  # type: ignore
        self.dalle_prompt = ans.replace("\n", "")
        ######################################
        # DEBUG output
        print("######################################")
        print("#########GPT Answer is")
        print("######################################")
        print(self.dalle_prompt)
        ######################################

    # make DALL-E create "p_n" new pic on "p_prompt" in "p_size"
    def dalle_request(self):
        # pass API key to API
        openai.api_key = self.key
        self.image = openai.Image.create(
            prompt=self.dalle_prompt, n=self.pic_n, size=self.pic_size
        )
        ######################################
        # DEBUG output
        print("com.dalle_request check ..")
        ######################################

    def get_url(self):
        self.url = self.image.data[0].url  # type: ignore
        ######################################
        # DEBUG output
        print(self.url)
        ######################################

    def download_image(self):
        img_data = requests.get(self.url).content
        with open(self.pic_path, "wb") as handler:
            handler.write(img_data)
        ######################################
        # DEBUG output
        print("com.download_image check .. file_path=" + self.pic_path)
        ######################################

    # def jpgToBmp(self):
        # # import image
        # img = Image.open(self.pic_path)
        # # convert to 256x256
        # img = img.resize((256, 256))
        # # turn into list of pixels
        # ary = np.array(img)

        # # Split the three color-channels
        # r, g, b = np.split(ary, 3, axis=2)
        # r = r.reshape(-1)
        # g = r.reshape(-1)
        # b = r.reshape(-1)

        # # Standard RGB to grayscale
        # bitmap = list(
            # map(lambda x: 0.299 * x[0] + 0.587 *
                # x[1] + 0.114 * x[2], zip(r, g, b))
        # )
        # bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
        # bitmap = np.dot((bitmap > 128).astype(float), 255)
        # # save BMP-image
        # im = Image.fromarray(bitmap.astype(np.uint8))
        # self.bmp_path = self.pic_path[:-3] + "bmp"
        # im.save(self.bmp_path)
        # print("bmp converted at ... bmp_path=" + self.bmp_path)

    def urlToQr(self):
        # 111x111 bmp qr-code
        qr = qrcode.QRCode(version=1,
                           box_size=3,
                           border=4
                           )
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='white',
                            back_color='black')
        img.save(self.pic_path[:-9] + ".bmp")  # <-- qr code path

    def communicate(self):
        self.gpt_request()
        if self.double_gpt:
            self.gpt_request_2nd()
        self.dalle_request()
        self.get_url()
        self.download_image()
        #self.jpgToBmp()
        self.urlToQr()
        return self.dalle_prompt


######################################
# DEBUG get user input
def get_user_input():
    que = input("Enter Prompt: ")
    return que


######################################

######################################
# DEBUG output
print("logic.com check")
######################################
