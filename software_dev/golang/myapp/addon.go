// {}

package main
// outside of functions, every statement begins with a keyword (import, var, func, ..)

import (
    "fmt"
    "math/rand"
)

// varaibles at package level
var one, two bool
var five, six = 5, "six" // if an initialization value is given, the type can be omitted

func local_variables(){
    // varaible declaration at function level
    var three, four bool
    seven := "seven" // this can be used insted of a 'var'-statement, but only within functions

    // Auto initialization
    // if variables are not explicitly initialized at declaration, they are implicitly initialized by the runtime.
    // zero for numeric types, fals for bool, "" for string
    var i int
    var f float64
    var b bool
    var s string
    fmt.Printf("%v %v %v %q\n", i, f, b, s)

    // Type conversions
    i := 42
    f := float64(i)
    u := uint(f)

    // Formatting
    my_var := 10
    fmt.Printf("Value: %v", my_var)
    fmt.Printf("Type: %T", my_var)

    // Arrays
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)

    // Slices
    var s []int = primes[1:4]
	fmt.Println(s)
}

func add(x int, y int) int {
	// takes two int parameters and returns an int
    return x + y
}

func swap(x, y string) (string, string) {
    // shortened parameters syntax
    // multiple return values
	return y, x
}

func split(sum int) (x, y int) {
	// returning named variables
    x = sum * 4 / 9
	y = sum - x
	return
}

func for_loops(){
    // full syntax
    sum := 0
    for i := 0; i < 10; i++ {
        sum += i
    }
    fmt.Println(sum)

    // shortened syntax
	sum := 1
	for sum < 1000 {  // The init and post-statements are optional
		sum += sum
	}
	fmt.Println(sum)
    // There is no 'while' in Go. A shortened 'for' acts like a 'while'
    // 'for {...}' will loop ... forever
}

func conditionals() int {
    if c := 12; c > 10 { // init statement; condition. init-statement can be omitted
		return c
	} else {
        return 2 * c  // The 'elese'-staement is optional
    }
	return 0
}

func switch() {
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

func pointers() {
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

type Point struct {
	X int
	Y int
}

var (
	v1 = Point{1, 2}  // has type Point
	v2 = Point{X: 1}  // Y:0 is implicit
	v3 = Point{}      // X:0 and Y:0
	p  = &Point{1, 2} // has type *Point
)

func point_user() {
    fmt.Println(Point{1, 2})
    
    v := Point{10, 20}
	v.X = 4
	fmt.Println(v.X)

    v := Point{1, 2}
	p := &v
	p.X = 1e9  // actually (*p).X, but p.X is permitted
	fmt.Println(v)
}


func main()  {
    fmt.Println("My favorite number is", rand.Intn(10))
    // 'Println' can be called from 'fmt', because it is public. Go calls this 'exported'.
    // You can 'export' fuctions from a package by starting their name with a capital letter.
    a, b := swap("hello", "world")
    // '>>', '<<' are byte-shift operators. 
    // mil = 1 << 6
}
