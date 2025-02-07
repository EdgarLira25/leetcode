package main

import (
	"fmt"
	"math"
	"strconv"
)

func reverse(x int) int {
	reversed := ""
	for _, value := range strconv.Itoa(x) {
		if len(reversed) > 0 && string(reversed[0]) == "-" {
			reversed = string(reversed[0]) + string(value) + reversed[1:]
		} else {
			reversed = string(value) + reversed
		}
	}
	reversed_int, _ := strconv.Atoi(reversed)
	if reversed_int < -int(math.Pow(2, 31)) || reversed_int > int(math.Pow(2, 31)-1) {
		return 0
	}
	return reversed_int
}

func main() {
	fmt.Println(reverse(1534236469))

}
