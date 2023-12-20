

if __name__ == "__main__":

    N, K = [int(x) for x in input().split()]

    a = [int(x) for x in input().split()]

    dp = [False] * (K + 1)

    for stones in range(K+1):

        for x in a:

            if stones >= x and not dp[stones - x]:

                dp[stones] = True

    print("First") if dp[K] else print("Second")


