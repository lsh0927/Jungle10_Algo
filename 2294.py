import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
   coins.append(int(input()))

coins = list(set(coins))
coins.sort()

queue = deque([(0, 0)]) 
visited = [False] * (k + 1)
visited[0] = True

while queue:
   current_amount, coin_count = queue.popleft()
   
   if current_amount == k:
       print(coin_count)
       exit()
   
   for coin in coins:
       next_amount = current_amount + coin
       
       if next_amount <= k and not visited[next_amount]:
           visited[next_amount] = True
           queue.append((next_amount, coin_count + 1))

print(-1)