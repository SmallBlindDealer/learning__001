
import java.util.ArrayList;
import java.util.List;

import model.InMemoryStore;
import model.TimeSlot;
import service.CentreService;
import service.UserService;


public class ClearFit {

    public static void main(String[] args) {

        InMemoryStore inMemoryStore = new InMemoryStore();

        CentreService centreService = new CentreService(inMemoryStore);
        UserService userService = new UserService(inMemoryStore);

        String centreName = "Koramangala";
        centreService.addCentre(centreName);
        centreService.addCentreTiming(centreName, new ArrayList<>(List.of(
            new TimeSlot(18, 21), 
            new TimeSlot(6, 9))));

        centreService.addCentreActivites(centreName, new ArrayList<>(List.of("Weights", "Cardio", "Yoga", "Swimming")));
        centreService.addWorkOut(centreName, "Weights", 6, 7, 100);
        centreService.addWorkOut(centreName, "Swimming", 7, 8, 150);


        String centreName2 = "Bellandur";
        centreService.addCentre(centreName2);
        centreService.addCentreTiming(centreName2, new ArrayList<>(List.of(new TimeSlot(7, 10))));
        centreService.addCentreActivites(centreName2, new ArrayList<>(List.of("Weights", "Cardio", "Yoga")));
        centreService.addWorkOut(centreName2, "Weights", 7, 8, 100);
        centreService.addWorkOut(centreName2, "Weights", 9, 10, 100);

        centreService.viewWorkOutAvailability("Weights");
        String user1 = "Shiv";
        userService.register(user1);
        userService.bookSession(user1, centreName2, "Weights", 7, 8);
        centreService.viewWorkOutAvailability("Weights");



    }

    
    
}
