package mygoroutines

import (
	"fmt"
	"math"
	"sync"
)

// a worker fucntion that does some work
func worker(id int, wg *sync.WaitGroup) {
	for i := 1; i <= 9; i++ {
		math.Sin(math.Cos(math.Tan(1)))
		// time.Sleep(time.Microsecond * 1)
		// fmt.Printf("Worker %d, step %d\n", id, i)
	}
	fmt.Printf("Worker %d done\n", id)
	wg.Done()
}

// a go function, that shows the usage of goroutines
func Goroutines() {
	fmt.Println("----- Goroutines -----")
	var wg sync.WaitGroup
	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go worker(i, &wg)
	}
	wg.Wait()
}

// worker function that waits for a task on a channel and reports a result back
func worker2(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Printf("Worker %d, job %d\n", id, j)
		results <- j * 2
	}
}

// manager function calling the worker functions
func manager(jobs chan<- int, results <-chan int) {
	for i := 1; i <= 9; i++ {
		jobs <- i
	}
	close(jobs)
	for a := 1; a <= 9; a++ {
		<-results
	}
}
