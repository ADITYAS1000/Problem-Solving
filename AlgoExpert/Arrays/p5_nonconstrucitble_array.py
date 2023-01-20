# O(n log n) | O(1)
def nonConstructibleChange(coins):
    changeCoin = 0
    coins.sort()
    for coin in coins:
        if changeCoin + 1 < coin:
            return changeCoin + 1
        
        changeCoin += coin

print(nonConstructibleChange([5,7,1,1,2,3,22]))