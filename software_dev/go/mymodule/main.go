// Package description goes here
package main

// outside of functions, every statement begins with a keyword (import, var, const, func, ..)

import (
	"fmt" //from standard library (https://pkg.go.dev/fmt)
	"math/rand"
	"runtime"
	"time"

	"mymodule/mypointers"
)

// Function description goes here
func main() {
	localVariables()
	arrays()
	readUserInput()
	byteshiftOperators()
	Add(12, 13)
	mypointers.PointersToPrimitives()
}

// varaibles at package level
var one, two bool
var five, six = 5, "six" // if an initialization value is given, the type can be omitted

func localVariables() {
	//simple variables and constants
	var myVariable = "Something" // type inference
	const myConstant = 20
	fmt.Println("Hello World!")
	fmt.Println("Some text", myVariable, "some more text.")
	// primitive types: string, int, uint,

	// varaible declaration at function level
	var three, four bool
	seven := "seven" // this can be used insted of a 'var'-statement, but only within functions
	fmt.Println("varaible declaration at function level")
	fmt.Println(three, four, seven)
	fmt.Println()

	// Auto initialization
	// if variables are not explicitly initialized at declaration, they are implicitly initialized by the runtime.
	// zero for numeric types, false for bool, "" for string
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)

	// auto initialization
	var myUninitializedVariable string
	fmt.Println(myUninitializedVariable) // outputs "", because Go automatically initializes variables
	myUninitializedVariable = "Anything"
	fmt.Printf("My %v Text.\n", myUninitializedVariable)

	// Type conversions
	ii := 42
	ff := float64(ii)
	uu := uint(ff)
	fmt.Println(uu)

	// Formatting
	my_var := 10
	fmt.Printf("Value: %v", my_var)
	fmt.Printf("Type: %T", my_var)
}

func arrays() {
	var arrayName = [50]string{"one", "two", "three"} //fixed length array
	fmt.Println(arrayName[0])

	// // Arrays
	// var a [2]string
	// a[0] = "Hello"
	// a[1] = "World"
	// fmt.Println(a[0], a[1])
	// fmt.Println(a)

	// primes := [6]int{2, 3, 5, 7, 11, 13}
	// fmt.Println(primes)

	var arr []int
	arr = append(arr, 1)
	arr = append(arr, 2)
	fmt.Println(arr)
	fmt.Println(len(arr))
	fmt.Println(cap(arr))

	// // Slices
	// var ss []int = primes[1:4]
	// fmt.Println(ss)
}

func readUserInput() {
	// reading user input
	var answer string
	fmt.Print("Query: ")
	fmt.Scan(&answer) //pointer
	fmt.Printf("Answer was: %v\n", answer)

	fmt.Println("My favorite number is", rand.Intn(10))
	// 'Println' can be called from 'fmt', because it is public. Go calls this 'exported'.
	// You can 'export' fuctions from a package by starting their name with a capital letter.
	a, b := multipleReturnValues("hello", "world")
	fmt.Println(a, b)
}

func byteshiftOperators() {
	// '>>', '<<' are byte-shift operators.
	// mil = 1 << 6
}

// takes two int parameters and returns an int
func Add(x int, y int) int {
	return x + y
}

// shortened parameters syntax, multiple return values
func multipleReturnValues(x, y string) (string, string) {
	return y, x
}

// returning named variables
func namedReturnValues(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func for_loops() {
	// full syntax
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	// shortened syntax
	counter := 1
	for counter < 1000 { // The init and post-statements are optional
		counter += counter
	}
	fmt.Println(counter)
	// There is no 'while' in Go. A shortened 'for' acts like a 'while'
	// 'for {...}' will loop ... forever
}

func conditionals() int {
	if c := 12; c > 10 { // init statement; condition. init-statement can be omitted
		return c
	} else {
		return 2 * c // The 'elese'-staement is optional
	}
}

func switch_case() {
	// switch with initializer and condition
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}

	// switch without initializer and condition
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}

func deferring() {
	// A defer statement defers the execution of a function until the surrounding function returns.
	// The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.
	defer fmt.Println("world")
	fmt.Println("hello")

	// Stacked defers (LIFO)
	fmt.Println("counting")
	for i := 0; i < 3; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("done")
	// > counting
	// > done
	// > 2
	// > 1
	// > 0
}
