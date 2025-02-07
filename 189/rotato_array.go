package main

import "fmt"

func rotate(nums []int, k int) {
	if k < len(nums) {
		new_nums := append(nums[len(nums)-k:], nums[0:len(nums)-k]...)
		copy(nums, new_nums)
	} else {
		for i := 0; i < k; i++ {
			new_nums := append([]int{nums[len(nums)-1]}, nums[0:len(nums)-1]...)
			copy(nums, new_nums)
		}
	}
}

func rotate2(nums []int, k int) {
	for i := 0; i < k; i++ {
		new_nums := append([]int{nums[len(nums)-1]}, nums[0:len(nums)-1]...)
		copy(nums, new_nums)
	}
}

func main() {
	abc := []int{1, 2, 3}
	rotate2(abc, 1)
	fmt.Println(abc)
}
