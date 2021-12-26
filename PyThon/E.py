# Hotels max sum task

hotels, euros = map(int, input().split())
hotel_prices = list(map(int, input().split()))

def maximizer(prices: list, money: int) -> int:
    left, right, max_sum, temp = 0, 0, 0, 0
    while right < len(prices):
        temp += prices[right]
        right += 1

        while temp > money:
            temp -= prices[left]
            left += 1
        if temp > max_sum:
            max_sum = temp

    return max_sum

# hotel_prices, euros = [16, 1, 3, 4, 5, 11, 0, 4], 20
print(maximizer(hotel_prices, euros))