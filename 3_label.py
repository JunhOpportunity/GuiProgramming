from tkinter import *

root = Tk()
root.title("label practice")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="./ExitButton.png")
label2 = Label(root, image=photo)
label2.pack()

# 버튼 누르면 레이블 값 변경
def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="./x.png")
    label2.config(image=photo2)

btn= Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()