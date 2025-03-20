package service;
import java.util.*;

import model.Centre;
import model.InMemoryStore;
import model.TimeSlot;
import model.WorkOut;


public class CentreService {
    
    public InMemoryStore inMemoryStore;

    public CentreService(InMemoryStore inMemoryStore) {
        this.inMemoryStore = inMemoryStore;
    }


    public Centre addCentre(String name) {
        this.inMemoryStore.centres.put(name, new Centre(name));
        return this.inMemoryStore.centres.get(name);
    }


    public void addCentreTiming(String name, List<TimeSlot> timeSlots) {
        
        Centre centre = this.inMemoryStore.centres.get(name);
        if (centre!=null) {
            for(TimeSlot obj: timeSlots) {
                centre.addTiming(obj);
            }
        }
    }


    public void addCentreActivites(String name, List<String> activites) {

        Centre centre = this.inMemoryStore.centres.get(name);
        if (centre!=null) {
            for(String obj: activites) {
                centre.addActivity(obj);
            }
        }
    }


    public void addWorkOut(String centreName, String workoutType, int startTime, int endTime, int availableSlots) 
    {
        Centre centre = this.inMemoryStore.centres.get(centreName);
        WorkOut workOut = new WorkOut(workoutType, new TimeSlot(startTime, endTime), availableSlots);
        centre.addWorkOut(workoutType, workOut);
    }



    public void viewWorkOutAvailability(String activity) {
        List<String> sortedCentreNames = new ArrayList<>(this.inMemoryStore.centres.keySet());
        Collections.sort(sortedCentreNames); 

        for (String centreName: sortedCentreNames) {
            Centre centre = this.inMemoryStore.centres.get(centreName);
            List<WorkOut> workOutInfo = centre.getWorkOutInfo(activity);

            if (workOutInfo.size()>=1) {
                workOutInfo.sort((a, b)-> Integer.compare(a.timeSlot.startTime, b.timeSlot.startTime));
                for (WorkOut obj: workOutInfo) {
                    System.out.println(centreName + " " + activity + " " + obj.timeSlot.startTime + " " + obj.timeSlot.endTime + " "+ obj.availableSlots);
                }
            }
        }


    }

    public void viewWorkOutAvailability(String activity, String centreName) {
        
        Centre centre = this.inMemoryStore.centres.get(centreName);
        if (centre==null) {
            return;
        }
        List<WorkOut> workOutInfo = centre.getWorkOutInfo(activity);
        if (workOutInfo.size()>=1) {
            workOutInfo.sort((a, b)-> Integer.compare(a.availableSlots, b.availableSlots));
            for (WorkOut obj: workOutInfo) {
                System.out.println(centreName + " " + activity + " " + obj.timeSlot.startTime + " " + obj.timeSlot.endTime + " "+ obj.availableSlots);
            }
        }

    }
}
