# Nhập vào 1 số tự nhiên n < 1000. Áp dụng thuật toán quay lui,
# liệt kê tất cả các xâu nhị phân có độ dài n mà có ít nhất hai bít 1 đứng liền nhau.

def tao(n):
    kq = []
    ht = ['0'] * n

    def quilui(a, b):
        if a == n:
            if b:
                kq.append(''.join(ht))
            return

        # Thử đặt bit 0
        ht[a] = '0'
        quilui(a + 1, b)

        # Thử đặt bit 1
        ht[a] = '1'
        d = b or (a > 0 and ht[a - 1] == '1')
        quilui(a + 1, d)

    quilui(0, False)
    return kq


def main():
    while True:
        try:
            n = int(input("Nhập độ dài của xâu nhị phân (n < 1000): "))
            if 0 < n < 1000:
                break
            else:
                print("n phải là số tự nhiên lớn hơn 0 và nhỏ hơn 1000.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    chuoi = tao(n)

    print(f"\nCác xâu nhị phân có độ dài {n} và có ít nhất hai bít 1 đứng liền nhau:")
    for string in chuoi:
        print(string)
    print(f"\nTổng số xâu: {len(chuoi)}")


if __name__ == "__main__":
    main()