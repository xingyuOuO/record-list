# 人事資料管理系統

def show_menu():
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")


def add_record(records):
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")
        records.append({
            "department": department,
            "name": name,
            "age": age,
            "phone": phone
        })
        more = input("是否繼續新增資料? (y/n): ").lower()
        if more == 'n':
            break


def query_record(records):
    name = input("請輸入要查詢的姓名: ")
    found = False
    for record in records:
        if record['name'] == name:
            print("\n--- 查詢結果 ---")
            print("部門        姓名        年齡        手機")
            print("----------------------------------------")
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']}")
            found = True
            break
    if not found:
        print("查無此人。")


def modify_record(records):
    name = input("請輸入要修改的姓名: ")
    found = False
    for record in records:
        if record['name'] == name:
            print("\n當前資料:")
            print("部門        姓名        年齡        手機")
            print("----------------------------------------")
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']}")
            print("\n1. 修改部門")
            print("2. 修改姓名")
            print("3. 修改年齡")
            print("4. 修改手機")
            choice = input("請選擇要修改的欄位: ")

            if choice == '1':
                record['department'] = input("請輸入新的部門: ")
            elif choice == '2':
                record['name'] = input("請輸入新的姓名: ")
            elif choice == '3':
                record['age'] = input("請輸入新的年齡: ")
            elif choice == '4':
                record['phone'] = input("請輸入新的手機: ")
            else:
                print("無效的選項")
                return
            print("\n--- 更新後的資料 ---")
            print("部門        姓名        年齡        手機")
            print("----------------------------------------")
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']}")
            found = True
            break
    if not found:
        print("查無此人。")


def delete_record(records):
    name = input("請輸入要刪除的姓名: ")
    found = False
    for record in records:
        if record['name'] == name:
            print("\n--- 要刪除的資料 ---")
            print("部門        姓名        年齡        手機")
            print("----------------------------------------")
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']}")
            confirm = input(f"確定要刪除 {name} 的資料嗎? (y/n): ").lower()
            if confirm == 'y':
                records.remove(record)
                print(f"{name} 的資料已刪除。")
            found = True
            break
    if not found:
        print("查無此人。")


def show_all_records(records):
    if not records:
        print("目前沒有任何資料")
    else:
        print("\n部門        姓名        年齡        手機")
        print("----------------------------------------")
        for record in records:
            print(f"{record['department']:<10}{record['name']:<10}{record['age']:<10}{record['phone']}")


def main():
    records = []
    while True:
        show_menu()
        choice = input("請選擇功能: ")

        if choice == '1':
            add_record(records)
        elif choice == '2':
            query_record(records)
        elif choice == '3':
            modify_record(records)
        elif choice == '4':
            delete_record(records)
        elif choice == '5':
            show_all_records(records)
        elif choice == '6':
            print("系統關閉")
            break
        else:
            print("選項只有1-6")


if __name__ == "__main__":
    main()
