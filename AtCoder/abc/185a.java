import java.util.*;

class Main {
    static public void main(String[] args) {
        Scanner io = new Scanner(System.in);

        int ans = io.nextInt();
        ans = Math.min(ans, io.nextInt());
        ans = Math.min(ans, io.nextInt());
        ans = Math.min(ans, io.nextInt());

        System.out.println(ans);
    }
}