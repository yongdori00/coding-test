import java.util.ArrayList;
import java.util.Collections;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class newscluteringS {
    public static int solution(String str1, String str2) {
        int answer = 0;
        float same = 0;
        float different = 0;
        int str1index = 0, str2index = 0;
        int remainder = 0;

        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        ArrayList<String> str1set = new <String>ArrayList();
        ArrayList<String> str2set = new <String>ArrayList();

        for (int i = 0; i < str1.length() - 1; i++)
            str1set.add(str1.substring(i, i + 2));

        for (int i = 0; i < str2.length() - 1; i++)
            str2set.add(str2.substring(i, i + 2));

        String pattern = "[^a-z]";
        Pattern p = Pattern.compile(pattern);
        Matcher match;

        for (int i = 0; i < str1set.size(); i++) {
            match = p.matcher(str1set.get(i));
            if (match.find()) {
                str1set.remove(i);
                i--;
            }
        }
        for (int i = 0; i < str2set.size(); i++) {
            match = p.matcher(str2set.get(i));
            if (match.find()) {
                str2set.remove(i);
                i--;
            }
        }

        Collections.sort(str1set);
        Collections.sort(str2set);

        while (str1index < str1set.size() && str2index < str2set.size()) {
            if (str1set.get(str1index).equals(str2set.get(str2index))) {
                same++;
                different++;
                str1index++;
                str2index++;
            } else if (str1set.get(str1index).compareTo(str2set.get(str2index)) > 0) {
                different++;
                str2index++;
            } else if (str2set.get(str2index).compareTo(str1set.get(str1index)) > 0) {
                different++;
                str1index++;
            }
        }
        while(str1index < str1set.size()){
            different++;
            str1index++;
        }
        while(str2index < str2set.size()){
            different++;
            str2index++;
        }

        if(str2set.size() == 0 && str1set.size() == 0){
            same = 1;
            different = 1;
        }
        
        answer = (int) (65536 * same / different);
        return answer;
    }

    public static void main(String argv[]) {
        System.out.println(solution("E=M*C^2", "e=m*c^2"));
    }
}