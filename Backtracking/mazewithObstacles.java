public class mazewithObstacles {
    public static void main(String[] args) {
        boolean[][] board={
            {true,true,true},
            {true,false,true},
            {true,true,true}
        };
          pathfinder("", board, 0, 0);
    }
    static void pathfinder(String p,boolean[][] maze,int r,int c){
        if (r==maze.length-1 && c==maze[0].length-1) {
            System.out.println(p);
            return;
        }
        if (maze[r][c]==false) {
            return;
        }
        if (r<maze.length-1) {
            pathfinder(p+"Down->",maze, r+1, c);
        }
        if (c<maze[0].length-1) {
            pathfinder(p+"Right->",maze,r, c+1);
        }
    }
}