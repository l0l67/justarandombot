from lxml import html
import requests

base_url = "https://r6stats.com/de/search/"
username = "0"
def search(username):
    page = requests.get(base_url + username + "/pc")
    tree = html.fromstring(page.content)
    global ges

    kd = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[1]/div[2]//text()'))
    win_rate = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[2]/div[2]//text()'))
    k_pmatch = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[3]/div[2]//text()'))
    kills = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[4]/div[2]//text()'))
    wins = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[5]/div[2]//text()'))
    played = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[6]/div[2]//text()'))
    deaths = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[7]/div[2]//text()'))
    lost = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[8]/div[2]//text()'))
    playtime = ''.join(tree.xpath('//*[@id="__layout"]/div/div[4]/div[2]/div/main/div/div[2]/div[2]/section[1]/div/div[9]/div[2]/button//text()'))

    ges = "KD: " + kd + "\n" + "Gewinnrate: " + win_rate + "\n" + "Kills per Match: " + k_pmatch + "\n" + "Kills: " + kills + "\n" + "Tode: " + deaths + "\n" + "Gewonnen: " + wins + "\n" +"Gespielte Spiele: " + played + "\n" + "Verloren: " + lost + "\n" + "Spielzeit: " + playtime

    return ges
