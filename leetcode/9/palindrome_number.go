package main

import "strconv"

func isPalindrome(x int) bool {

	if x < 0 {
		return false
	}

	abcde := strconv.Itoa(x)
	var reversed string = ""

	for _, x := range abcde {
		reversed = string(x) + reversed
	}

	if reversed != abcde {
		return false
	}
	return true
}

func main() {

}
