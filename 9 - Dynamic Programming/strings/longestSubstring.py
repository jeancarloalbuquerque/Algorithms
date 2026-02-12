def longestSubstring(a, b):
    dp = [[0] * len(b) for _ in range(len(a))]
    longest = 0

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                try:
                    previous = dp[i - 1][j - 1]
                except KeyError:
                    previous = 0 
                
                dp[i][j] = previous + 1
                longest = max(longest, dp[i][j])
                
    return longest

str_a = 'fish'
str_b = 'wish'

result = longestSubstring(str_a, str_b)

print(f'Longest substring lenght: {result}')