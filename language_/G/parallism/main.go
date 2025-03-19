package main

import (
	"fmt"
	"time"
	"runtime"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(time.Second) // Simulate work
		results <- job * 2
	}
}

func main() {

	runtime.GOMAXPROCS(4) // Use 4 CPU cores

	fmt.Println("Running with multiple cores!")

	// Worker pools efficiently manage multiple goroutines.
	const numWorkers = 5
	jobs := make(chan int, 5)
	results := make(chan int, 5)

	// Start worker goroutines
	for i := 1; i <= numWorkers; i++ {
		go worker(i, jobs, results)
	}

	// Send jobs
	for j := 1; j <= 5; j++ {
		jobs <- j
	}
	close(jobs)

	// Collect results
	for r := 1; r <= 5; r++ {
		fmt.Println("Result:", <-results)
	}
}
