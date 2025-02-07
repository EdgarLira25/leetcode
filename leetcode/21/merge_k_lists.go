package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func print(list *ListNode) {
	for list != nil {
		fmt.Println(list.Val)
		list = list.Next
	}
}
func len_bigger_than_1(list *ListNode) bool {
	if list != nil {
		return true
	}
	return false
}

func exclude_nil_lists(lists []*ListNode) []*ListNode {
	list_temp := []*ListNode{}
	for _, list := range lists {
		if len_bigger_than_1(list) {
			list_temp = append(list_temp, []*ListNode{list}...)
		}
	}
	return list_temp

}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

	lists := []*ListNode{list1, list2}

	lists = exclude_nil_lists(lists)
	if len(lists) == 1 {
		return lists[0]
	} else if len(lists) == 0 {
		return nil
	}

	main_node := lists[0]
	other_lists := lists[1:]

	for _, list := range other_lists {
		ant := list
		atual := list
		atual_main_node := main_node

		for atual_main_node != nil || len_bigger_than_1(atual) == true {
			if atual_main_node == nil {
				ant.Next = atual
				break
			}
			if atual != nil && atual.Val <= atual_main_node.Val && atual == ant {
				temp := atual.Next
				atual.Next = atual_main_node
				atual_main_node = atual
				main_node = atual
				atual = temp
			} else if atual != nil && atual.Val <= atual_main_node.Val {
				for atual != nil && ant.Val <= atual.Val && atual.Val <= atual_main_node.Val {
					temp := atual.Next
					atual.Next = ant.Next
					ant.Next = atual
					ant = atual
					atual = temp
				}
			} else if atual.Val >= atual_main_node.Val && atual_main_node.Next == nil {
				atual_main_node.Next = atual
				break
			}

			if atual == nil {
				break
			}

			ant = atual_main_node
			atual_main_node = atual_main_node.Next
		}
	}

	return main_node
}

func createLinkedList(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	head := &ListNode{Val: values[0]}
	current := head
	for _, val := range values[1:] {
		current.Next = &ListNode{Val: val}
		current = current.Next
	}
	return head
}

// func main() {
// 	list1Values := []int{1, 3, 4, 6, 8, 9, 12}
// 	// list2Values := []int{1, 2, 5, 7, 11, 21, 24}
// 	list3Values := []int{-4, 0, 4, 7, 10, 14, 22, 29}
//
// 	// Criando as listas encadeadas
// 	list1 := createLinkedList(list1Values)
// 	// list2 := createLinkedList(list2Values)
// 	list3 := createLinkedList(list3Values)
//
// 	// Agrupando as listas em um slice
// 	lists := []*ListNode{list1, list3}
//
// 	print(mergeKLists(lists))
// 	// Exemplo de uso
// 	// fmt.Println(lists) // Mostra o endereço das listas encadeadas
//
// }

func main() {

	// node1 := &ListNode{Val: 1}
	// node2 := &ListNode{Val: 7}
	// node3 := &ListNode{Val: 0}
	// node4 := &ListNode{Val: 5}
	// node5 := &ListNode{Val: 2}
	// node6 := &ListNode{Val: 3}
	//
	// // Ligando os nós para formar listas encadeadas
	// node1.Next = node2
	// node3.Next = node4
	// node5.Next = node6
	// listOfLists := []*ListNode{node1, node3, node5}

	// Lista com um único nó: [-2]
	nodeA := &ListNode{Val: 2}
	list2 := nodeA
	// Lista com múltiplos nós: [-3, -2, 1]
	nodeB := &ListNode{Val: 1}
	nodeC := &ListNode{Val: 3}
	nodeD := &ListNode{Val: 4}
	nodeB.Next = nodeC
	nodeC.Next = nodeD
	list3 := nodeB
	// print(nodeB)

	// Conjunto das listas
	lists := []*ListNode{list2, list3}
	print(mergeKLists(lists))

}
