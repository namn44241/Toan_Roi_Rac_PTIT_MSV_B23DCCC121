# Liệt kê nghiệm nguyên của phương trình x1 + x2 + x3 = 15 với x1 ≥ 0 , x2 ≥ 0 , x3 ≥ 0.

def main():
    tong = 15
    kq = []

    for x1 in range(tong + 1):
        for x2 in range(tong - x1 + 1):
            x3 = tong - x1 - x2
            if x3 >= 0:
                kq.append((x1, x2, x3))

    print(f"Các nghiệm nguyên không âm của phương trình x1 + x2 + x3 = {tong }:")
    for x1, x2, x3 in kq:
        print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
    print(f"\nTổng số nghiệm: {len(kq)}")

if __name__ == "__main__":
    main()


# def main():
#     tong = 15
#     min_x1, min_x2, min_x3 = 1, 2, 3
#     kq = []
#
#     for x1 in range(min_x1, tong - min_x2 - min_x3 + 1):
#         for x2 in range(min_x2, tong - x1 - min_x3 + 1):
#             x3 = tong - x1 - x2
#             if x3 >= min_x3:
#                 kq.append((x1, x2, x3))
#
#     print(f"Các nghiệm nguyên của phương trình x1 + x2 + x3 = {tong},")
#     print(f"với x1 >= {min_x1}, x2 >= {min_x2}, x3 >= {min_x3}:")
#     for x1, x2, x3 in kq:
#         print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
#     print(f"\nTổng số nghiệm: {len(kq)}")
#
# if __name__ == "__main__":
#     main()


def main():
    tong = 15
    kq = []

    for x1 in range(3):  # x1 < 3
        for x2 in range(4):  # x2 < 4
            x3 = tong - x1 - x2
            if 0 <= x3 < 5:  # 0 <= x3 < 5
                kq.append((x1, x2, x3))

    print(f"Các nghiệm nguyên của phương trình x1 + x2 + x3 = {tong},")
    print(f"với 0 <= x1 < 3, 0 <= x2 < 4, 0 <= x3 < 5:")
    for x1, x2, x3 in kq:
        print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
    print(f"\nTổng số nghiệm: {len(kq)}")

if __name__ == "__main__":
    main()