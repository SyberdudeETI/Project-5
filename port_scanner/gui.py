import tkinter as tk
from tkinter import Text
import port_scanner

class windows(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('PORT SCANNER')
        self.geometry('600x600' )
        self.configure(bg='black')



        self.E1= tk.Entry(self, bg='red')
        self.E1.pack(pady=10)
        self.btnE1= tk.Button(self, text='IP Absenden', bg='red', command= self.ip_Speicher)
        self.btnE1.pack(pady=10)





        btn1 = tk.Button(self, text='SCAN',  bg= 'red', height=2, width=9, command= self.scan)
        btn1.pack(pady=10)
        btn2 = tk.Button(self, text='EXIT', bg= 'red', height=2,  width=9, command= self.destroy)
        btn2.pack( pady=10)



        self.text = tk.Text(width= 500, height= 50, background='black', fg='red')
        self.text.pack( pady=20)




        self.mainloop()





    def ip_Speicher(self):
        self.ip1 = self.E1.get()
        self.text.insert(tk.END, "Target IP: " + self.ip1)
        if self.ip1 == '':
            self.text.insert(tk.END, '!ERROR! IP IS EMPTY\n')

    def scan(self):
        if not hasattr(self, 'ip1') or self.ip1 == '':
            self.text.insert(tk.END, '!ERROR! IP IS EMPTY\n')
            return
        ergebnis1 = port_scanner.scan(self.ip1, 80)
        if ergebnis1:
            self.text.insert(tk.END, 'Port: 80 - OFFEN\n')
        else:
            self.text.insert(tk.END, 'Port: 80 - GESCHLOSSEN\n')
        ergebnis2 = port_scanner.scan(self.ip1, 443)
        if ergebnis2:
            self.text.insert(tk.END, 'Port: 443 - OFFEN\n')
        else:
            self.text.insert(tk.END, 'Port: 443 - GESCHLOSSEN\n')
        ergebnis3 = port_scanner.scan(self.ip1, 22)
        if ergebnis3:
            self.text.insert(tk.END, 'Port: 22 - OFFEN\n')
        else:
            self.text.insert(tk.END, 'Port: 22 - GESCHLOSSEN\n')
        self.text.see(tk.END)





if __name__ == '__main__':
    windows()