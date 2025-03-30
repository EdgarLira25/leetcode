class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        atual = 1
        up = False
        down = False
        for atual in range(1, len(arr)):
            if (
                atual > 1
                and arr[atual] == arr[atual - 1]
                or atual == 1
                and arr[atual] <= arr[atual - 1]
            ):
                return False

            if atual > 1 and arr[atual] < arr[atual - 1]:
                up = True
                atual += 1
                break

        for atual2 in range(atual, len(arr)):
            if arr[atual2] >= arr[atual2 - 1]:
                return False
        down = True

        return up and down
