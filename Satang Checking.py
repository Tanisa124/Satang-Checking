from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from satang_pro import SatangPro
from datetime import datetime
#getting from satangpro personal account
API_KEY = "delete"
SECRET_KEY = "delete"

token = "delete"

def select(coin):
    API_KEY = "delete"
    SECRET_KEY = "delete"
    sp = SatangPro(api_key = API_KEY, secret_key = SECRET_KEY)
    if coin == 'dot':
        dot = sp.orders(pair = 'dot_thb')
        return dot

bid = (select('dot')['bid'])[:6]
offer = (select('dot')['ask'])[:6]

def check(volume):
    check_now =  str(); count = 0
    for i in volume:
        check_now = check_now + 'Price : ' + i['price']  +" "+'Amount : ' + i["amount"]
        count += 1
        if count != 6:
            check_now += "\n"
    return check_now

#for my chatbot
line_bot_api = LineBotApi('delete')

def linebreak(t):
    uid = "delete"
    return  line_bot_api.push_message(uid, TextSendMessage(text ="-------------------------"))


def name(n):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    uid = "delete"
    if n == 'dot':
        return line_bot_api.push_message(uid, TextSendMessage(text ="Dot Info at "+current_time))

def info(coin):
    uid = "delete"
    if coin == 'dot':
        bid_now = check(bid)
        offer_now = check(offer)
        return  line_bot_api.push_message(uid, TextSendMessage(text = "Bid_Now :"+'\n'+ bid_now )),linebreak('') ,line_bot_api.push_message(uid, TextSendMessage(text =  "Offer_Now :"+'\n'+ offer_now ))

name('dot')
info('dot')
linebreak('')
