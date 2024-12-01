# 9.	Trình bày phương pháp liệt kê các tổ hợp chập k của tập {1, 2, ...n} sử dụng phương pháp quay lui.

def print_combination(arr):
    print(arr)

def try_combination(i, n, k, arr):
    for j in range(arr[i-1] + 1, n - k + i + 1):
        arr[i] = j
        if i == k:
            print_combination(arr[1:k+1])
        else:
            try_combination(i + 1, n, k, arr)

def generate_combinations(n, k):
    # Khởi tạo mảng arr với k+1 phần tử, arr[0] = 0
    arr = [0] * (k + 1)
    try_combination(1, n, k, arr)

# Test với n = 5, k = 3
n = 5
k = 3
print(f"Các tổ hợp chập {k} của tập {{1, 2, ..., {n}}}:")
generate_combinations(n, k)