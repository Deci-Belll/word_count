"""クリップボード内の文字列を取得して文字数を表示する小さなユーティリティ。

使い方:
    1. 対象の文字列をクリップボードにコピーする
    2. 本スクリプトを実行し、Enterキーを押す
    3. クリップボードの文字列と文字数が表示される

このモジュールは pyperclip に依存します。
"""

import pyperclip

# 最大許容文字数
MAX_LENGTH = 24


def clip() -> str:
    """クリップボードから文字列を取得して返す。"""
    add_clip = pyperclip.paste()
    return add_clip


def main() -> None:
    """ユーザー入力を待ち、クリップボードの文字列を表示して文字数をチェックする。"""
    input()
    text = clip()
    length = len(text)
    print(text, str(length) + "文字")
    if length > MAX_LENGTH:
        print(f"[TOO LONG!!] (>{MAX_LENGTH}文字)")


if __name__ == "__main__":
    print("対象の文字列をクリップボードにコピーしてEnterを押してしてください。")
    while 1:
        main()
