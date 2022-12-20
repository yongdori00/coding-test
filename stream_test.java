import java.util.*;

public class stream_test{

    public static void main(String[] args) {
        String[] array = {"12312311", "2", "3"};

        Arrays.stream(array)
            .distinct()
            .filter((str) -> str.length() >= 5)
            .sorted(Comparator.reverseOrder())
            .forEach(System.out::println);
    }
}