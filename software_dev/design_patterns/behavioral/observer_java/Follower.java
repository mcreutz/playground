public class Follower implements Observer {
    private String followerName;

    public void Follower(String followerName) {
        this.followerName = followerName;
    }

    public void update(String status) {
        // do something
    }

    public void play() {
        // play something
    }
}
