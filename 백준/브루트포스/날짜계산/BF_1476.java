package 브루트포스.날짜계산;
import java.io.*;
import java.util.*;

/*

- 수 3개를 이용해서 연도를 나타낸다. 각각의 수는 지구, 태양, 그리고 달을 나타낸다.
    - 지구를 나타내는 수를 E, 태양을 나타내는 수를 S, 달을 나타내는 수를 M이라고 했을 때, 이 세 수는 서로 다른 범위를 가진다. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

 */
public class BF_1476 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int e = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int E = 0;
        int S = 0;
        int M = 0;
        int year = 0;
        while (true) {
            year++;
            E++;
            S++;
            M++;
            if (E==16) E=1;
            if (S==29) S=1;
            if (M==20) M=1;
            if (e == E && m == M && S == s) break;
        }
        System.out.print(year);
    }
}
