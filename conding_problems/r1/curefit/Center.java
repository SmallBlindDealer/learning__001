import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

class Center {
    String name;
    List<String> activities;
    int openTime, closeTime;
    Map<Integer, WorkoutSlot> slots = new ConcurrentHashMap<>();

    public Center(String name, int openTime, int closeTime, List<String> activities) {
        this.name = name;
        this.openTime = openTime;
        this.closeTime = closeTime;
        this.activities = new ArrayList<>(activities);
    }
}
