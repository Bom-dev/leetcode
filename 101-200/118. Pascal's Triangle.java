class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList<>();
        if (numRows >= 1) {
            for (int i = 0; i < numRows; i++) {
                List<Integer> col = new ArrayList<Integer>();
                for (int j = 0; j <= i; j++) {
                    int num = 1;
                    if (i > 1 && j >= 1 && i < numRows && j < i) {
                        num = list.get(i - 1).get(j) + list.get(i - 1).get(j - 1);
                    }
                    col.add(num);
                }
                list.add(col);
            }
        }
        return list;
    }
}