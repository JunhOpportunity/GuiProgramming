from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장 (????)
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)

chkbox.select() # 자동 체크 처리
chkbox.deselect() # 자동 체크 해제 처리
chkbox.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제 / 1 : 체크
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()