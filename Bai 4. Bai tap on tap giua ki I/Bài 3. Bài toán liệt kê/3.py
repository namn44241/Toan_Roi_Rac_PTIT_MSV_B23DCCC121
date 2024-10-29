# Nhập vào 1 số tự nhiên n < 1000. Liệt kê tất cả các tập con của tập {1, 2, ..., n}.

def tao(n):
    kq = []
    def quilui(a, b):
        kq.append(b[:])
        for i in range(a, n + 1):
            b.append(i)
            quilui(i + 1, b)
            b.pop()

    quilui(1, [])
    return kq

def main():
    while True:
        try:
            n = int(input("Nhập một số tự nhiên n (n < 1000): "))
            if 0 <= n < 1000:
                break
            else:
                print("n phải là số tự nhiên nhỏ hơn 1000.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    a = tao(n)

    print(f"\nCác tập con của tập {{1, 2, ..., {n}}}:")
    for i in a:
        print(i)
    print(f"\nTổng số tập con: {len(a)}")


if __name__ == "__main__":
    main()