from __future__ import print_function, division

try:
    import tkinter as tk
    import configparser as configparser
    from tkinter.filedialog import askdirectory
except ImportError:
    # I guess we're running Python2
    import Tkinter as tk
    import ConfigParser as configparser
    from tkFileDialog import askdirectory


def get_directory(entry):
    dir_ = askdirectory()
    print(dir_)
    entry.delete(0, tk.END)
    entry.insert(0, dir_)


root = tk.Tk()
root.title('Simple Importer')

row = 0
label = tk.Label(root, text='Source:')
label.grid(row=row, column=0, sticky=tk.W)
src_entry = tk.Entry(root)
src_entry.grid(row=row, column=1, sticky=tk.E+tk.W)
btn_src_browse = tk.Button(root, text='Browse...', command=lambda: get_directory(src_entry))
btn_src_browse.grid(row=row, column=2, sticky=tk.W)

row = 1
label = tk.Label(root, text='Destination:')
label.grid(row=row, column=0, sticky=tk.W)
dst_entry = tk.Entry(root)
dst_entry.grid(row=row, column=1, sticky=tk.E+tk.W)
btn_dst_browse = tk.Button(root, text='Browse...', command=lambda: get_directory(dst_entry))
btn_dst_browse.grid(row=row, column=2, sticky=tk.W)

row = 2
btn_import = tk.Button(root, text='Import')
btn_import.grid(row=row, column=0, columnspan=3, sticky=tk.E+tk.W)


if __name__ == '__main__':
    root.mainloop()
