from Pull_Image_From_Site import *
import urllib.request
import random



class DownloadImage:

    def download():

        if len(new_images) == 0:
            x = random.randint(1, 2)
        else:
            x = random.randint(1, len(new_images))

        urllib.request.urlretrieve(str(new_images[x]), "test.jpg")