import tkinter as tk
from tkinter import ttk

import glob

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("300x300")
        self.master.title("Tkinter with Class Template")
        
        #メニューバー作成 
        menubar = tk.Menu(self) 

        #メニューに親メニュー（ファイル）を作成する 
        menu_file = tk.Menu(menubar, tearoff=False) 
        menubar.add_cascade(label='ファイル', menu=menu_file) 

        #親メニューに子メニュー（開く・閉じる）を追加する 
        menu_file.add_command(label='開く', command=self.open_file) 
        menu_file.add_separator() 
        menu_file.add_command(label='閉じる', command=self.close_disp)

        #メニューバーを画面にセット 
        self.master.config(menu = menubar)

        # Widget内容設定
        self.create_widgets()

    def open_file():
        pass

    def close_disp():
        pass

    def create_widgets(self):
        button_hello = ttk.Button(self)
        button_hello.configure(text="Update")
        button_hello.configure(command = self.input_folder)
        button_hello.pack(fill="x")
        pass

    def callBack(self):
        pass

    def input_folder(self):
        # ６次元ファイル作成
        patternnum = 1
        files = glob.glob('./tmp/*.txt')
        matrix_ary = []
        for file in files:
            f = open(file, 'r', encoding='UTF-8')
            data = f.read()

            print(file, '\n' , data)
            if data == "":
                data = " "
            elif '\n' in data:
                data = data.replace('\n', ',')
            data = data.split(',')
            patternnum = patternnum * len(data)
            matrix_ary.append(data)

            print(len(data))

        print(matrix_ary)
        collen = len(matrix_ary)

        # 全行の配列
        # 　Max行 対象要素＊
        result_ary = [[0]* collen] * patternnum

        print('patternnum', ':', patternnum)


        for i in range(0, len(files)):
            now = int(patternnum / len(matrix_ary[i]))
            for j in range(1, now):
                for x in matrix_ary[i]:

                    print(j*matrix_ary[i].index(x)-1) #←計算式として不十分
                    result_ary[j*matrix_ary[i].index(x)-1][i] = x
        print(result_ary)

def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if __name__ == "__main__":
    main()
