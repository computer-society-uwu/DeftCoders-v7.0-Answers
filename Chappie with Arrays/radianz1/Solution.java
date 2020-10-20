import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOfTestCases = scanner.nextInt();

        for (int i = 0; i < numberOfTestCases; i++) {

            int numberOfElements = scanner.nextInt();

            ArrayList<Integer> list = new ArrayList<>();

            for (int j = 0; j < numberOfElements; j++) {
                list.add(Integer.valueOf(scanner.next()));
            }

            int numberOfSubstrings = 0;

            ArrayList<Integer> list1 = new ArrayList<>(list);

            for (int h = 0; h < list.size(); h++) {
                for (int k = h + 1; k < list.size(); k++) {
                    if (list1.size() > h || list1.size() > k) {
                        Integer integer = list1.get(h);
                        Integer anotherInteger = list1.get(k);
                        int gcd = gcd(integer, anotherInteger);
                        if (gcd == 1) {
                            numberOfSubstrings++;
                            list1.set(k, 0);
                            list1.set(h, 0);
                        }
                    }
                }
            }
            System.out.println(numberOfSubstrings == 0 ? -1 : numberOfSubstrings);
        }
    }
    
    static int gcd(int a, int b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }
}