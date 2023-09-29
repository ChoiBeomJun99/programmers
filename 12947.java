class Solution {
    public boolean solution(int x) {
        String[] tmp = Integer.toString(x).split("");
        
        int hap = 0;
        
        for (String s: tmp) {
            hap += Integer.parseInt(s);
        }
        
        return x % hap == 0;
    }
}