# Nhập vào 1 số tự nhiên n < 1000. Liệt kê tất cả các xâu nhị phân có độ dài n.

def tao(n):
    if n == 0:
        return ['']

    a = tao(n - 1)
    return ['0' + s for s in a] + ['1' + s for s in a]


def main():
    while True:
        try:
            n = int(input("Nhập độ dài của xâu nhị phân (n < 1000): "))
            if 0 <= n < 1000:
                break
            else:
                print("n phải là số tự nhiên nhỏ hơn 1000.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    b = tao(n)

    print(f"\nCác xâu nhị phân có độ dài {n}:")
    # for string in b:
    #     print(string)
    print({s for s in b})
    # print(f"\nTổng số xâu: {len(b)}")


if __name__ == "__main__":
    main()