class Solution:
    def calc(self, player) -> int:
        double = False
        turn = -15
        points = 0
        for index, point in enumerate(player):
            points += point if not double else point * 2
            if index - 2 == turn:
                double = False
            if point == 10:
                turn = index
                double = True
        return points

    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        point1 = self.calc(player1)
        point2 = self.calc(player2)

        if point1 > point2:
            return 1
        if point2 > point1:
            return 2
        return 0

