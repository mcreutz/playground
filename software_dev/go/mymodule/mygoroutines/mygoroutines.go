package mygoroutines

import (
	"fmt"
	"math"
	"sync"
)

func worker(id int, wg *sync.WaitGroup) {
	for i := 1; i <= 9; i++ {
		math.Sin(math.Cos(math.Tan(1)))
		// time.Sleep(time.Microsecond * 1)
		// fmt.Printf("Worker %d, step %d\n", id, i)
	}
	fmt.Printf("Worker %d done\n", id)
	wg.Done()
}

func Goroutines() {
	fmt.Println("----- Goroutines -----")
	var wg sync.WaitGroup
	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go worker(i, &wg)
	}
	wg.Wait()
}
