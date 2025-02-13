def tao(n, k):
    kq = []  # mảng lưu tổ hợp hiện tại
    dem = [0]  # dùng list để lưu biến đếm

    def quilui(a, b):
        # Nếu đã chọn đủ k phần tử
        if b == 0:
            print(kq)  # In tổ hợp hiện tại
            dem[0] += 1  # Tăng biến đếm
            return

        # Thử các số từ start đến n
        for i in range(a, n + 1):
            kq.append(i)
            quilui(i + 1, b - 1)
            kq.pop()  # Quay lui bằng cách bỏ phần tử vừa thêm

    quilui(1, k)
    return dem[0]  # trả về tổng số tổ hợp

def main():
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    if 2 <= k <= n <= 1000:
        print(f"Các tổ hợp chập {k} của {n} là:")
        tong = tao(n, k)
        print(f"Tổng số tổ hợp là: {tong}")
    else:
        print("Giá trị của n và k không hợp lệ.")

if __name__ == "__main__":
    main()