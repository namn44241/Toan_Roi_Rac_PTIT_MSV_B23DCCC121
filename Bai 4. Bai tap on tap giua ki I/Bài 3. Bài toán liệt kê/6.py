def check_sum(arr, k):
    return sum(arr) == k


def is_valid_number(num, used_numbers, max_num):
    return 1 <= num <= max_num and num not in used_numbers


def print_grid(n, first_column, last_row, diagonal):
    grid = [[0] * n for _ in range(n)]

    # Điền cột đầu tiên
    for i in range(n):
        grid[i][0] = first_column[i]

    # Điền dòng cuối
    for j in range(n):
        grid[n - 1][j] = last_row[j]

    # Điền đường chéo chính
    for i in range(n):
        grid[i][i] = diagonal[i]

    # In lưới
    for row in grid:
        print(' '.join(map(str, row)))


def solve_grid(n, k):
    max_num = 3 * n - 3
    used_numbers = set()

    def try_combination(first_col_idx=0, last_row_idx=0, diag_idx=0,
                        first_col=[], last_row=[], diagonal=[]):
        # Nếu đã điền đủ tất cả các vị trí
        if first_col_idx == n and last_row_idx == n and diag_idx == n:
            # Kiểm tra tổng các phần có bằng k không
            if (check_sum(first_col, k) and
                    check_sum(last_row, k) and
                    check_sum(diagonal, k)):
                print("\nĐã tìm được lời giải:")
                print_grid(n, first_col, last_row, diagonal)
                return True
            return False

        # Thử điền cột đầu tiên
        if first_col_idx < n:
            for num in range(1, max_num + 1):
                if is_valid_number(num, used_numbers, max_num):
                    # Xử lý trường hợp số nằm ở góc
                    if first_col_idx == n - 1:  # Góc dưới cột đầu
                        if num in last_row:
                            continue
                    if first_col_idx == first_col_idx:  # Số nằm trên đường chéo
                        if len(diagonal) > first_col_idx and num != diagonal[first_col_idx]:
                            continue

                    used_numbers.add(num)
                    first_col.append(num)
                    if try_combination(first_col_idx + 1, last_row_idx, diag_idx,
                                       first_col, last_row, diagonal):
                        return True
                    first_col.pop()
                    used_numbers.remove(num)
            return False

        # Thử điền dòng cuối
        if last_row_idx < n:
            for num in range(1, max_num + 1):
                if is_valid_number(num, used_numbers, max_num):
                    if last_row_idx == last_row_idx:  # Số nằm trên đường chéo
                        if len(diagonal) > last_row_idx and num != diagonal[last_row_idx]:
                            continue

                    used_numbers.add(num)
                    last_row.append(num)
                    if try_combination(first_col_idx, last_row_idx + 1, diag_idx,
                                       first_col, last_row, diagonal):
                        return True
                    last_row.pop()
                    used_numbers.remove(num)
            return False

        # Thử điền đường chéo chính
        if diag_idx < n:
            for num in range(1, max_num + 1):
                if is_valid_number(num, used_numbers, max_num):
                    # Kiểm tra nếu số này đã được dùng ở vị trí tương ứng
                    if diag_idx < len(first_col) and num != first_col[diag_idx]:
                        continue
                    if diag_idx < len(last_row) and num != last_row[diag_idx]:
                        continue

                    used_numbers.add(num)
                    diagonal.append(num)
                    if try_combination(first_col_idx, last_row_idx, diag_idx + 1,
                                       first_col, last_row, diagonal):
                        return True
                    diagonal.pop()
                    used_numbers.remove(num)
            return False

        return False

    if try_combination():
        return True
    else:
        print("Không tìm thấy lời giải")
        return False


# Test thử với n = 3 và k = 15
n = 3
k = 15
print(f"Tìm lời giải cho lưới {n}x{n} với tổng k = {k}")
solve_grid(n, k)