import java.util.*;

public class 성격유형검사 {
    public String solution(String[] survey, int[] choices) {
        Integer[] choice = Arrays.stream(choices)
            .map(s -> s - 3)
            .toArray(Integer[]::new);
        
        Arrays.stream(choices)
            .forEach(System.out::println);
        
        String answer = "";
        return answer;
    }
}
