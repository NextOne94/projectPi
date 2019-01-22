import socket
import tkinter as tk

window = tk.Tk()

window.title("Test UI Client")

window.geometry("400x400")

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.connect((host,port))

        
#- - - - FUNCTIONS- - - - -
def send_data():
        data2Server = str(entry1.get())
        s.send(data2Server.encode('utf-8'))

        return s.recv(1024).decode('utf-8')

def recv_data():
        dataFserver = send_data()

        data_display = tk.Text(master = window, height = 10, width = 10)
        data_display.grid(column = 0, row = 3)
        data_display.insert(tk.END, dataFserver)


#- - - - LABEL - - - -
label1 = tk.Label(text = "Hello world. ")
label1.grid(column = 0, row = 0)

label2 = tk.Label(text = "What is your Number? ")
label2.grid(column = 0, row = 1)


#- - - -Entry field- - - - 
entry1 = tk.Entry()
entry1.grid(column = 1, row = 1)

#- - - -BUTTON- - - -
button1 = tk.Button(text = "Clike me" , command = recv_data )
button1.grid(column = 0, row = 2)

window.mainloop()
