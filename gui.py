import trans as trs
import os
from tkinter import *
from tkinter import messagebox
 
#This file make GUI for trans.py
def clicked_new():
    """ """
    cmd_new = "python3 text.py"
    os.system(cmd_new)
def clicked_upgit():
    """ """
    cmd_upgit = "python3 upgit.py"
    os.system(cmd_upgit)
    messagebox.showinfo('Thông báo!','Đã tạo ra file index.html, bạn cần tài khoản github để tạo trang web github cho riêng mình và đưa file index.html cùng thư mục download lên đó. Trang web ví dụ: nguyenthe123.github.io')
def clicked_remove_data():
    """ """
    cmd_rm = "rm word.html"
    os.system(cmd_rm)
    messagebox.showinfo('Thông báo!','Đã xóa dữ liệu cũ')
def clicked_infor():
    """ """
    messagebox.showinfo('Thông báo!','Ứng dụng này dùng để tra nhiều từ, được viết bởi duythe.276051@gmail.com')
window = Tk()
window.title("Search For Words App")
window_height = 500
window_width = 900
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
lbl = Label(window, text="Xin chào, đây là ứng dụng dùng để tra từ.",font=("Arial Bold",22))
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
menu.add_cascade(label='Tệp', menu=new_item)
new_item.add_command(label='Mở cửa sổ mới', command = clicked_new)
new_item.add_command(label='Tải lên Github', command=clicked_upgit)
new_item.add_command(label='Xóa dữ liệu', command=clicked_remove_data)
new_item.add_command(label='Thông tin', command=clicked_infor)
new_item.add_command(label='Thoát', command = window.destroy)
window.config(menu=menu)
#lbl.grid(column=1, row=1)
lbl.place(x=63, y=60)
lbl2 = Label(window, text="Nhập từ:",font=("Arial",16))
lbl2.place(x=110, y= 185)
lbl2 = Label(window, text="Chú ý: Nhập đúng quy chuẩn văn bản thông thường.",font=("Helvetica Italic",12))
lbl2.place(x=180, y= 258)
txt = Entry(window)
#txt.grid(column=1, row=2)
txt.place(x=230, y=150)
txt.place(width=450, height = 100)
def clicked():
    """ When click """
    textn = txt.get()
    text_not_change = textn
    if textn[len(textn)-1] == '.':
        textn = textn[0:len(textn)-1]
 #      print(text)
    sentences = textn.split('.')
 #   print(sentences)
    for sentence in sentences:
        if sentence[0] == ' ':
            sentence = sentence[1:len(sentence)-1]
    for sentence in sentences:
        if sentence[len(sentence)-1] == ' ':
            sentence = sentence[0:len(sentence)-1]
    for sentence in sentences:
        words = sentence.split()
        for word in words:
                word = trs.convert_to_lower_case(word)
                trs.creat_htmlfile()
                stt = 1
                stt = trs.counting_words(stt)
 #              print("Tim kiem tu so " + str(stt))
                trs.download_image_from_google(word)
                inf_image_file = trs.change_name_of_image_file(word)
                path = trs.convert_png_to_jpg(word, inf_image_file)
 #              print("\n Tai file image cua tu ve " + path)
                trs.creating_html_file(word,stt,path)
 #              print("Tao file html")
    lbl.configure(text= 'Đã tìm và lưu vào file word.html, tìm tiếp:' )
def clicked2():
    """ When click """
    cmd = "firefox word.html"
    os.system(cmd)
btn = Button(window, text="Tìm kiếm", command=clicked)
btn.place(x=400, y=300)
btn2 = Button(window, text="Xem kết quả", command=clicked2)
btn2.place(x=385,y=400)
window.mainloop()

