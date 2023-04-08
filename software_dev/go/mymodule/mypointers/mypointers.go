package mypointers

import "fmt"

func PointersToPrimitives() {
	i, j := 42, 2701

	p := &i         // p is a pointer to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j

	//&: address of
	//*: value at adress
}
