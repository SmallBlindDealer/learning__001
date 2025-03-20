package model;



public class BookedSlotInfo {
    public Centre centre;
    public String activity;
    public TimeSlot timeSlot;
    public WorkOut workOut;

    public BookedSlotInfo(Centre centre, String activity, TimeSlot timeSlot, WorkOut workOut) {
        this.centre = centre;
        this.activity = activity;
        this.timeSlot = timeSlot;
        this.workOut = workOut;
    }
}
