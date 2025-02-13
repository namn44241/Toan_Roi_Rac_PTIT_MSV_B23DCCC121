def count_numbers_with_sum(n_digits, target_sum):
    def generate_combinations(pos, remaining_sum, current_sum, leading_zero):
        # Nếu đã đủ số chữ số và tổng bằng target_sum
        if pos == n_digits:
            if current_sum == target_sum:
                return 1
            return 0

        count = 0
        # Xét các chữ số từ 0-9
        start = 0 if not leading_zero or pos > 0 else 1  # Số đầu không được là 0
        for i in range(start, 10):
            if current_sum + i <= target_sum:
                count += generate_combinations(pos + 1,
                                               remaining_sum - i,
                                               current_sum + i,
                                               leading_zero)
        return count

    return generate_combinations(0, target_sum, 0, True)


# Thực thi với n = 10 chữ số, tổng = 18
n_digits = 10
target_sum = 18

result = count_numbers_with_sum(n_digits, target_sum)
print(f"Số lượng số {n_digits} chữ số có tổng các chữ số = {target_sum} là: {result}")