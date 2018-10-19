from apscheduler.schedulers.blocking import BlockingScheduler
from price_alert import *

def hourJob():
    url = 'https://www.amazon.com/Gaming-i7-8750H-Display-Gigabit-FX504GM-ES74/dp/B07F6K21HJ/'
    content = simple_get(url)
    print(get_price(content))

if __name__ == '__main__':    
    scheduler = BlockingScheduler()
    scheduler.add_job(hourJob, 'interval', minutes=30)
    print("===================scheduler started...")
    scheduler.start()


