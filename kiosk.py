menus = {'짜장면':4000,'짬뽕':4000,'차돌짬뽕':9000,'탕수육':13000}
pick ={}
owermoney = 0


def menu_list():
    print("===============================")
    print("             메뉴판             ")
    print("===============================")
    for menu_name_13, price_13 in menus.items():
        print(menu_name_13, ":", price_13, "원")
        print("===============================")

def pick_menus():
    menu_list()

    while True:
        want_takeout = input("주문할 메뉴 (종료 원할시 '종료'): ")

        if want_takeout == "종료":
            break

        if want_takeout in menus:
            pick[want_takeout] = pick.get(want_takeout, 0) + 1
            print(f"-> {want_takeout} 담겼습니다.")
        else:
            print("존재하지 않는 메뉴입니다.")

def calculate_total_takeout():
    total_price = 0
    print("\n===== 주문 내역 =====")
    for menu, count in pick.items():
        price = menus[menu] * count
        total_price += price
        print(f"{menu} x {count} = {price}원")

    final_price = int(total_price *0.75)
    print(f"총 합계: {final_price}원")

    return final_price

def calculate_total():
    total_price = 0
    print("\n===== 주문 내역 =====")
    for menu, count in pick.items():
        price = menus[menu] * count
        total_price += price
        print(f"{menu} x {count} = {price}원")
    print(f"총 합계: {total_price}원")
    return total_price

def what_payment_takeout(final_price):
    global owermoney
    payment = int(input("무엇으로 결제할 것인가요? 숫자로 입력하시요(1. 카드, 2. 현금) :"))
    if payment == 1:
        pay_money = int(input("카드가 보내주는 돈(아직은 뭐 못하니 입력값으로...ㅜ : "))
        if pay_money == final_price:
            print("결제가 완료 되었습니다.")
            owermoney += final_price
            pick.clear()
        elif pay_money < final_price:
            print("잔액부족, 한도 초과")
            pick.clear()

    elif payment == 2:
        print("cash -> plz come to counter")

def what_payment(total_price):
    global owermoney
    payment = int(input("무엇으로 결제할 것인가요? 숫자로 입력하시요(1. 카드, 2. 현금) :"))
    if payment == 1:
        pay_money = int(input("카드가 보내주는 돈(아직은 뭐 못하니 입력값으로...ㅜ : "))
        if pay_money == total_price:
            print("결제가 완료 되었습니다.")
            owermoney += total_price
            pick.clear()
        elif pay_money < total_price:
            print("잔액부족, 한도 초과")
            pick.clear()

    elif payment == 2:
        print("cash -> plz come to counter")
        pick.clear()

def owners_version():
    while True:
        print("===== 음식점 메뉴 관리 프로그램 =====")
        print("1. 신규 메뉴등록")
        print("2. 메뉴판 전체 보기")
        print("3. 프로그램 종료")
        print(" ")
        i = int(input("선택(1. 추가 | 2. 조회 | 3. 종료): "))

        if i == 1:
            menu = str(input("메뉴명 : "))
            cost = int(input("가격 :"))
            print("신규 메뉴", menu, "(이)가 등록되었습니다.")
            menus[menu] = cost
            print(menus)


        elif i == 2:
            menu_list()

            j = int(input("메뉴에서 어떤 작업을 하실 건가요? 1. 수정 | 2. 삭제 | 3. 나가기 "))
            if j == 1:
                menu_change = str(input("어떤 수정을 하실 건가요?(이름, 가격) : "))
                if menu_change == '이름':
                    change_name = str(input("이름을 수정할 메뉴를 알려주세요 : "))
                    if change_name in menus:
                        want_change = str(input("바꾸고 싶은 이름을 작성해 주세요 : "))
                        menus[want_change] = menus.pop(change_name)
                    else:
                        print("해당 메뉴가 없습니다.")
                        continue
                elif menu_change == '가격':
                    change_name = str(input("가격을 수정할 메뉴를 알려주세요 : "))
                    if change_name in menus:
                        what_cost = int(input("바꾸고 싶은 가격을 작성해 주세요 : "))
                        menus[change_name] = what_cost
                    else:
                        print("no signal")
                        continue
                else:
                    print("no signal")
                    continue

            elif j == 2:
                what_menu = str(input("어떤 메뉴를 삭제 하실 건가요? : "))
                if what_menu in menus:
                    del menus[what_menu]
                    print(what_menu, "(이)가 삭제 되었습니다.")
                    print(menus)
                else:
                    print("삭제하고 싶은 메뉴가 메뉴판에 없습니다.")
                    print("현제 상황 :", menus)
                    continue

            elif j == 3:
                print("나가기")
                continue


        elif i == 3:
            print(menus)
            print("프로그램이 종료 되었습니다.")
            break
        else:
            break

def customer_version():
    while True:
        what_want = int(input("1.포장, 2.매장 (번호로 입력해 주세요)"))
        if what_want == 1:
            pick_menus()
            if pick:
                total = calculate_total_takeout()
                what_payment_takeout(total)
            else:
                print("no signal")

        elif what_want == 2:
            pick_menus()
            if pick:
                total= calculate_total()
                what_payment(total)
            else:
                print("no signal")

        else:
            break

def main():
    while True:
        version_choose = int(input("버전을 고르시오(1:관리자, 2:손님용, 3:번 금액): "))
        if version_choose == 1:
            owners_version()
        elif version_choose ==2:
            customer_version()
        elif version_choose == 3:
            print(f"오늘 번 금액: {owermoney}원")
        else:
            break

if __name__ == "__main__":
    main()