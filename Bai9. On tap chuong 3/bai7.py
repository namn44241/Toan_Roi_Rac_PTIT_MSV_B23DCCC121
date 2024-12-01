# 7.	Cho dãy A = (a₁, a₂, ..., aₙ).
# Viết chương trình trong C/C++/Python liệt kê các dãy con k phần tử giảm dần của dãy số A?
# Ví dụ: Cho A = (1, 5, 3, 4, 2, 0), k=3, các dãy con thỏa mãn yêu cầu đề bài: (5,3,2); (5,2,0);(5,4,2)...
# Lưu ý: Không sử dụng các thư viện có sẵn để sinh hoán vị, tổ hợp.

def generate_decreasing_subsequences(A, k):
    n = len(A)
    result = []
    current = []
    
    def backtrack(start, current):
        # Nếu đã đủ k phần tử và dãy giảm dần
        if len(current) == k:
            result.append(current[:])
            return
        
        # Thử các phần tử từ vị trí start
        for i in range(start, n):
            # Nếu current rỗng hoặc phần tử mới nhỏ hơn phần tử cuối của current
            if not current or A[i] < current[-1]:
                current.append(A[i])
                backtrack(i + 1, current)
                current.pop()
    
    # Bắt đầu với mảng rỗng
    backtrack(0, current)
    
    # Sắp xếp kết quả theo thứ tự giảm dần
    result.sort(reverse=True)
    return result

# Test với ví dụ trong đề
A = [1, 5, 3, 4, 2, 0]
k = 3

# Tìm các dãy con giảm dần
subsequences = generate_decreasing_subsequences(A, k)

# In kết quả
for seq in subsequences:
    print(seq)