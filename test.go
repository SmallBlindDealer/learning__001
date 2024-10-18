package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Hello World!")
	a := 5
	a = 3
	var a2 string = "Shiv"
	fmt.Println(a)
	fmt.Println(a2)

	var arr [4]int
	fmt.Println(arr)

	var arr2 = [4]int{1,2,3}
	fmt.Println(arr2)

	var hashMap = make(map[string]string)
	hashMap["1"] = "shiv"
	hashMap["2"] = "shankar"
	hashMap["3"] = "keshari"

	for k, v:= range hashMap {
		fmt.Printf("key: %v, val: %v\n", k, v)
	}
	

	fmt.Println(time.Now())
	pTime := time.Now()
  	time.Sleep(5*time.Second)
	fmt.Println(pTime.Format("01-02-2006"))
}
