# 420. Strong Password Checker
import re


class Solution:
    def uppercaseCheck(self, password):
        return 1 if not re.search(r'[A-Z]', password) else 0

    def lowercaseCheck(self, password):
        return 1 if not re.search(r'[a-z]', password) else 0

    def numberCheck(self, password):
        return  1 if not re.search(r'[0-9]', password) else 0

    # 检查同一字符连续出现三次及以上，并转换为次数 "aaaaabbbbbbcc" -> [5,6] 有个测试用例有.和！需要特殊处理
    def lengthCheck(self, password):
        res = []
        for el in re.finditer(r'([\\.a-zA-Z0-9!])\1{2,}', password):
            # print('str found', el.start(), el.end())
            res.append(el.end()-el.start())
        return res

    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        check_num = self.uppercaseCheck(password) + self.lowercaseCheck(password) + self.numberCheck(password)
        res = self.lengthCheck(password)
        # 连续多余的字符串替换
        replace = sum(map(lambda x: int(x//3),res))
        if n <= 5:
            return max(check_num,6-n)
        elif n <= 20:
            return max(replace, check_num)
        elif n > 20:
            numdel = n - 20

            # 多余的字符串删除
            l = list(map(lambda x: (x % 3)+1,res))
            l.sort()
            rem = numdel
            for i in range(0,len(l)):
                if rem >= l[i]:
                    rem -= l[i]
                    replace -= 1
            replace -= int(rem / 3)

            if replace < check_num:
                replace = check_num

            return numdel + replace
        return 0
