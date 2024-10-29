def main():
    tong = 21
    kq = []

    for x1 in range(4):  # x1 <= 3
        for x2 in range(2, tong - x1 - 4 + 1):  # x2 >= 2
            for x3 in range(4, tong - x1 - x2 + 1):  # x3 >= 4
                x4 = tong - x1 - x2 - x3
                if x4 >= 0:  # x4 >= 0
                    kq.append((x1, x2, x3, x4))

    print(f"Các nghiệm nguyên của phương trình x1 + x2 + x3 + x4 = {tong},")
    print(f"với x1 <= 3, x2 >= 2, x3 >= 4, x4 >= 0:")
    for x1, x2, x3, x4 in kq:
        print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
    print(f"\nTổng số nghiệm: {len(kq)}")

if __name__ == "__main__":
    main()