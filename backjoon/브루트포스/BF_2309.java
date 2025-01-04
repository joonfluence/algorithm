package 브루트포스.일곱난쟁이;

/*

구성 요소 갯수의 합이 7, 총 합쳤을 때 값이 100일 때

 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

/*

1. 중첩 for-loop 돌면서, 2개의 값을 제하고 계산해본다.

 */
public class BF_2309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<Integer>();
        int size = 9;

        for (int i = 0; i < size; i++) {
            nums.add(sc.nextInt());
        }

        int sizeSum = nums.stream().mapToInt(a -> a).sum();
        int aIdx = 0;
        int bIdx = 0;

        for (int i = 0; i < size-1; i++) {
            for (int j = i+1; j < size; j++) {
                int value = sizeSum - (nums.get(i) + nums.get(j));
                if (value == 100){
                    aIdx = nums.get(i);
                    bIdx = nums.get(j);
                }
            }
        }

        int finalAIdx = aIdx;
        nums.removeIf(n -> n.equals(finalAIdx));
        int finalBIdx = bIdx;
        nums.removeIf(n -> n.equals(finalBIdx));
        Collections.sort(nums);
        nums.forEach(System.out::println);
    }
}
