import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    public static void main(String[] args) {
        String matching = "Match";

        Scanner scanner = new Scanner(System.in);

        String boy = scanner.next();
        char[] boyArray = boy.toCharArray();

        String girl = scanner.next();
        char[] girlArray = girl.toCharArray();

        Map<Character, Integer> boyLetterAndCount = getLetterCount(boyArray);
        Map<Character, Integer> girlLetterAndCount = getLetterCount(girlArray);

        ArrayList<Character> boyFirstLetters = new ArrayList<>();
        List<Character> boyLetters = sortMap(boyLetterAndCount);
        if (boyLetters.size() >= 1) boyFirstLetters.add(boyLetters.get(0));
        if (boyLetters.size() >= 2) boyFirstLetters.add(boyLetters.get(1));
        if (boyLetters.size() >= 3) boyFirstLetters.add(boyLetters.get(2));

        ArrayList<Character> girlFirstLetters = new ArrayList<>();
        List<Character> girlLetters = sortMap(girlLetterAndCount);
        if (girlLetters.size() >= 1) girlFirstLetters.add(girlLetters.get(0));
        if (girlLetters.size() >= 2) girlFirstLetters.add(girlLetters.get(1));
        if (girlLetters.size() >= 3) girlFirstLetters.add(girlLetters.get(2));

        if (boyFirstLetters.size() != girlFirstLetters.size()) matching = "Not a Match";
        else {
            for (char letter : boyFirstLetters) {
                if (!girlFirstLetters.contains(letter)) {
                    matching = "Not a Match";
                    break;
                }
            }
        }
        for (char letter : boyFirstLetters) {
            System.out.print(letter);
        }
        System.out.println();
        for (char letter : girlFirstLetters) {
            System.out.print(letter);
        }
        System.out.println("\n" + matching);
    }
    
     static Map<Character, Integer> getLetterCount(char[] array) {
        Map<Character, Integer> letterCount = new HashMap<>();

        for (char letter : array) {
            if (letterCount.containsKey(letter)) {
                int count = letterCount.get(letter);
                letterCount.put(letter, count + 1);
            } else {
                letterCount.put(letter, 1);
            }
        }
        return letterCount;
    }

    static List<Character> sortMap(Map<Character, Integer> map) {
        List<Map.Entry<Character, Integer>> list = new LinkedList<>(map.entrySet());

        Set<Integer> valueSet = map.entrySet().stream().map(Map.Entry::getValue).sorted().collect(Collectors.toCollection(LinkedHashSet::new));
        List<Integer> valueList = new ArrayList<>(valueSet);
        List<Character> result = new ArrayList<>();

        for (int i = valueList.size() - 1; i >= 0; i--) {
            List<Character> letters = new ArrayList<>();
            for (Map.Entry<Character, Integer> entry : list) {
                if (entry.getValue().equals(valueList.get(i))) {
                    letters.add(entry.getKey());
                }
            }
            Collections.sort(letters);
            result.addAll(letters);
        }
        return result;
    }
}