
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;


class ClearFitService {
    Map<String, Center> centers = new ConcurrentHashMap<>();

    public void addCenter(String name, int openTime, int closeTime, List<String> activities) {
        centers.put(name, new Center(name, openTime, closeTime, activities));
    }

    public void addWorkout(String centerName, String workoutType, int startTime, int endTime, int seats) {
        Center center = centers.get(centerName);
        if (center != null && startTime >= center.openTime && endTime <= center.closeTime) {
            center.slots.put(startTime, new WorkoutSlot(workoutType, startTime, endTime, seats));
        }
    }

    public List<String> viewWorkoutAvailability(String workoutType) {
        List<String> result = new ArrayList<>();
        for (Center center : centers.values()) {
            for (WorkoutSlot slot : center.slots.values()) {
                if (slot.workoutType.equals(workoutType)) {
                    result.add(center.name + " " + workoutType + " " + slot.startTime + " " + slot.endTime + " " + slot.availableSeats);
                }
            }
        }
        return result;
    }

    public boolean bookSession(String user, String centerName, String workoutType, int startTime) {
        Center center = centers.get(centerName);
        if (center != null) {
            WorkoutSlot slot = center.slots.get(startTime);
            if (slot != null && slot.workoutType.equals(workoutType)) {
                slot.lock.lock();
                try {
                    if (slot.availableSeats > 0) {
                        slot.bookedUsers.add(user);
                        slot.availableSeats--;
                        return true;
                    } else {
                        slot.interestList.add(user);
                    }
                } finally {
                    slot.lock.unlock();
                }
            }
        }
        return false;
    }

    public void cancelSession(String user, String centerName, String workoutType, int startTime) {
        Center center = centers.get(centerName);
        if (center != null) {
            WorkoutSlot slot = center.slots.get(startTime);
            if (slot != null && slot.bookedUsers.contains(user)) {
                slot.lock.lock();
                try {
                    slot.bookedUsers.remove(user);
                    slot.availableSeats++;
                    if (!slot.interestList.isEmpty()) {
                        String nextUser = slot.interestList.poll();
                        System.out.println("Notification sent to " + nextUser);
                    }
                } finally {
                    slot.lock.unlock();
                }
            }
        }
    }
}
