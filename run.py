import time

from booking.sauce import Sauce

with Sauce() as bot:
    bot.get_webpage()
    bot.username_entry()
    bot.password_entry()
    bot.login_button()
    time.sleep(99999)
