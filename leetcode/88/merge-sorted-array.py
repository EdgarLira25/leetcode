from typing import List


class Solution:
    def insert_move_items(self, lista, index, item, size):
        for x in range(size):
            if x == index:
                for y in range(size - 1, x, -1):
                    temp = lista[y]
                    lista[y] = lista[y - 1]
                    lista[y - 1] = temp
                lista[index] = item
                return

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        atual = 0
        x = 0
        while n > 0:
            if nums2[atual] < nums1[x] or x >= m:
                self.insert_move_items(nums1, x, nums2[atual], m + 1)
                m += 1
                n -= 1
                atual += 1
            x += 1
