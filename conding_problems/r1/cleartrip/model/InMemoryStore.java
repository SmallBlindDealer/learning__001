package model;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InMemoryStore {
    public Map<String, Centre> centres;
    public Map<String, List<BookedSlotInfo>> users;

    public InMemoryStore() {
        centres = new HashMap<>();
        users = new HashMap<>();
    }

    // public Map<String, Centre> getCentreData() {
    //     return centres;
    // }

    // public Map<User, List<BookedSlotInfo>> getusersData() {
    //     return users;
    // }

}
