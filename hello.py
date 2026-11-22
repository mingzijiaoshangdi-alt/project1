"""一个简单的 Python 问候程序。运行方式：python hello.py"""


def main():
    name = input("你叫什么名字？").strip()
    print(f"你好，{name or '朋友'}！欢迎使用 GitHub。")


if __name__ == "__main__":
    main()
