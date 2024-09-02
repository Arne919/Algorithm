import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    result = 0
    cards = list(map(int, input().split()))
    player = []
    enemy = []
    first, second = 0, 0

    pass