string1 = "abcdefghij"
string2 = "cdgi"


def longest_commmon_subsequence(string1, string2):
    dp = [[0 for j in range(len(string2) + 1)]for i in range(len(string1) + 1)]

    for i in range(len(string1) - 1, -1, -1):
        for j in range(len(string2) - 1, -1, -1):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])

    return dp[0][0]


print(longest_commmon_subsequence(string1, string2))



