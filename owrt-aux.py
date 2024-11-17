# OpenWRT-Auxiliary 主程序

sw_name = "OpenWRT-Auxiliary"
ver = "0.0.1"
link = "https://github.com/SNESNya/OpenWRT-Auxiliary"
authors = ["LAGSNES", "ChatGPT"]

def main_menu():
    print(f"{sw_name} {ver}")
    print("输入需要使用的功能并回车:\n")
    print("[1] 关于")
    print("[0] 退出")

def about():
    print(f"{sw_name} {ver}")
    print(f"GitHub链接: {link}")
    print(f"by {', '.join(authors)}")

def main():
    while True:
        main_menu()
        choice = input("请输入选项: ").strip()
        if choice == "1":
            about()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
