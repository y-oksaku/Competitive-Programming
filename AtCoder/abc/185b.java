import java.util.*;

class Main {
    static public void main(String[] args) {
        Scanner io = new Scanner(System.in);

        int N = io.nextInt();
        int M = io.nextInt();
        int T = io.nextInt();
        int now = N;
        int t = 0;
        String ans = "Yes";

        for (int i = 0; i < M; i++) {
            int A = io.nextInt();
            int B = io.nextInt();

            now -= A - t;
            if (now <= 0) ans = "No";

            now = Math.min(N, now + B - A);
            t = B;
        }

        now -= T - t;
        if (now <= 0) ans = "No";

        System.out.println(ans);
    }
}