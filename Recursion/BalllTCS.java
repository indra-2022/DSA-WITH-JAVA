public class BalllTCS {
    public static void main(String[] args) {
        System.out.println(countWays(1,1,1,' '));
    }
    static int countWays(int g, int y, int r, char prev) {

    // check if no balls are there
    if (g == 0 && y == 0 && r == 0) {
        return 1;
    }

    int count = 0;

    // Place Green
    if (g > 0 && prev != 'G') {
        count += countWays(g - 1, y, r, 'G');
    }

    // Place Yellow
    if (y > 0 && prev != 'Y') {
        count += countWays(g, y - 1, r, 'Y');
    }

    // Place Red
    if (r > 0 && prev != 'R') {
        count += countWays(g, y, r - 1, 'R');
    }

    return count;
}

}
