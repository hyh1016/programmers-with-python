class Solution {
    
    private int BOARD_LENGTH = 3;
    private String[] board;    

    public int solution(String[] board) {
        this.board = board;
        int oCount = count('O');
        int xCount = count('X');
        int diff = oCount - xCount;
        if (diff > 1 || diff < 0) return 0;
        
        boolean oWin = complete('O');
        boolean xWin = complete('X');
        if (oWin && xWin) return 0;
        if (xWin && oCount > xCount) return 0;
        if (oWin && oCount == xCount) return 0;
        
        return 1;
    }
    
    private int count(char player) {
        int count = 0;
        for (int i=0; i<BOARD_LENGTH; i++) {
            for (int j=0; j<BOARD_LENGTH; j++) {
                if (board[i].charAt(j) == player) count++;
            }
        }
        return count;
    }
    
    private boolean complete(char player) {
        for (int i=0; i<BOARD_LENGTH; i++) {
            int c1 = 0;
            int c2 = 0;
            for (int j=0; j<BOARD_LENGTH; j++) {
                if (board[i].charAt(j) == player) c1++;
                if (board[j].charAt(i) == player) c2++;
            }
            if (c1 == BOARD_LENGTH || c2 == BOARD_LENGTH) return true;
        }
        int c3 = 0;
        int c4 = 0;
        for (int i=0; i<BOARD_LENGTH; i++) {
            if (board[i].charAt(i) == player) c3++;
            if (board[i].charAt(2-i) == player) c4++;
        }
        if (c3 == BOARD_LENGTH || c4 == BOARD_LENGTH) return true;
        
        return false;
    }
}
