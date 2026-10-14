class Solution:
    def checkValidString(self, s: str) -> bool:
        count = star = 0

        for x in s:
            if x == '(':
                count += 1
            elif x == ')':
                count -= 1
                if count < 0:
                    if star <= 0:
                        return False
                    else:
                        star -= 1
                        count = 0

            else:
                star += 1

            print(count)
            print(star)

        if count != 0 and count > star:
            return False

        
        count = star = 0

        for x in reversed(s):
            if x == ')':
                count += 1
            elif x == '(':
                count -= 1
                if count < 0:
                    if star <= 0:
                        return False
                    else:
                        star -= 1
                        count = 0

            else:
                star += 1

        if count == 0 or count <= star:
            return True

        return False