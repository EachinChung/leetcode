# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        z_map = []
        for i in range(numRows):
            z_map.append([])

        direction = True
        count = 0
        i = 0
        while i < len(s):
            # print(f"{i} {c}")
            if direction:
                if count == numRows:
                    direction = False
                    count = numRows - 2
                else:
                    # print(f'zheng {s[i]} {count}')
                    z_map[count].append(s[i])
                    count += 1
                    i += 1
            else:
                if count == -1:
                    direction = True
                    count = 1
                else:
                    # print(f'fan {s[i]} {count}')
                    z_map[count].append(s[i])
                    count -= 1
                    i += 1

        answer = ''
        for item in z_map:
            answer += ''.join(item)

        return answer


if __name__ == '__main__':
    demo = Solution()
    # print(demo.convert("LEETCODEISHIRING", 3))
    print(demo.convert("LEETCODEISHIRING", 4))
