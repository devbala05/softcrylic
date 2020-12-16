# importing the libraries
from bs4 import BeautifulSoup
import requests
import json
import shutil
import os
import re

class Extraction:
    def __init__(self):
        pass

    def do_action(self):
        dir="D:\Softcrylic"
        url="https://hashnode.com/explore"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        author = soup.find(id='__NEXT_DATA__')
        images = [img for img in soup.findAll('img')]
        image_links = [each.get('data-src') for each in images]
        for imglink in image_links:
            if imglink:
                filename = imglink.split('/')[-1]
                filename = filename.split('?')[0]
                r = requests.get(imglink, allow_redirects=True)
                open(filename, 'wb').write(r.content)       
        dirName = 'author_images'
        try:
            path = os.mkdir(dirName)
            print("Directory " , dirName ,  " Created ") 
        except FileExistsError:
            print("Directory " , dirName ,  " already exists") 
####
        author1 = [img for img in soup.findAll('props')]

        #soup1 = BeautifulSoup(html_content)
        #a = [x.extract() for x in author.findAll(['script'])]


        for script in soup(["script"]):
            script.extract()
        #print("Extracted3: %s"%script)
        result = str(author)


        pattern2 = re.compile(r'\s?on\w+="[^"]+"\s?')
        subst = u""
        result1 = re.sub(pattern2, subst, result)





        a = soup.title.string
        b = soup.title.parent.name
        an = soup.find_all('a')
        ans = soup.find(id="link3")

        a = soup.prettify()

        div = soup.div

        mydivs = soup.findAll("div", {"class": "w-full"})
        #print("END:%s"%mydivs)
        j = 0
        #range(4,14)
        data = {}
        data['author_details'] = []
        #for div in mydivs:
        for i in range(4,14):
            div = mydivs[i]
            url = div.find('a')
            link = url.get('href')
            img = div.find('img')
            #imgpath = img.get('data-src')
            print("Author Name: %s"%div.find('a').contents[0])
#           tags = div.find('text-xs')
            tags = div.findAll("div", {"class": "text-xs"})
            tag_array = []
            for i in tags:
                atag = i.find_all('a')
                #tag_array = []
                for tag in atag:
                    tag_array.append(tag.contents[0])
    
    
    
            j=j+1
            data['author_details'].append({
    "auther_name": str(div.find('a').contents[0]),
			"author_tags": str(tag_array),
			"total_followers": "",
			"author_web_url": str(div.find('a')['href']),
			"recent_post": ["", ""]
     })
        with open(dir+'\data.txt', 'w') as outfile:
            json.dump(data, outfile)


ins = Extraction()
ins.do_action()

