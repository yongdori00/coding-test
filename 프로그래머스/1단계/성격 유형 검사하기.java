//Arrays 때문
import java.util.*;

class Solution {
    public static<T> T[] subArray(T[] array, int start, int end){
        return Arrays.copyOfRange(array, start, end+1);
    }
    
    public String solution(String[] survey, int[] choices) {
        String[] mbti = {"RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"};
        int[] score = {0,0,0,0};
        
        //점수를 -3~+3으로 변경
        int[] choice = Arrays.stream(choices)
            .map(s -> s - 4)
            .toArray();
        
        //각각 T가+, R이-, F가+, C가-를 생각으로 RT를 +, TR이 - 이런식으로 작업함.
        for(int i = 0; i < survey.length; i++){
            if(Arrays.asList(subArray(mbti, 0, 1)).contains(survey[i])){
                if(mbti[0].equals(survey[i]))
                    score[0]+=choice[i];
                else
                    score[0]-=choice[i];
            }
            else if(Arrays.asList(subArray(mbti, 2, 3)).contains(survey[i])){
                if(mbti[2].equals(survey[i]))
                    score[1]+=choice[i];
                else
                    score[1]-=choice[i];
            }
            else if(Arrays.asList(subArray(mbti, 4, 5)).contains(survey[i])){
                if(mbti[4].equals(survey[i]))
                    score[2]+=choice[i];
                else
                    score[2]-=choice[i];
            }
            else if(Arrays.asList(subArray(mbti, 6, 7)).contains(survey[i])){
                if(mbti[6].equals(survey[i]))
                    score[3]+=choice[i];
                else
                    score[3]-=choice[i];
            }
        }

        Arrays.stream(score)
        .forEach(System.out::println);
        
        
        String answer = "";
        answer += score[0] > 0 ? "T" : "R";
        answer += score[1] >= 0 ? "C" : "F";
        answer += score[2] >= 0 ? "J" : "M";
        answer += score[3] > 0 ? "N" : "A";
        
        return answer;
    }
}