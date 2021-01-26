def greedy(coins, k):
    changes = []   # 잔돈 종류 처리
    coins = reversed(coins)
    count = 0
    total = k
    for coin in coins:
        if coin <= total and total % coin >= 0:
            cnt = total // coin
            count += cnt
            total -= coin*cnt
            changes.append(coin)
        if total == 0:
            break
    return count, changes   # 잔액 갯수
 
if __name__ == "__main__":
    # 동전 개수와 잔액
    n, k = [int(x) for x in input().split()]
    coins = []
    for i in range(n):  # 동전 입력하기
        coin = int(input())
        coins.append(coin)
    print(greedy(coins, k))

