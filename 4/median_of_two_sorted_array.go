package main

import "fmt"

func insert_ordened(nums1 []int, val int, index int) []int {
	left_list_temp := nums1[:index]
	right_list_temp := nums1[index:]
	right_list_temp = append([]int{val}, right_list_temp...)
	new_list := append(left_list_temp, right_list_temp...)
	return new_list
}

func take_median(nums []int) float64 {
	even := len(nums) % 2
	if even == 0 {
		return float64(nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)]) / 2
	} else {
		return float64(nums[int(len(nums)/2)])
	}
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	idx := 0
	if len(nums2) == 0 && len(nums1) == 0 {
		return 0
	}
	if len(nums2) == 0 {
		return take_median(nums1)
	}
	if len(nums1) == 0 {
		return take_median(nums2)
	}

	atual := nums2[0]
	nums2 = nums2[1:]
	for idx < len(nums1) {
		for idx < len(nums1)-1 && atual > nums1[idx] {
			idx += 1
		}
		if atual <= nums1[idx] {
			nums1 = insert_ordened(nums1, atual, idx)
		} else if atual > nums1[len(nums1)-1] {
			nums1 = insert_ordened(nums1, atual, idx+1)
		}

		if len(nums2) > 0 {
			atual = nums2[0]
			nums2 = nums2[1:]
		} else {
			break
		}
	}
	fmt.Println(nums1)
	return take_median(nums1)
}

func main() {
	array1 := []int{2, 2, 4, 4}
	array2 := []int{2, 2, 2, 4, 4}
	fmt.Println("2", findMedianSortedArrays(array1, array2))
}
