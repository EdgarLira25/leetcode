package main

import "fmt"

func isValid(s string) bool {
	stack := []rune{}
	pairs := map[rune]rune{')': '('}

	for _, char := range s {
		switch char {
		case '(':
			stack = append(stack, char)
		case ')':
			if len(stack) == 0 || stack[len(stack)-1] != pairs[char] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func generateParenthesis(n int) []string {

	parenthesis := []string{"("}
	for i := 0; i < n*2-1; i++ {
		temp := []string{}
		for _, index := range parenthesis {
			temp = append(temp, string(index)+"(")
			temp = append(temp, string(index)+")")
		}
		parenthesis = temp
	}
	valid_list := []string{}
	for _, item := range parenthesis {
		if isValid(item) {
			valid_list = append(valid_list, item)
		}
	}
	return valid_list
}

func main() {
	fmt.Println(generateParenthesis(3))
}
