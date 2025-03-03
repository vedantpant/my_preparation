from itertools import permutations


def calculate_overlaps(strings):
    """Precompute overlaps between all pairs of strings."""
    n = len(strings)
    overlap = [[0] * n for _ in range(n)]  # Initialize an NxN matrix

    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(1, len(strings[i])):  # Find max suffix-prefix match
                    if strings[i][-k:] == strings[j][:k]:
                        overlap[i][j] = k
    return overlap


def shortest_superstring_dp(strings):
    """Finds the shortest superstring using Dynamic Programming."""
    n = len(strings)
    overlap = calculate_overlaps(strings)

    # DP table: dp[mask][i] stores the shortest superstring that includes mask and ends at i
    dp = [[None] * n for _ in range(1 << n)]
    path = [[None] * n for _ in range(1 << n)]  # Store the previous index to reconstruct path

    # Base case: each string alone is a valid superstring
    for i in range(n):
        dp[1 << i][i] = strings[i]  # dp[0001][0] = "abc", dp[0010][1] = "bca", etc.

    # Fill DP table
    for mask in range(1, 1 << n):  # Iterate over all subsets of strings
        for i in range(n):
            if not (mask & (1 << i)):  # Skip if string `i` is not in this subset
                continue
            for j in range(n):
                if mask & (1 << j):  # Skip if `j` is already included
                    continue
                new_mask = mask | (1 << j)  # Add `j` to the subset
                new_string = dp[mask][i] + strings[j][overlap[i][j]:]  # Merge optimally

                # Update DP if this new string is shorter
                if dp[new_mask][j] is None or len(new_string) < len(dp[new_mask][j]):
                    dp[new_mask][j] = new_string
                    path[new_mask][j] = i  # Store previous index for backtracking

    # Find the shortest superstring from all final DP states
    min_superstring = None
    last = -1
    full_mask = (1 << n) - 1  # All strings included

    for i in range(n):
        if min_superstring is None or len(dp[full_mask][i]) < len(min_superstring):
            min_superstring = dp[full_mask][i]
            last = i  # Store the last used string

    return min_superstring


# Example Usage
strings = ["abc", "bca", "cab"]
print(shortest_superstring_dp(strings))  # Output: "abcab"
