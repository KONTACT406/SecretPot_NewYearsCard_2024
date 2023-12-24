import random
import time
import tkinter as tk
from tkinter import ttk

ronde_b = "ロンド B スクエア"
biz_ud = "BIZ UDゴシック"

window_size_horizontal = 1024
window_size_vertical = 768
title_main_str = "闇鍋★年賀状★2024"

# リストの準備
title = []
member = ["A氏", "B氏", "C氏"]
member_num = len(member)
color = ["赤", "青", "緑"]
who = ["鷹", "獅子舞", "みかん"]
where = ["富士山", "こたつ", "神社"]
what = ["凧揚げをしている", "寝ている", "おせちを食べている"]

# GUIの設定
root = tk.Tk()
root.title(title_main_str)
root.geometry(f"{window_size_horizontal}x{window_size_vertical}")

# Textウィジェットの作成
text_widget = tk.Text(root, font=(biz_ud, 16), wrap=tk.WORD)
text_widget.pack(pady=20)

# ランダムな抽選
def RandomChoose():
    global member, color, who, where, what

    selected_member = random.choice(member)
    member.remove(selected_member)

    selected_color = random.choice(color)
    color.remove(selected_color)

    selected_who = random.choice(who)
    who.remove(selected_who)

    selected_where = random.choice(where)
    where.remove(selected_where)

    selected_what = random.choice(what)
    what.remove(selected_what)

    return selected_member, selected_color, selected_who, selected_where, selected_what

def Display(index=0):
    if index < member_num:
        selected_member, selected_color, selected_who, selected_where, selected_what = RandomChoose()

        text = f"{selected_member}："
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        text = f"{selected_color}色の"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        text = f"{selected_who}が"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        text = f"{selected_where}で"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        text = f"{selected_what}\n"
        text_widget.insert(tk.END, text)
        root.update()
        time.sleep(2)

        root.after(10000, Display, index + 1)  # 0ミリ秒後に次のテキストを表示
    else:
        text_widget.insert(tk.END, "抽選終了\n")

# 最初のテキスト表示をトリガー
Display()

# GUIを表示
root.mainloop()

