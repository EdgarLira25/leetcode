class Solution:

    def find_max_value_for_each_children(self, money, children):
        money = money - children
        distribution = [[1, child] for child in range(children)]
        if money == 0:
            return distribution
        for dist in distribution:
            if money <= 0:
                break

            if dist[1] == children-1:
                if money == 3:
                    distribution[children-2][0] += 1
                    dist[0] += 2
                else: 
                    dist[0] += money
                    break

            desconto = abs(dist[0] - 8) if money >= abs(dist[0] - 8) else money
            if desconto == 3:
                distribution[children-1][0] += 1
                desconto = 2

            dist[0] += desconto
            money -= desconto
        return distribution

    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        nums = 0 
        kk = self.find_max_value_for_each_children(money,children)
        if not kk:
            return -1

        for mon, _ in kk:
            if mon == 8:
                nums+=1
        return nums
