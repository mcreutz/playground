package myfunctions

import "fmt"

func Functions() {
	fmt.Println("----- Functions -----")
	res := functionWithParameters(12, 13)
	fmt.Println(res)
	a, b := functionWithMultipleReturnValues("Hello", "World")
	fmt.Println(a, b)
	one, two := functionWithNamedReturnValues(17)
	fmt.Println(one, two)
}

// takes two int parameters and returns an int
func functionWithParameters(x int, y int) int {
	return x + y
}

// shortened parameters syntax, multiple return values
func functionWithMultipleReturnValues(x, y string) (string, string) {
	return y, x
}

// returning named variables
func functionWithNamedReturnValues(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
