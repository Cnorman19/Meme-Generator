import urllib.request
import bs4 as bs

new_images = []


class Image_Generation:

    def get_Images():
        url = 'https://imgur.com/r/meme'
        values = {}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        resp = urllib.request.urlopen(req).read()
        soup = bs.BeautifulSoup(resp, 'lxml')


        for each_img in soup.find_all('img'):
            new_images.append("https:" + each_img.get('src'))

        print(new_images)

