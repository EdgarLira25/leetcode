# Tentei ser inteligente, mas um brute force definitivamente seria mais rápido
class Solution:
    def check_more_than_one_if_the_frequency(self, frequency, dictionary):
        appears = 0

        for value in dictionary.values():
            if value == frequency:
                appears += 1

        if appears > 1:
            return True

        return False

    def find_less_most_frequency_number(self, dictionary):
        frequency_dict = {}
        for x in dictionary:
            if dictionary[x] not in frequency_dict:
                frequency_dict[dictionary[x]] = 1
            else:
                frequency_dict[dictionary[x]] += 1

        biggest = -1
        val = float("inf")

        # print(frequency_dict)
        for x in frequency_dict:
            if frequency_dict[x] > biggest:
                val = x
                biggest = frequency_dict[x]
            elif frequency_dict[x] == biggest and x < val:
                val = x
                biggest = frequency_dict[x]

        # print(val)
        return val

    def equalFrequency(self, word: str) -> bool:
        frequency = {}

        if len(word) == 1:
            return True
        if len(set(word)) == 1:
            return True

        for item in word:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] += 1

        values = set(frequency.values())

        if len(values) == 1 and list(values)[0] == 1:
            return True

        set_len = len(values)

        if set_len <= 1 or set_len > 2:
            return False

        most_frequency = self.find_less_most_frequency_number(frequency)
        # print(most_frequency)
        values = list(values)

        if most_frequency == values[0]:
            if most_frequency > 1 and values[1] == 1:
                return True
            elif len(set(word)) == 2 and most_frequency == 1 and values[1] > 1:
                return True

            if self.check_more_than_one_if_the_frequency(values[1], frequency):
                return False
            return True if values[0] == -1 + values[1] else False

        if most_frequency > 1 and values[0] == 1:
            return True
        elif len(set(word)) == 2 and most_frequency == 1 and values[0] > 1:
            return True

        if self.check_more_than_one_if_the_frequency(values[0], frequency):
            return False
        return True if values[1] == -1 + values[0] else False


print(Solution().equalFrequency("cccd"), "expected True")
print(Solution().equalFrequency("abbcc"), "expected True")
print(Solution().equalFrequency("ddaccb"), "expected False")
print(Solution().equalFrequency("ab"), "expected True")
print(Solution().equalFrequency("abc"), "expected True")
print(Solution().equalFrequency("aazzaaz"), "expected True")
print(Solution().equalFrequency("abcc"), "expected True")
print(Solution().equalFrequency("aazzaazccc"), "expected True")
print(Solution().equalFrequency("aazzaazcccddd"), "expected True")
print(Solution().equalFrequency("aazzaazccca"), "expected False")
print(Solution().equalFrequency(""), "expected False")
print(Solution().equalFrequency("a"), "expected True")
