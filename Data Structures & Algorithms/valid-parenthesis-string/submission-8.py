class Solution:
    def checkValidString(self, s: str) -> bool:

        def countPar(string, par_1, par_2):
            count = star = 0

            for x in string:
                if x == par_1:
                    count += 1
                elif x == par_2:
                    count -= 1
                    if count < 0:
                        if star <= 0:
                            return False
                        else:
                            star -= 1
                            count = 0

                else:
                    star += 1

            if count != 0 and count > star:
                return False

            return True

        return countPar(s, '(', ')') and countPar(reversed(s), ')', '(')