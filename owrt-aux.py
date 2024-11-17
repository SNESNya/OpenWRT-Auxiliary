import subprocess

# 软件基本信息
sw_name = "OpenWRT-Auxiliary"
ver = "0.0.2"
link = "https://github.com/SNESNya/OpenWRT-Auxiliary"
authors = ["LAGSNES", "ChatGPT"]

def main_menu():
    print(f"{sw_name} {ver}")
    print("输入需要使用的功能并回车:\n")
    print("[2] opkg 工具")
    print("[0] 退出")

def about():
    print(f"{sw_name} {ver}")
    print(f"GitHub链接: {link}")
    print(f"by {', '.join(authors)}")

def opkg_menu():
    print("opkg 工具\n")
    print("[1] 更新软件包列表")
    print("[2] 搜索软件包")
    print("[3] 搜索已安装的软件包")
    print("[0] 返回 " + sw_name)

def opkg_update():
    try:
        # 执行opkg update命令
        result = subprocess.run(['opkg', 'update'], capture_output=True, text=True)
        if result.returncode == 0:
            print("更新成功")
        else:
            print(f"更新失败，错误代码 {result.returncode}")
    except Exception as e:
        print(f"更新失败，错误代码 {str(e)}")

def search_package():
    package = input("搜索你需要的软件包\n[0] 取消\n> ").strip()
    if package == "0":
        return
    try:
        # 执行opkg搜索命令
        result = subprocess.run(['opkg', 'list', 'available', package], capture_output=True, text=True)
        if result.returncode == 0:
            print("搜索结果:")
            print(result.stdout)
        else:
            print("未找到相关软件包")
    except Exception as e:
        print(f"搜索失败，错误: {str(e)}")

def search_installed_package():
    package = input("搜索你已安装的软件包\n[0] 取消\n> ").strip()
    if package == "0":
        return
    try:
        # 执行opkg查询已安装软件包的命令
        result = subprocess.run(['opkg', 'list-installed', package], capture_output=True, text=True)
        if result.returncode == 0:
            print("已安装的软件包:")
            print(result.stdout)
        else:
            print("未安装相关软件包")
    except Exception as e:
        print(f"查询失败，错误: {str(e)}")

def opkg_tool():
    while True:
        opkg_menu()
        choice = input("请输入选项: ").strip()
        if choice == "1":
            opkg_update()
        elif choice == "2":
            search_package()
        elif choice == "3":
            search_installed_package()
        elif choice == "0":
            return
        else:
            print("无效选项，请重试。")

def main():
    while True:
        main_menu()
        choice = input("请输入选项: ").strip()
        if choice == "2":
            opkg_tool()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()
