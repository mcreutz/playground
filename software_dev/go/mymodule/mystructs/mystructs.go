package mystructs

import "fmt"

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
	fmt.Println("----- Structs -----")

	fmt.Println(Point{1, 2})

	v := Point{10, 20}
	v.X = 4
	fmt.Println(v.X)

	vv := Point{1, 2}
	p := &vv
	p.X = 1e9 // actually (*p).X, but p.X is permitted
	fmt.Println(vv)
}
