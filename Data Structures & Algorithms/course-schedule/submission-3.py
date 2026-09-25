class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_set = {}

        for i, j in prerequisites:
            if i not in hash_set:
                hash_set[i] = [j]
            else:
                hash_set[i].append(j)

        def is_cycle(x, seen, done):
            if x in seen:
                return True
            
            if x not in hash_set:
                return False

            if x not in done:
                seen.add(x)
                for k in hash_set[x]:
                    if is_cycle(k, seen, done):
                        done[x] = True
                        return done[x]
                seen.remove(x)
                done[x] = False
                return done[x]

            return done[x]
            
        done = {}
        for x in hash_set.keys():
            if is_cycle(x, set(), done):
                return False

        return True