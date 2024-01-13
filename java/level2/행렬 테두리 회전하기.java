class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] matrix = new int[rows][columns];
        for (int i=0; i<rows; i++) {
            for (int j=0; j<columns; j++) {
                matrix[i][j] = i * columns + j + 1;
            }
        }
        for (int i=0; i<queries.length; i++) {
            int[] query = queries[i];
            answer[i] = rotateAndGetMin(matrix, query);
        }
        return answer;
    }
    
    private int rotateAndGetMin(int[][] matrix, int[] query) {
        int sr = query[0]-1, sc = query[1]-1, er = query[2]-1, ec = query[3]-1;
        int min = matrix[sr][sc];
        int current = matrix[sr][sc];
        for (int c=sc; c<ec; c++) {
            int next = matrix[sr][c+1];
            min = Math.min(min, next);
            matrix[sr][c+1] = current;
            current = next;
        }
        for (int r=sr; r<er; r++) {
            int next = matrix[r+1][ec];
            min = Math.min(min, next);
            matrix[r+1][ec] = current;
            current = next;
        }
        for (int c=ec; c>sc; c--) {
            int next = matrix[er][c-1];
            min = Math.min(min, next);
            matrix[er][c-1] = current;
            current = next;
        }
        for (int r=er; r>sr; r--) {
            int next = matrix[r-1][sc];
            min = Math.min(min, next);
            matrix[r-1][sc] = current;
            current = next;
        }
        return min;
    }
}