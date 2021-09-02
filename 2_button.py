from tkinter import *

root = Tk()
root.title("New page")      # 창 제목

btn1 = Button(root, text="버튼1")   # 이 코드만 작성하면 버튼 안보임
btn1.pack()                         # 이 코드까지 작성해야함

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")  # 이것을 포함해서 버튼1, 2, 3의 text 길이가 더 길어지면 가로 세로 길이도 더 길어진다.
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")   # 버튼의 가로와 세로 길이 고정. (text의 길이가 더 길어져도 가로 세로 길이 변화 x)
btn4.pack()

btn5 = Button(root, fg="green", bg="yellow", text="버튼5")  # fg = 글자색 / bg = 배경색
btn5.pack()

photo = PhotoImage(file="./ExitButton.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")
btn7 = Button(root, text="동작 버튼", command=btncmd)
btn7.pack()

root.mainloop()
