package 브루트포스.수이어쓰기;

import java.util.Scanner;

/*

1)

Scanner sc = new Scanner(System.in);
int N = sc.nextInt();
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= N; i++) {
    sb.append(Integer.toString(i));
}
System.out.println(sb.toString().length());

2)

int[] dp = new int[N+1];
dp[0] = 0;

for (int i = 1; i <= N; i++) {
    int length = Integer.toString(i).length();
    dp[i] = dp[i - 1] + length;
}
System.out.println(dp[N]);

 */

public class BF_1748 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int totalCount = 0;
        int num = 1;
        int criteria = 10;
        for (int i = 1; i <= N; i++) {
            if (i % criteria == 0){
                num += 1;
                criteria *= 10;
            }
            totalCount += num;
        }
        System.out.println(totalCount);
    }
}
