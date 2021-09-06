from tkinter import *

root = Tk()
root.title("progressbar")
root.geometry("640x480")

# row와 column을 이용한 그리드 공부
# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# padx(y) 말고 width, height 로 할 수 있음.
# padx(y)로 할 경우 어떤 열에 포함된 버튼의 텍스트 길이가 길 경우 그 최대 길이를 따르기 때문에 다른 길이들과 다른 경우 width, height를 사용
btn_f16 = Button(root, text="F16", padx=10, pady=10) # 버튼에 padx(y)는 버튼 테두리와 글자 사이의 여백
btn_f17 = Button(root, text="F17", width=10, height=10)
btn_f18 = Button(root, text="F18", padx=10, pady=10)
btn_f19 = Button(root, text="F19", padx=10, pady=10)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # grid에 padx(y)는 버튼들 사이의 여백
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", padx=10, pady=10)
btn_equal = Button(root, text="=", padx=10, pady=10)
btn_div = Button(root, text="/", padx=10, pady=10)
btn_mul = Button(root, text="*", padx=10, pady=10)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 시작 줄
btn_7 = Button(root, text="7", padx=10, pady=10)
btn_8 = Button(root, text="8", padx=10, pady=10)
btn_9 = Button(root, text="9", padx=10, pady=10)
btn_minus = Button(root, text="-", padx=10, pady=10)
btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_minus.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_4 = Button(root, text="4", padx=10, pady=10)
btn_5 = Button(root, text="5", padx=10, pady=10)
btn_6 = Button(root, text="6", padx=10, pady=10)
btn_add = Button(root, text="+", padx=10, pady=10)
btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_1 = Button(root, text="1", padx=10, pady=10)
btn_2 = Button(root, text="2", padx=10, pady=10)
btn_3 = Button(root, text="3", padx=10, pady=10)
btn_enter = Button(root, text="enter", padx=10, pady=10)
btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # rowspan은 합치겠다는 것


btn_0 = Button(root, text="0", padx=10, pady=10)
btn_dot = Button(root, text=".", padx=10, pady=10)
btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_dot.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()