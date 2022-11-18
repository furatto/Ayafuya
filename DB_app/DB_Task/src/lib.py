import os
import sqlite3

# データベースに接続
con = sqlite3.connect('./main.db')  # dbの作成 すでにある場合は接続
cur = con.cursor()  # sqlite操作のためのカーソル作成


def Start():
    # ここからcloseの間で処理を書く
    # テーブルの作成
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Main(id INTEGER PRIMARY KEY AUTOINCREMENT,name text,info text)")  # テーブル作成,Intenger ~ Autoincrementでidを自動生成s
    # ---------ここから下にメイン処理を書く
    cur.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'Main'")
    main(n=0)


def page(n):
    cur.execute("select * from Main limit 5 offset %s" %
                (n))  # テーブル内容を1行ずつ表示する
    for i in range(5):
        print("|", cur.fetchone())


def main(n):
    # dbの作成 すでにある場合は接続
    cur.execute("SELECT COUNT(id) FROM Main")  # レコード(行数)の総数を取得
    page(n)

    # メインのcui画面情報 ユーザ用
    print("\n1:データ入力 2:データ削除 3:データ参照 4:次のページ 5:前のページ 999:終了")
    select = input()
    if select == "1":
        os.system("clear")
        try:
            a, b = input("データ(コマンドと出力結果)を入力してください\nスペースで区切ること:").split()
        except ValueError:
            print("コマンドと情報の間にスペースを開けてください。又は情報を2つ入力してください")
            return main(n)
        write_DB(a, b)
        os.system("clear")
        return main(n)
    elif select == "2":  # データ削除プログラム
        os.system('clear')
        name = input("削除するコマンド名を入力してください:")
        delete_DB(name)
        return main(n)
    elif select == "3":  # データ参照プログラム
        os.system('clear')
        name = input("探したいコマンド名を入力して下さい:")
        search_DB(name)
        return main(n)
    elif select == "4":  # 次のページへ
        os.system("clear")
        n += 1
        return main(n)
    elif select == "5":  # 前のページへ
        os.system("clear")
        if n == 0:
            return main(n)
        else:
            n -= 1
            return main(n)
    elif select == "999":  # 終了
        return Quit()
    else:
        os.system('clear')
        print("write again\n")
        return main(n)


def Quit():  # 終了関数
    os.system('clear')
    cur.execute("DELETE FROM Main")
    con.commit()
    con.close()  # データベースを閉じる　これがないとまずい
    print("See you next time...")
    return 0


def First(n):
    os.system("clear")
    if n == "1":
        Start()
    elif n == "2":
        Quit()


def write_DB(name, info):
    # cur.execute("INSERT INTO 'Main'SELECT '{0}' AS 'name', '{1}' AS 'info'".format(name, info))  # データ登録
    cur.execute(
        "insert into Main(name,info) values ('{0}','{1}')".format(name, info))
    con.commit()  # データ登録の反映


def search_DB(name):
    cur.execute(
        "select * from Main where name = '{0}'".format(name))
    return print(cur.fetchone(), "\n")


def delete_DB(name):
    cur.execute("DELETE FROM Main WHERE name = '{0}'".format(name))


if __name__ == "__main__":
    Start()
    Quit()
    First()
    page()
    write_DB()
    search_DB()
    delete_DB()
