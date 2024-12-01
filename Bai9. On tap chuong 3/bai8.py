# 8.	Viết chương trình C/C++/Python liệt kê các hoán vị của tập {1, 2, ..., n} sử dụng phương pháp sinh theo thứ tự từ điển.
def next_permutation(perm):
    n = len(perm)

    # Bước 1: Tìm từ phải sang trái vị trí i đầu tiên mà perm[i] < perm[i+1]
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    # Nếu không tìm thấy, đây là hoán vị cuối cùng
    if i < 0:
        return False

    # Bước 2: Tìm từ phải sang trái vị trí j đầu tiên mà perm[j] > perm[i]
    j = n - 1
    while perm[j] <= perm[i]:
        j -= 1

    # Bước 3: Đổi chỗ perm[i] và perm[j]
    perm[i], perm[j] = perm[j], perm[i]

    # Bước 4: Lật ngược đoạn từ i+1 đến n-1
    left = i + 1
    right = n - 1
    while left < right:
        perm[left], perm[right] = perm[right], perm[left]
        left += 1
        right -= 1

    return True


def generate_permutations(n):
    # Tạo hoán vị đầu tiên [1, 2, ..., n]
    perm = list(range(1, n + 1))

    # In hoán vị đầu tiên
    print(perm)

    # Sinh và in các hoán vị tiếp theo
    while next_permutation(perm):
        print(perm)


# Test với n = 3
n = 3
print(f"Các hoán vị của tập {{1, 2, ..., {n}}}:")
generate_permutations(n)