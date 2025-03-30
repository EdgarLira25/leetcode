class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if name and not typed:
            return False

        if name == typed:
            return True

        last_letter = ""
        cursor_typed = 0
        len_typed = len(typed)
        len_name = len(name)

        for x in range(len_name):
            if last_letter and last_letter != name[x]:
                while cursor_typed < len_typed and typed[cursor_typed] == last_letter:
                    cursor_typed += 1

            if cursor_typed < len_typed and typed[cursor_typed] == name[x]:
                cursor_typed += 1
            else: 
                return False

            last_letter = name[x]

        while cursor_typed < len_typed and typed[cursor_typed] == last_letter:
            cursor_typed += 1

        if cursor_typed == len_typed:
            return True

        return False
