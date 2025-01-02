package main


type Queue struct {
	items []*interface{}
}

func (q *Queue) Dequeue() interface{} {
	if len(q.items)==0 {
		return nil
	}
	first := q.items[0]
	q.items = q.items[1:]
	return *first

}
func (q *Queue) Add(item interface{}) {
	q.items = append(q.items, &item)
}
