# Nhập vào 1 số tự nhiên n < 1000. Liệt kê tất cả các hoán vị của tập {1, 2, ..., n}.

def tao(n):
    kq = []
    def quilui(m):
        if len(m) == n:
            kq.append(m[:])
            return

        for i in range(1, n + 1):
            if i not in m:
                m.append(i)
                quilui(m)
                m.pop()

    quilui([])
    return kq


def main():
    while True:
        try:
            n = int(input("Nhập một số tự nhiên n (n < 1000): "))
            if 0 < n < 1000:
                break
            else:
                print("n phải là số tự nhiên lớn hơn 0 và nhỏ hơn 1000.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    a = tao(n)

    print(f"\nCác hoán vị của tập {{1, 2, ..., {n}}}:")
    for n in a:
        print(n)
    print(f"\nTổng số hoán vị: {len(a)}")


if __name__ == "__main__":
    main()