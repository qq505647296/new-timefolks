import time  
  
def countdown(t):  
    while t:  
        mins, secs = divmod(t, 60)  
        timer = '{:02d}:{:02d}'.format(mins, secs)  
        print(timer, end="\r")  
        time.sleep(1)  
        t -= 1  
        
    print('时间到！')  
  
# 输入你想要专注的时间（以分钟为单位）  
time_in_minutes = int(input("请输入你想要专注的时间（以分钟为单位）："))  
countdown(time_in_minutes * 60) # 将输入的分钟数转换为秒数
