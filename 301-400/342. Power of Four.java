class Solution {
    public boolean isPowerOfFour(int n) {
        if (n == 1)
            return true;
        else if (n == 0 || n % 2 != 0 || n % 4 != 0)
            return false;
        else
            return isPowerOfFour(n / 4);
    }
}