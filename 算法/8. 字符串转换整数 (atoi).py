class Solution:
    def myAtoi(self, s: str) -> int:
        no1 = True
        answer = ''
        for c in s:
            if no1:
                if c == '-':
                    no1 = False
                    answer += c
                    continue
                if c == ' ':
                    continue
                if c == '+':
                    no1 = False
                    continue

                try:
                    int(c)
                except ValueError:
                    return 0
                else:
                    answer += c
                    no1 = False
            else:
                try:
                    int(c)
                except ValueError:
                    break
                else:
                    answer += c

        # if answer == '':
        #     return 0

        try:
            a = int(answer)
        except ValueError:
            return 0
        if a < -2147483648:
            return -2147483648
        if a > 2147483647:
            return 2147483647
        return a


if __name__ == '__main__':
    print(Solution().myAtoi('4193 with words'))
    print(Solution().myAtoi('   -42'))
    print(Solution().myAtoi('words and 987'))
    print(Solution().myAtoi('42'))
    print(Solution().myAtoi(''))
    print(Solution().myAtoi('-'))
    print(Solution().myAtoi('+-2'))
