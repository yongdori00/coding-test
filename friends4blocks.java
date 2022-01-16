import java.util.ArrayList;

public class friends4blocks {
    public static int solution(int m, int n, String[] board) {
        int answer = 0;
        
        ArrayList []Alist = new ArrayList[n];
        for(int i = 0; i < n;i++){
            Alist[i] = new ArrayList<Integer>();
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                Alist[j].add(board[m-i-1].charAt(j));
            }
        }for(int i = 0; i < Alist.length - 1; i++){
            for(int j = 0; j < Alist[i].size() - 1; j++){
                if(Alist[i].get(j) == Alist[i].get(j + 1))
                    if(Alist[i].get(j) == Alist[i + 1].get(j) && Alist[i].get(j) == Alist[i + 1].get(j + 1)){
                        Alist[i].remove(j+1);
                        Alist[i].remove(j);
                        Alist[i+1].remove(j+1);
                        Alist[i+1].remove(j+1);
                        j--;
                        answer++;
                    }
                Alist[j].add(board[m-i-1].charAt(j));
            }
        }
        return answer;
        //전부 새로 해야할 듯
    }

    public static void main(String []s){
        String [] board = {"CCBDE", "AAADE", "AAABF", "CCBBF"};
        solution(4,5,board);
    }
}
