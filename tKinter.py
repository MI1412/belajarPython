# tkinter adalah untuk membuat GUI 
import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg='grey')
window.geometry('300x200')
window.resizable(False,False)
window.title('say hello')

# frame input
input_frame = ttk.Frame(window)
# penempatan grid,pack,place
input_frame.pack(padx=10,fill='x',expand=True)

# variabel dan fungsi

nama_depan_label = ttk.Label(input_frame,text='Nama Depan')
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)

nama_belakang_label = ttk.Label(input_frame,text='Nama Belakang')
NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
def tombol_klik():
    print(NAMA_DEPAN.get(), NAMA_BELAKANG.get())
    pesan = f"halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title='yoo',message=pesan)


# komponen - komponen
# 1.label nama depan
nama_depan_label.pack(padx=5,pady=1,fill='x',expand=True)

# 2. entry nama depan
nama_depan_entry.pack(padx=5,pady=2,fill='x',expand=True)

# 3.label nama belakang
nama_belakang_label.pack(padx=5,pady=1,fill='x',expand=True)

# 4. entry nama belakang
nama_belakang_entry.pack(padx=5,pady=2,fill='x',expand=True)

# 5. tombol 
say_button = ttk.Button(input_frame,text='katakan hai',command=tombol_klik)
say_button.pack(fill='x',expand=True,pady=10)

# main window
window.mainloop()


