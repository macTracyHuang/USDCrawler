from bs4 import BeautifulSoup
import requests

def task(event=None,context=None):
    price=getData()
    if float(price) < 30.2:
        send_message("Time to Buy Me:" + getData())
        return "cool"
    else:
        return "oops"

def getData():
    urlpage='https://rate.bot.com.tw/xrt?Lang=zh-TW'

    #save html content
    page=requests.get(urlpage)

    #encode with format utf-8
    page.encoding = 'utf-8'

    #Parse html
    soup=BeautifulSoup(page.text,'html.parser')

    usd_sell=soup.find_all('td', class_='rate-content-sight').pop(1).text

    return usd_sell


#line notification

def send_message(msg):
    import sys
    try:
        token = 'TnBt2X4yFBGA3wwph8ktRzIFe9QxO2N4D9Xr8uHtEyx'
    except KeyError:
        sys.exit('LINE_TOKEN is not defined!')

    """Send a LINE Notify message (with or without an image)."""

    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': msg}
    # files = {'imageFile': open(img, 'rb')} if img else None
    URL = 'https://notify-api.line.me/api/notify'
    r = requests.post(URL, headers=headers, params=payload)

    return r.status_code


#if __name__ == '__main__':
    #task()
