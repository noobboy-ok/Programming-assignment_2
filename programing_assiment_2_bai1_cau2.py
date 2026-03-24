def is_wavy(s):
    if len(s) < 2: return True
    for i in range(len(s) - 1):
        if i % 2 == 0:
            if not (s[i] < s[i+1]): return False
        else:
            if not (s[i] > s[i+1]): return False
    return True

def get_next(s):
    chars = ['a', 'b', 'c', 'd']
    s_list = list(s)
    n = len(s)
    if s == 'd' * n: return 'a' * (n + 1)
    for i in range(n - 1, -1, -1):
        if s_list[i] != 'd':
            idx = 0
            for j in range(4):
                if chars[j] == s_list[i]: idx = j; break
            s_list[i] = chars[idx + 1]
            for k in range(i + 1, n): s_list[k] = 'a'
            break
    return "".join(s_list)

def count_wavy_before(s):
    n = len(s)
    count = 0
    current = 'a' * n
    
    while current < s:
        if is_wavy(current):
            count += 1
        current = get_next(current)
        if len(current) > n: break
    return count

if __name__ == "__main__":
    user_input = input("Nhập chuỗi s : ").strip().lower()

    valid = True
    for char in user_input:
        if char not in ['a', 'b', 'c', 'd']:
            valid = False
            break
            
    if not valid:
        print("Lỗi: Chuỗi chỉ được chứa các ký tự a, b, c hoặc d.")
    else:
        result = count_wavy_before(user_input)
        print(f"Số chuỗi wavy có độ dài {len(user_input)} đứng trước '{user_input}' là: {result}")
            