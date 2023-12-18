

if __name__ == "__main__":

    N = int(input())

    dp = [0] * 3

    for day in range(N):
        cost = [int(x) for x in input().split()]
        new_dp = [0] * 3
        for i in range(3):

            for j in range(3):

                if (i != j):

                    new_dp[j] = max(new_dp[j] , dp[i] + cost[j])
        dp = new_dp
    print(max(dp))