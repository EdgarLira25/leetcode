package main

import (
	"fmt"
	"math"
	"regexp"
	"strconv"
	"strings"
)

func myAtoi(s string) int {
	s = strings.TrimSpace(s)
	sNew := ""
	for idx, character := range s {
		r, _ := regexp.Compile("^[^\\d-+]+$")
		match := r.MatchString(string(character))
		if match == false {
			if idx > 0 && (string(character) == "-" || string(character) == "+") {
				break
			}
			sNew += string(character)
		} else {
			break
		}
	}
	a, _ := strconv.Atoi(string(sNew))
	if a < -int(math.Pow(2, 31)) {
		return -int(math.Pow(2, 31))
	}
	if a > int(math.Pow(2, 31))-1 {
		return int(math.Pow(2, 31)) - 1
	}
	return a
}

func main() {
	fmt.Println(myAtoi("-5-"))

}
