from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)    # extended : 여러개 선택 가능 / single : 하나만 선택 가능 / height : 0은 리스트 전부 다 보여줌. 특정 숫자 입력하면, 그 숫자 이상의 리스트들은 키보드로 스크롤해야 볼 수 있음
listbox.insert(0, "딸기")
listbox.insert(1, "바나나")
listbox.insert(2, "사과")
listbox.insert(END, "복숭아")   # 인덱스 입력 안해도 자동으로 맨 뒤에 저장
listbox.insert(END, "포도")
listbox.pack()



def btncmd():
    listbox.delete(END)         # 맨 뒤 항목 삭제
    listbox.delete(0)           # 맨 앞 항목 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인
    print("1번째부터 3번쨰까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (위치로 반환 = 인덱스로 반환)
    print("선택된 항목 :", listbox.curselection())
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()