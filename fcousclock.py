
importtime
import tkinter as tk
 
def tick():
    # 获取当前时间
    current_time = time.strftime('%H:%M:%S')
    # 更新标签文本
    clock_label.config(text=current_time)
    # 每1秒调用一次tick函数
    clock_label.after(1000, 
