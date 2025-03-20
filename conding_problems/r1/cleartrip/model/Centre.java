package model;


import java.util.*;


public class Centre {
    String name;
    List<TimeSlot> timings;
    Set<String> activities;
    // Map<String, Map<Integer, String>> workoutSlots;
    Map<String, List<WorkOut>> workoutSlots;

    public Centre(String name) {
        this.name = name;
        this.timings = new ArrayList<>();
        this.activities = new HashSet<>();
        this.workoutSlots = new HashMap<>();
    }

    public void addTiming(TimeSlot timeslot) {
        this.timings.add(timeslot);
    }

    public void addActivity(String activity) {
        this.activities.add(activity);
    }

    public void addWorkOut(String activity, WorkOut workOut) {
        List<WorkOut> workOutL = new ArrayList<>();
        if (this.workoutSlots.get(activity)!=null) {
            workOutL = this.workoutSlots.get(activity);
        }
        workOutL.add(workOut);
        this.workoutSlots.put(activity, workOutL);

    }

    public List<WorkOut> getWorkOutInfo(String activity) {
        if (this.workoutSlots.get(activity)!=null) {
            return this.workoutSlots.get(activity);
        }
        return null;
    }

    public void updateWorkOut(String activity) {

    }


}