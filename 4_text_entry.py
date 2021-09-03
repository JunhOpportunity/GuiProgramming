from tkinter import *
root = Tk()
root.title("text & entry")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")    # 미리 적혀있을 안내 문구, 문자 입력시 사라지나? -> 사라지지 않음.

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")


# 1 : 라인
# 0 : 위치
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 첫 번째 라인의 0번째 인덱스부터 끝까지 text 가져오기
    print(e.get())              # entry 가져오기

    # 내용 삭제
    txt.delete("1.0", END)      # text 내용 삭제
    e.delete(0, END)            # entry 내용 삭제

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()