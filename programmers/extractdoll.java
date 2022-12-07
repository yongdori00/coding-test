public class extractdoll {
    static public int solution(int[][] board, int[] moves) {
        int []itemloc = new int[board[0].length];
        int answer = 0;
        int k = 0;
        int boardlength = board.length;
        int loc = 0;

        Stack <Integer>answerStack = new Stack<Integer>();

        for(int i = 0; i < board[0].length; i++){
            k = 0;
            while(board[k][i] == 0){
                k++;
            }
            itemloc[i] = k;
        }


        for(int i = 0; i < moves.length; i++){
            loc = moves[i] - 1;
            if(boardlength == itemloc[loc])
                continue;
            if(answerStack.isEmpty() || answerStack.peek() != board[itemloc[loc]][loc]){
                answerStack.push(board[itemloc[loc]][loc]);
                itemloc[loc]++;
            }
            else{
                answerStack.pop();
                answer+=2;
                itemloc[loc]++;
            }
        }
        return answer;
}
