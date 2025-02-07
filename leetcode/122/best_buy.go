package main

func maxProfit(prices []int) int {
	profit := 0
	for index := 1; index < len(prices); index++ {
		if prices[index]-prices[index-1] < 0 {
			profit += prices[index] - prices[index-1]
		}
	}
	return profit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
    maxProfit(prices)
}
