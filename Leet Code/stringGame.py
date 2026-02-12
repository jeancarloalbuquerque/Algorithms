# 3304. Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=problem-list-v2&envId=recursion

class Solution(object):
    def kthCharacter(self, k, word:str='x'):
        if len(word) >= k:
            print(word)
            return word[k-1]

        for char in word:
            word += chr(
                (ord(char) - ord('a') + 1) % 
                (ord('z') - ord('a') + 1) +
                ord('a')
            )

        return self.kthCharacter(k, word)

k = 10
result = (Solution()).kthCharacter(k)

print(result)