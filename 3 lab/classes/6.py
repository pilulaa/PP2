class primeNum:
    def filter_prime(x):
        cnt = 0
        for i in range(1, x):
            if x % i == 0:
                cnt = cnt + 1
        if cnt == 1: return True
        return False

a = list(map(int, input().split()))

print(list(filter(lambda x: primeNum.filter_prime(x), a)))