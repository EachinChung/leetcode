# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s and len(p) == 1: return False

        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for r in range(nrow)]

        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c - 1
            if p[j] == '*': dp[0][c] = dp[0][c - 2]

        for r in range(1, nrow):
            i = r - 1
            for c in range(1, ncol):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False

        return dp[nrow - 1][ncol - 1]


if __name__ == '__main__':
    demo = Solution()
    print(demo.isMatch('a', 'ab*'))
    print(demo.isMatch('a', 'a'))
    print(demo.isMatch('aaa', 'ab*a*c*a'))
    print(demo.isMatch('aaa', 'a*a'))
    print(demo.isMatch('aa', 'a*'))
    print(demo.isMatch('aa', 'a.'))
    print(demo.isMatch('ab', '.*'))
    print(demo.isMatch('aab', 'c*a*b'))
    print('cuo')
    print(demo.isMatch('aa', 'a'))
    print(demo.isMatch('aa', 'aaa'))
    print(demo.isMatch('aaa', 'ab*a'))
    print(demo.isMatch('ippi', 'p*.'))
    print(demo.isMatch('mississippi', 'mis*is*p*.'))
    print(demo.isMatch('ab', '.*c'))
