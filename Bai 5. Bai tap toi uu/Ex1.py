# Viết chương trình nhập vào số n > 5 và mảng M gồm n phần tử không âm. Liệt kê tất cả các
# tổ hợp gồm 3 phần tử trong mảng M và in ra tổ hợp có tổng nhỏ nhất và chia hết cho 3.

# Bước 1: Nhập dữ liệu
def nhap_mang():
    while True:
        n = int(input("Nhập n (n > 5): "))
        if n > 5:
            break
        print("n phải lớn hơn 5, vui lòng nhập lại!")

    M = []
    print(f"Nhập {n} số không âm:")
    for i in range(n):
        while True:
            x = int(input(f"M[{i}] = "))
            if x >= 0:
                M.append(x)
                break
            print("Phải nhập số không âm!")
    return M


# Bước 2: Tìm tất cả tổ hợp 3 phần tử
def tim_to_hop(M):
    ket_qua = []
    n = len(M)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                to_hop = [M[i], M[j], M[k]]
                tong = sum(to_hop)

                if tong % 3 == 0:
                    ket_qua.append([to_hop, tong])

    return ket_qua


# Bước 3: Tìm tổ hợp có tổng nhỏ nhất
def tim_tong_nho_nhat(ket_qua):
    if not ket_qua:
        return None

    to_hop_nho_nhat = ket_qua[0]

    for to_hop in ket_qua:
        if to_hop[1] < to_hop_nho_nhat[1]:
            to_hop_nho_nhat = to_hop

    return to_hop_nho_nhat


def main():
    M = nhap_mang()

    print("\nMảng vừa nhập:", M)

    ket_qua = tim_to_hop(M)

    print("\nTất cả các tổ hợp có tổng chia hết cho 3:")
    for to_hop in ket_qua:
        print(f"Tổ hợp {to_hop[0]}, có tổng = {to_hop[1]}")

    to_hop_nho_nhat = tim_tong_nho_nhat(ket_qua)
    if to_hop_nho_nhat:
        print(f"\nTổ hợp có tổng nhỏ nhất: {to_hop_nho_nhat[0]}")
        print(f"Tổng = {to_hop_nho_nhat[1]}")
    else:
        print("\nKhông có tổ hợp nào thỏa mãn!")


if __name__ == "__main__":
    main()