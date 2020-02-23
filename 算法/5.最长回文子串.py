# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ''

        start, end = 0, 0

        for i in range(len(s)):
            print(i)


def expand_around_center(s: str, left: int, right: int) -> int:
    pass


if __name__ == '__main__':
    demo = Solution()
    print(demo.longestPalindrome('abcabcbb'))
    # print(demo.longestPalindrome('babad'))
    # print(demo.longestPalindrome('cbbd'))
