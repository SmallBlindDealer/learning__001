
import java.util.*;


public class ClearFitApp {
    public static void main(String[] args) {
        ClearFitService service = new ClearFitService();
        service.addCenter("Koramangala", 5, 9, Arrays.asList("Weights", "Cardio", "Yoga", "Swimming"));
        service.addWorkout("Koramangala", "Weights", 6, 7, 100);
        
        System.out.println(service.viewWorkoutAvailability("Weights"));
        service.bookSession("Vaibhav", "Koramangala", "Weights", 6);
        System.out.println(service.viewWorkoutAvailability("Weights"));
        service.cancelSession("Vaibhav", "Koramangala", "Weights", 6);
        System.out.println(service.viewWorkoutAvailability("Weights"));
    }
}
