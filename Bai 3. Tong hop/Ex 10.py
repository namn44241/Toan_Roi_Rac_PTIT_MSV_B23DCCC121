# Cho 2 số n, k ( 2 <= k <= n <= 10^3).
# Sử dụng đệ quy tính số tổ hợp chập k của n.

def tinh(n, k):
    if k == 0 or k == n:
        return 1
    return tinh(n - 1, k - 1) + tinh(n - 1, k)


def main():
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 2 <= k <= n <= 1000:
        a = tinh(n, k)
        print(f"Số tổ hợp chập {k} của {n} là: {a}")
    else:
        print("Giá trị của n và k không hợp lệ.")


if __name__ == "__main__":
    main()


    def tao(n, k):
        ht = [0]
        kq = []

        def quilui(a, b):
            # Nếu đã chọn đủ k phần tử
            if b == 0:
                ht[0] += 1
                return

            # Thử các số từ start đến n
            for i in range(a, n + 1):
                kq.append(i)
                quilui(i + 1, b - 1)
                kq.pop()  # Quay lui bằng cách bỏ phần tử vừa thêm

        quilui(1, k)
        return ht[0]


    def main():
        n = int(input("Nhập n: "))
        k = int(input("Nhập k: "))

        if 2 <= k <= n <= 1000:
            result = tao(n, k)
            print(f"Số tổ hợp chập {k} của {n} là: {result}")
        else:
            print("Giá trị của n và k không hợp lệ.")


    if __name__ == "__main__":
        main()
