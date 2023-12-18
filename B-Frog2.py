
def calculate_minimum(N, K, stones):

    INF = 10 ** 20

    dp = [INF] * N
    dp[0] = 0

    for i in range(N):

        for j in range(i+1, i+ K+1):

            if j < N:

                dp[j] = min(dp[j] , dp[i] + abs(stones[i] - stones[j]))

    return dp[N-1]


if __name__ == "__main__":

    N, K = [int (x) for x in input().split()]

    stones = [int(x) for x in input().split()]

    print(calculate_minimum(N, K, stones))

