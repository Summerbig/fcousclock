import time

def focus_timer(minutes):
    print("Start focusing for {} minutes...".format(minutes))
    time.sleep(minutes * 60)
    print("Time's up! Take a break.")

focus_timer(25) # 25分钟专注时间
