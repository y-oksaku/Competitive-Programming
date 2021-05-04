import java.util.*;

class Main {
    static public void main(String[] args) {
        Scanner io = new Scanner(System.in);

        int N = io.nextInt();
        int M = io.nextInt();

        if (M == 0) {
            System.out.println(1);
            return;
        }

        List<Integer> A = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            int a = io.nextInt();
            A.add(a);
        }
        A.add(N + 1);

        A.sort(Integer::compare);

        List<Integer> width = new ArrayList<>();
        int now = 0;
        for (int a: A) {
            int w = a - now - 1;
            if (w > 0) width.add(w);
            now = a;
        }

        if (width.size() == 0) {
            System.out.println(0);
            return;
        }

        int k = width.stream().min(Integer::compare).get();
        int ans = 0;
        for (int w: width) {
            ans += (w + k - 1) / k;
        }

        System.out.println(ans);
    }
}