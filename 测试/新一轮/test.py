# 10000,
# 含 1 正整数

def with_1(num: int) -> int:
    count = 0
    for i in range(num + 1):
        if '1' in str(i):
            count += 1
    
    return count

if __name__ == "__main__":
    print(with_1(10000))
