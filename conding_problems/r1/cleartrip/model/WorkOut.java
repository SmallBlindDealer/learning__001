package model;
public class WorkOut {
    
    public String workoutType;
    public TimeSlot timeSlot;
    public int availableSlots;

    public WorkOut(String workoutType, TimeSlot timeSlot, int availableSlots) {
        this.workoutType = workoutType;
        this.timeSlot = timeSlot;
        this.availableSlots = availableSlots;
    }
}
