from lxml import html
import requests

base_url = "https://minecraft-heads.com/custom-heads/search?searchword="
url = "https://minecraft-heads.com/custom-heads"
img_url = "https://minecraft-heads.com"
sterm = "0"
selector = "2"
result = 0
def search(sterm, result):
    global cmd
    global data
    cmd = []
    data = []
    href_l = []
    counter = result
    img = []
    if result == 0:
        result = 2
    else:
        result = 2
        i = 0
        while i < int(counter):
            page = requests.get(base_url + sterm)
            tree = html.fromstring(page.content)

            first_res = tree.xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/div[2]/div[' + str(result) +']/a')

            elt = ""
            for elt in first_res:
                href = elt.attrib['href'], elt.text_content().split(" ")
                href = href[0].replace('/custom', '')
                href_l.append(href)
                print("href  " + href)


            page = requests.get(base_url + sterm)
            tree = html.fromstring(page.content)

            img.append(tree.xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/div[2]/div[' + str(result) +']/a/img/@src'))            

            try:
                page = requests.get(url + href_l[i])
                print(url + href_l[i])
                tree = html.fromstring(page.content)
                command = tree.xpath('//*[@id="UUID-Code-MC1-16"]')
                for t in command:
                    command = t.text_content()
                #command = command.replace('\\', '\\\\') 
                #python macht aus "\\" "\"
                command = "```" + command + "```"
                cmd.append(command)
                image_url = img_url + ''.join(img[int(i)])
                data.append(requests.get(image_url).content)
                #with open('discord_temp_imgs/image.jpg', 'wb') as outf:0
                #    outf.write(data)

                #data[i] = bytes(data[i])
            except UnboundLocalError as e:
                command = "404 not found, spelled correctly?"
                cmd.append(command)
                with open('discord_temp_imgs/404.png', 'rb') as er_img:
                    data.append(er_img.read())


            i += 1
            result += 1
    return data
    return cmd


def start_thread(sterm, result):
    t1 = threading.Thread(target = search, args = (sterm, result))
    t1.start()
