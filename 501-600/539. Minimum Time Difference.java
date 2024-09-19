import java.lang.Math;

class Solution {
    public int findMinDifference(List<String> timePoints) {
        int differ = 0;
        int size = timePoints.size();
        int[] totals = new int[size];
        for (int i = 0; i < size; i++) {
            Integer hourA = Integer.valueOf(timePoints.get(i).substring(0,2));
            Integer minA = Integer.valueOf(timePoints.get(i).substring(3));
            if (hourA == 0) hourA = 24;
            int totalA = hourA * 60 + minA;
            totals[i] = totalA;
        }

        Arrays.sort(totals);

        for (int i = 0; i < size - 1; i++) {
            if (i == 0) {
                int min = Math.abs(totals[size - 1] - totals[0]);
                differ = Math.min(min, Math.abs(1440 - min));          
            }
            int min = Math.abs(totals[i] - totals[i+1]);
            min = Math.min(min, Math.abs(1440 - min));
            if (min < differ) differ = min;
        }
        return differ;
    }
}