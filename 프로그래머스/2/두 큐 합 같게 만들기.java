import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        
        //큐 생성
        Queue<Integer> queu1 = new LinkedList();
        Queue<Integer> queu2 = new LinkedList();
        
        //두 큐의 길이가 같기 때문
        int len1 = queue1.length;
        int length = len1 *2;
        
        for(int i = 0; i < len1; i++){
            queu1.add(queue1[i]);
            queu2.add(queue2[i]);
        }
        
        //총 합
        long sum1 = queu1.stream().mapToInt(Integer::intValue).sum();
        long sum2 = queu2.stream().mapToInt(Integer::intValue).sum();
        
        //두 큐가 모두 1회전씩 하면 끝난 경우임.
        while(length >= 0){
            int temp = 0;
            while(sum1 < sum2){
                temp = queu2.poll();
                queu1.add(temp);
                sum1+=temp;
                sum2-=temp;
                length--;
            }
            while(sum1 > sum2){
                temp = queu1.poll();
                queu2.add(temp);
                sum2+=temp;
                sum1-=temp;
                length--;
            }
            if (sum1 == sum2){
                break;
            }
            
        }
        
        if(length <= 0 && sum1!=sum2)
            answer = -1;
        else
            answer = len1 * 2 - length;
        
        return answer;
    }
}