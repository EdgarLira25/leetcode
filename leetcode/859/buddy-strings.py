class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if not s or not goal:
            return False
        if len(goal) != len(s):
            return False
        if len(s) == 1 and len(goal) == 1:
            return False

        string = list(s)
        objective = list(goal)
        diff = 0
        diff_points = []
        for i in range(len(string)):
            if string[i] != goal[i]:
                diff_points.append(i)
                diff += 1
            if diff > 2:
                return False

        if len(diff_points) == 2:
            list_temp = objective.copy()
            temp = list_temp[diff_points[0]]
            list_temp[diff_points[0]] = list_temp[diff_points[1]]
            list_temp[diff_points[1]] = temp
            if list_temp == string:
                return True
            else:
                return False

        if len(diff_points) == 1:
            return False

        for i in range(len(string)):
            for j in range(i, len(string)):
                if i == j:
                    continue
                string_copy = string.copy()
                temp = string_copy[i]
                string_copy[i] = string_copy[j]
                string_copy[j] = temp
                if string_copy == objective:
                    return True
        return False

