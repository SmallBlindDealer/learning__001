import java.util.*;
import java.util.concurrent.locks.ReentrantLock;




class WorkoutSlot {
    String workoutType;
    int startTime, endTime, availableSeats;
    Set<String> bookedUsers = Collections.synchronizedSet(new HashSet<>());
    Queue<String> interestList = new LinkedList<>();
    ReentrantLock lock = new ReentrantLock();

    public WorkoutSlot(String workoutType, int startTime, int endTime, int seats) {
        this.workoutType = workoutType;
        this.startTime = startTime;
        this.endTime = endTime;
        this.availableSeats = seats;
    }
}
