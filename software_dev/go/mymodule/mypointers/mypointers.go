package mypointers

import "fmt"

func Pointers() {
	fmt.Println("----- Pointers -----")
	pointersToPrimitives()
	pointersToArrays()
	pointersToSlices()
	pointersToStructs()
}

func pointersToPrimitives() {
	fmt.Println("Pointers to Primitives")
	//&: address of
	//*: value at adress

	i, j := 42, 2701

	p := &i         // p is a pointer to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j
}

func pointersToArrays() {
	fmt.Println("Pointers to Arrays")
	arr := [3]int{1, 2, 3}
	p := &arr
	fmt.Println(p)
	fmt.Println(*p)
	fmt.Println((*p)[0])
	fmt.Println((*p)[1:2])
}

func pointersToSlices() {
	fmt.Println("Pointers to Slices")
	slc := []int{1, 2, 3}
	p := &slc
	fmt.Println(p)
	fmt.Println(*p)
	fmt.Println((*p)[0])
	fmt.Println((*p)[1:2])
}

func pointersToStructs() {
	fmt.Println("Pointers to Structs")
	type Vertex struct {
		X int
		Y int
	}
	v := Vertex{1, 2}
	p := &v
	fmt.Println(p)
	fmt.Println(*p)
	fmt.Println((*p).X)
	fmt.Println(p.X) // shorthand for (*p).X
}
