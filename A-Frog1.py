
def maximum_jumps(N,stones):
    INF = 10 ** 20
    dp = [INF] * N
    dp[0] = 0
    for i in range(N):

        for j in (i+1,i+2):

            if j < N:
                dp[j] = min(dp[j] , dp[i] + abs(stones[j] - stones[i]))

    return dp[N-1]

if __name__=="__main__":

    N = int(input())
    stones = [int(x) for x in input().split()]

    print(maximum_jumps(N,stones))