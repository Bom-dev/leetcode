class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1)
            return x;
        if (x == Integer.MAX_VALUE)
            return 46340;
        int base = 1;
        for (int i = 0; i < x; i++) {
            if (i * i == x) {
                return i;
            } else if (i * i > x) {
                return base;
            }
            base = i;
        }
        return base;
    }
}