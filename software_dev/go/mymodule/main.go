// Package description goes here
package main

// outside of functions, every statement begins with a keyword (import, var, const, func, ..)

import (
	"fmt" //from standard library (https://pkg.go.dev/fmt)
	"runtime"
	"time"

	"mymodule/myfunctions"
	"mymodule/mygoroutines"
)

// Function description goes here
func main() {
	consoleOutput()
	localVariables()
	typeConversion()
	arrays()
	slices()
	readUserInput()
	byteshiftOperators()
	for_loops()
	conditionals()
	switch_case()
	deferring()
	myfunctions.Functions()
	// mypointers.PointersToPrimitives()
	// mystructs.Structs()
	// mymethods.Methods()
	mygoroutines.Goroutines()
}

// variables at package level
var one, two bool        // initialized to 'false'
var five, six = 5, "six" // if an initialization value is given, the type can be omitted

func consoleOutput() {
	fmt.Println("----- Console Output -----")
	// Println prints a line to the console. Variables are formatted by their standard. Values are separated by spaces.
	fmt.Println("Hello", "World", 123, 3.14, one, two, five, six)
	// Printf prints a formatted string to the console. The format is specified by a format string. Newline is not appended.
	fmt.Printf("Hello %v %v %v %v %v\n", "World", 123, 3.14, true, 1+2i)
}

func localVariables() {
	//simple variables and constants declaration at function level
	fmt.Println("----- Local Variables -----")
	var myVariable = "Something" // type inference
	const myConstant = 20
	fmt.Println("Some text", myVariable, "some more text.")
	// primitive types: string, int, uint,
	var three, four bool
	seven := "seven" // ':='-notation can be used insted of a 'var'-statement, but only within functions
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
}

func typeConversion() {
	fmt.Println("----- Type Conversion -----")
	i := 42
	f := float64(i)
	u := uint(f)
	fmt.Println(u)
}

func arrays() {
	fmt.Println("----- Arrays -----")

	var arrayName = [50]string{"one", "two", "three"} //fixed length array
	fmt.Println(arrayName[0])

	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)
	fmt.Println(a[len(a)-1]) // last element
}

func slices() {
	fmt.Println("----- Slices -----")

	// slices are like references to arrays
	arr := [6]int{2, 3, 5, 7, 11, 13}
	var slc []int = arr[1:4] // begin is inclusive, end is exclusive
	fmt.Println(slc)
	// omitting the low index implies 0
	fmt.Println(arr[:3])
	// omitting the high index implies len(s)
	fmt.Println(arr[4:])

	// slices can be larger than the underlying array
	var bigSlc []int = arr[:]
	slc = append(bigSlc, 17)
	fmt.Println(len(arr))
	fmt.Println(len(bigSlc))

	// nil slices
	var nslc []int
	nslc = append(nslc, 1)
	nslc = append(nslc, 2)
	fmt.Println(slc)
	fmt.Println(len(nslc))
	fmt.Println(cap(nslc))
}

func readUserInput() {
	fmt.Println("----- Read User Input -----")
	var answer string
	fmt.Print("Query: ")
	fmt.Scan(&answer) //pointer
	fmt.Printf("Answer was: %v\n", answer)
}

func byteshiftOperators() {
	fmt.Println("----- Byteshift Operators -----")
	// '>>', '<<' are byte-shift operators.
	// mil = 1 << 6
}

func for_loops() {
	fmt.Println("----- For Loops -----")
	// full syntax
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	// shortened syntax
	counter := 1
	for counter < 10 { // The init and post-statements are optional
		counter += 1
	}
	fmt.Println(counter)

	// There is no 'while' in Go. A 'for' without statements acts like a 'while'
	while_counter := 1
	for {
		while_counter++
		if while_counter > 10 {
			break
		}
	}
	fmt.Println(while_counter)
}

func conditionals() int {
	fmt.Println("----- Conditionals -----")
	if c := 12; c > 10 { // init statement; condition. init-statement can be omitted
		return c
	} else {
		return 2 * c // The 'elese'-staement is optional
	}
}

func switch_case() {
	fmt.Println("----- Switch Case -----")
	// switch with initializer
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

	// switch with conditions
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good day.")
	}
}

func deferring() {
	fmt.Println("----- Deferring -----")
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
