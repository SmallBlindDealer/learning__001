
// You are given a list of tasks. Each task will have {id,queueTime,expectedExecutionTime}
// You need to return the order in which these task should be executed by a CPU.
// Your ordering should give preference to a task that has less expectedExecutionTime 
// among the available tasks when the cpu ready for the next task to be executed.

// Example: <t1,0,10> <t2,11,3> <t3,11,2>
// output: <t1,0,10> <t3,11,2> <t2,11,3>


import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

class Task {
    String id;
    Integer queueTime;
    Integer expectedExecutionTime;

    Task(String id, int queueTime, int expectedExecutionTime) {
        this.id = id;
        this.queueTime = queueTime;
        this.expectedExecutionTime = expectedExecutionTime;
    }

    @Override
    public String toString() {
        return "<id: " + id + "," + queueTime + "," + expectedExecutionTime + ">";
    }

    public Integer getExpectedExecutionTime() {
        return this.expectedExecutionTime;
    }

}


class CpuTaskSort {

    public static void main(String[] args) {
        List<Task> tasks = new ArrayList<>();

        tasks.add(new Task("t1", 0, 5));
        tasks.add(new Task("t2", 2, 3));
        tasks.add(new Task("t3", 3, 2));
        tasks.add(new Task("t4", 10, 1));
        tasks.add(new Task("t5", 7, 1));
        // t1 -->0--5 --t2 t3
        // t1 -->0--5 --t3--7 t2 t5
        // t1 -->0--5 --t3--7 --t5--8 t2
        // t1 -->0--5 --t3--7 --t5--8 --t2--10 t4
        // t1 -->0--5 --t3--7 --t5--8 --t2--10 t4--11

        tasks.sort((o1, o2)-> o1.queueTime.compareTo(o2.queueTime));
        Deque<Task> myQueue = new ArrayDeque<>(tasks);

        int timeSpent = 0;
        Queue<Task> q = new PriorityQueue<>((a, b)->a.expectedExecutionTime.compareTo(b.expectedExecutionTime));
        q.add(myQueue.pollFirst());

        while (!q.isEmpty()) {
            Task obj = q.poll();
            Integer expectedExecutionTime = obj.expectedExecutionTime;
            timeSpent+=expectedExecutionTime;
            System.out.println(timeSpent + " " + obj);
            while (!myQueue.isEmpty() && myQueue.getFirst().queueTime<=timeSpent) {
                Task curr = myQueue.pollFirst();
                q.add(curr);
            }
        }
    }
}