package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func main() {
	t0 := time.Now()
	for i := 0; i < 1e7; i++ {
		math.Sin(math.Cos(rand.Float64()))
	}
	fmt.Println(time.Since(t0))
}
