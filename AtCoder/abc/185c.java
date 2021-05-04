import java.util.*;

class Main {
    static public void main(String[] args) {
        Scanner io = new Scanner(System.in);

        int L = io.nextInt() - 1;
        boolean[] isDivided = new boolean[20];

        for (int i = 0; i < 20; i++) isDivided[i] = false;

        long ans = 1;
        for (int i = 0; i < 11; i++) {
            ans *= (L - i);
            for (int j = 1; j <= 11; j++) {
                if (isDivided[j]) continue;
                if (ans % j == 0) {
                    isDivided[j] = true;
                    ans /= j;
                }
            }
        }

        System.out.println(ans);
    }
}