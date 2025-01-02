package main

import (
	"container/heap"
	"fmt"
	"strconv"
	"strings"
)


type IntHeap []int

func findSortestDistance(start, end string, graph map[string]map[string]int) []string {
	var visitedSet = make(map[string]bool)
	
	if _, ok:=visitedSet[start]; ok {
		return []string{""}
	}
	if start==end {
		return []string{end}
	}
	return nil

}

func asd(arr []string) {
	total, _ := strconv.Atoi(arr[0])
	graph := make(map[string]map[string]int)
	for i:= total+1; i<len(arr); i++ {
		s := strings.Split(arr[i], "|")
		var start, end, cost = s[0], s[1], s[2]
		cost_, _ := strconv.Atoi(cost)
		if _, ok:=graph[start]; ok==false {
			graph[start] = map[string]int{}
		}
		if _, ok:=graph[end]; ok==false {
			graph[end] = map[string]int{}
		}
		graph[start][end] = cost_
		graph[end][start] = cost_

	}
	start :=arr[1]
	end :=arr[1+total-1]
	findSortestDistance(start, end, graph)
}


func main() {
	asd([]string{"4", "A", "B","C", "D", "A|B|1", "B|D|9", "B|C|3", "C|D|4"})
}


