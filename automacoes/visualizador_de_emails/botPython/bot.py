from botcity.core import DesktopBot
from botcity.maestro import *
import time

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def BotWait(bot, time):
    bot.wait(time)

def PressTab(bot, rng):
    for i in range(rng):
        bot.tab()

def PressShiftTab(bot, rng):
    for i in range(rng):
        bot.shift_tab()

def PressEnter(bot, rng):
    for i in range(rng):
        bot.key_enter()

def RangeEmailsLoop(bot):
    for i in range(4590):
        if bot.find("../bot_images/image copy", matching=0.8, waiting_time=10000):
            bot.click()
        BotWait(bot, 2000)

def main():
    bot = DesktopBot()
    bot.execute("c:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Navegador Opera GX")
    
    BotWait(bot, 1200)
    bot.type_keys("mail.google.com/mail/u/0/")

    PressEnter(bot, 1)
    
    BotWait(bot, 1000)
    PressTab(bot, 22)

    BotWait(bot, 2000)
    PressEnter(bot, 75)

    BotWait(bot, 12000)
    if bot.find("../bot_images/image", matching=0.8, waiting_time=10000):
        bot.click()
        BotWait(bot, 2000)
        RangeEmailsLoop(bot)


if __name__ == '__main__':
    main()