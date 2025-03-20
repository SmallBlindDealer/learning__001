package service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.ReentrantLock;

import model.BookedSlotInfo;
import model.Centre;
import model.InMemoryStore;
import model.TimeSlot;
import model.WorkOut;

public class UserService {
    private static ReentrantLock lock = new ReentrantLock();
    
    public InMemoryStore inMemoryStore;

    public UserService(InMemoryStore inMemoryStore) {
        this.inMemoryStore = inMemoryStore;
    }

    public void register(String userName) {
        if (this.inMemoryStore.users.get(userName)==null) {
            this.inMemoryStore.users.put(userName, new ArrayList<>());
        }

    }

    synchronized public void bookSession(String userName, String centreName, String activity, int startTime, int endTime) {


        if (this.inMemoryStore.users.get(userName)==null) {
            return;
        }

        Centre centre = this.inMemoryStore.centres.get(centreName);
        if (centre==null) {
            return;
        }

        List<WorkOut> workOutInfo = centre.getWorkOutInfo(activity);

        for(WorkOut obj: workOutInfo) {

            if (obj.availableSlots<=0 || startTime<obj.timeSlot.startTime || endTime>obj.timeSlot.endTime) {
                continue;
            }
            lock.lock();
            obj.availableSlots-=1;
            BookedSlotInfo bookedInfo = new BookedSlotInfo(centre, activity, new TimeSlot(startTime, endTime), obj);
            this.inMemoryStore.users.get(userName).add(bookedInfo);
            lock.unlock();
            break;

        }
        
    }

    public void cancelSession(String userName, String centreName, String activity, int startTime, int endTime) {
        

        if (this.inMemoryStore.users.get(userName)==null) {
            return;
        }
        List<BookedSlotInfo> bookedSlotInfos = this.inMemoryStore.users.get(userName);
        if (bookedSlotInfos==null) {
            return;
        }
        BookedSlotInfo bookedSlotInfoObj = null;

        for (BookedSlotInfo obj: bookedSlotInfos) {
            if (obj.activity==activity && obj.timeSlot.startTime==startTime && obj.timeSlot.endTime==endTime) {
                bookedSlotInfoObj = obj;
                break;
            }
        }
        if (bookedSlotInfoObj!=null) {
            // remove from user slots info
            lock.lock();
            bookedSlotInfos.remove(bookedSlotInfoObj);
            // inc workout count
            bookedSlotInfoObj.workOut.availableSlots+=1;
            lock.unlock();
        }



    }

}
