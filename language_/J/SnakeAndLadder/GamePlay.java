import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class GamePlay {
    public static void main(String[] args) {

        Deque<Player> players = new ArrayDeque<>();

        players.addLast(new Player("1", "shiv"));
        players.addLast(new Player("2", "shanker"));
        players.addLast(new Player("3", "Keshari"));

        List<Jumper> ladders = new ArrayList<>();
        ladders.add(new Jumper(7, 13));
        ladders.add(new Jumper(11, 27));
        ladders.add(new Jumper(31, 65));
        ladders.add(new Jumper(35, 82));

        List<Jumper> snakes = new ArrayList<>();
        ladders.add(new Jumper(25, 5));
        ladders.add(new Jumper(64, 36));
        ladders.add(new Jumper(96, 18));
        ladders.add(new Jumper(78, 43));

        BoardGame boardGame = new BoardGame(100, ladders, snakes, players);
        boardGame.gameStart();
    }
    

    
}
