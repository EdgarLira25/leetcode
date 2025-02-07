package main

import (
	"fmt"
	"strconv"
    "math/big"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	number_string_1 := ""
	for current := l1; current != nil; current = current.Next {
		number_string_1 = fmt.Sprint(current.Val) + number_string_1
	}

	number_string_2 := ""
	for current := l2; current != nil; current = current.Next {
		number_string_2 = fmt.Sprint(current.Val) + number_string_2
	}

    number_int_1 := new(big.Int)
    number_int_1.SetString(number_string_1, 10)
    number_int_2 := new(big.Int)
    number_int_2.SetString(number_string_2, 10)
    
    number_int_1.Add(number_int_1, number_int_2)

	item := &ListNode{}
	for idx, current := range number_int_1.String() {
		val, _ := strconv.Atoi(string(current))
		if item.Next == nil && idx == 0{
			item.Val = val
			continue
		}

		item = &ListNode{val, item}
	}

	return item
}

func main() {
    // x := 1000000000000000000000000000001
    largeNumber := new(big.Int)
    largeNumber.SetString("1000000000000000000000000000001", 10)
    fmt.Println(largeNumber)

	// node9 := &ListNode{Val: 6}
	// node8 := &ListNode{Val: 7, Next: node9}
	// node7 := &ListNode{Val: 8, Next: node8}
	// node3 := &ListNode{Val: 1}
	// node2 := &ListNode{Val: 2, Next: node3}
	// node1 := &ListNode{Val: 3, Next: node2}
	//
	// abc := addTwoNumbers(node1, node7)
	// fmt.Println("-----")
	// for abc != nil {
	// 	fmt.Println(abc.Val)
	// 	abc = abc.Next
	// }
}
