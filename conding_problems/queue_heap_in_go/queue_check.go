package main

import (
	"fmt"
)

func main() {
	a := &Queue{}
	a.Add("a")
	a.Add("b")
	fmt.Println(a.items)
	fmt.Println(a.Dequeue())
	fmt.Println(a.items)
	fmt.Println("->>--->")
}
