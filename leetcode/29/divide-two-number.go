package main

import (
	"fmt"
	"math"
)

func divide(dividend int, divisor int) int {
	result := int(dividend / divisor)
	if result <= -int(math.Pow(2, 31)) {
		return -int(math.Pow(2, 31))
	}

	if result >= int(math.Pow(2, 31)) {
		return int(math.Pow(2, 31)) - 1
	}

	return result
}

func main() {
	fmt.Println(divide(-2147483648, -1))
}
