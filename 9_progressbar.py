import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("progressbar")
root.geometry("640x480")

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 정해지지 않음. 직사각형 블럭 왔다갔다
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 게이지 차오름
progressbar.start(10) # 10 m/s 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지
btn = Button(root, text="중지", command=btncmd)
btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

# ★★★★★★★★★★ 아래 함수 잘 이해 X ★★★★★★★★★★★★
def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i)
        progressbar2.update() # 매번 GUI 업데이트. 이거 안쓰면 그냥 한번에 없다가 참
        print(p_var2.get())
btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()