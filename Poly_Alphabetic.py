from tkinter import *

x_window = Tk()
output_text = StringVar()
check_space = IntVar()
txt_plain_text = Entry(x_window, width=35, font=10)
txt_key = Entry(x_window, width=20, font=10)

ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']


# encryption
def encryption(message, key, space_ch):
    print(message,key)
    if space_ch == 0:
        ls.insert(0, ' ')
    elif space_ch == 1 and ls[0] == ' ':
        ls.pop(0)

    ls_message_cipher = []
    len_message = len(message)
    i = 0
    x = 0

    while i < len_message:
        if message[i] == ' ' and space_ch == 0:
            ls_message_cipher.append(ls[(ls.index(key[x % len(key)]) + ls.index(message[i])) % len(ls)])
            i += 1
            x += 1
        elif message[i] == ' ':
            i += 1
        else:
            ls_message_cipher.append(ls[(ls.index(key[x % len(key)]) + ls.index(message[i])) % len(ls)])
            i += 1
            x += 1
    message_str = ""

    for item in ls_message_cipher:
        message_str += item

    output_text.set("Cipher text : " + message_str)
    # print(chr(key))
    # print(message, key, type(key))


# decryption
def decryption(message, key, space_ch):
    if space_ch == 0:
        ls.insert(0, ' ')
    elif space_ch == 1 and ls[0] == ' ':
        ls.pop(0)

    ls_message_plain_text = []
    len_message = len(message)
    i = 0

    while i < len_message:
        ls_message_plain_text.append(ls[(ls.index(message[i]) - ls.index(key[i % len(key)])) % len(ls)])
        i += 1
    message_str = ""

    for item in ls_message_plain_text:
        message_str += item

    output_text.set("Plain Text : " + message_str)
    print(message_str)


def click_btn1():
    encryption(str(txt_plain_text.get()).lower(), str(txt_key.get()).lower(), check_space.get())


def click_btn2():
    decryption(str(txt_plain_text.get()).lower(), str(txt_key.get()).lower(), check_space.get())


def main():
    # frame window
    # x_window.configure(background="black")
    x_window.title("Simple Shift Vignere")
    x_window.geometry("500x300")

    # labels
    lbl_txt1 = Label(x_window, text="Text : ", padx=5, pady=5)
    lbl_txt2 = Label(x_window, textvariable=output_text, padx=5, pady=5, font=10)
    lbl_key = Label(x_window, text="Key : ", padx=5, pady=5)
    lbl_txt1.place(x=10, y=10)
    lbl_key.place(x=10, y=50)

    # text
    txt_plain_text.focus()
    txt_plain_text.place(x=60, y=15)
    txt_key.place(x=60, y=55)

    # Check Button
    ch_btn = Checkbutton(x_window, text="Ignore space", variable=check_space)
    ch_btn.place(x=300, y=50)

    # Button and check button
    btn_encrypt = Button(x_window, text="Encrypt", padx=5, pady=5, command=click_btn1, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")
    btn_decrypt = Button(x_window, text="Decrypt", padx=5, pady=5, command=click_btn2, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")

    btn_encrypt.place(x=100, y=110)
    btn_decrypt.place(x=250, y=110)

    lbl_txt2.place(x=60, y=160)
    x_window.mainloop()


if __name__ == '__main__':main()