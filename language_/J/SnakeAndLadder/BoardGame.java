import java.util.Deque;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Queue;
import java.util.List;

public class BoardGame {
    private int boardSize;
    private List<Jumper> ladders;
    private List<Jumper> snakes;
    private Deque<Player> players;
    private HashMap<Player, Integer> playersPos;

    BoardGame(int boardSize, List<Jumper> ladders , List<Jumper> snakes, Deque<Player> players) {
        this.boardSize= boardSize;
        this.ladders = ladders;
        this.snakes = snakes;
        this.players = players;
        this.playersPos = new HashMap<>();
        initializePos();
        
    }

    private void initializePos() {
        for (Player player: this.players) {
            this.playersPos.put(player, 0);
        }
    }
    
    public Integer finalMove(Integer currentMove) {
        for (Jumper jumper: this.ladders) {
            if (jumper.startPosition==currentMove) {
                System.out.println("ladder help "+ currentMove + " to " + (currentMove+jumper.endPosition));
                return currentMove+jumper.endPosition;
            }
        }
        for (Jumper jumper: this.snakes) {
            if (jumper.startPosition==currentMove) {
                System.out.println("snake bite "+ currentMove + " to " + (currentMove + jumper.endPosition));
                return currentMove+jumper.endPosition;
            }
        }
        System.out.println("normal move  "+ currentMove);
        return currentMove;
    }
    
    public static int rollDice() {
        return (int) (Math.random()*6+1);
    }

    public void gameStart() {

        while (true) {
            Player currPlayer = this.players.pollFirst();
            System.out.println("current player: "+ currPlayer.name);
            int rolledValue = rollDice();
            Integer finalPos = finalMove(rolledValue+this.playersPos.get(currPlayer));

            if (finalPos>this.boardSize) {
                this.players.addLast(currPlayer);
                continue;
            } else if (finalPos==this.boardSize) {
                System.out.println("->>---> winner: "+ currPlayer.name);
                break;
            } else {
                this.playersPos.put(currPlayer, finalPos);
                this.players.addLast(currPlayer);
            }
        }
    }

}