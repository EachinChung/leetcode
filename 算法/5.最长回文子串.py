class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ''

        start, end = 0, 0

        for i in range(len(s)):
            palindrome1 = expand_around_center(s, i, i)
            palindrome2 = expand_around_center(s, i, i + 1)

            if palindrome1[0] > palindrome2[0] and palindrome1[0] > end - start:
                start = palindrome1[1]
                end = palindrome1[2]
            elif palindrome2[0] > end - start:
                start = palindrome2[1]
                end = palindrome2[2]

        return s[start:end]


def expand_around_center(s: str, left: int, right: int):
    try:
        if s[left] != s[right]:
            return -1, 0, 0
    except IndexError:
        return -1, 0, 0

    while left > 0 and right < len(s) - 1:
        if s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        else:
            break

    return right - left + 1, left, right + 1


if __name__ == '__main__':
    demo = Solution()
    print(demo.longestPalindrome('a'))
    print(demo.longestPalindrome('aa'))
    print(demo.longestPalindrome('aaa'))
    print(demo.longestPalindrome('abcabcbb'))
    print(demo.longestPalindrome('babad'))
    print(demo.longestPalindrome('cbbd'))
    print(demo.longestPalindrome('cccc'))
