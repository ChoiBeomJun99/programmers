class Solution {
    public String solution(String[] seoul) {
        int tmp = 0;
        
        for (int i = 0; i < seoul.length; i++) {
            if(seoul[i].equals("Kim")) {
                tmp = i;
                break;
            }
            
        }
        
        return "김서방은 " + Integer.toString(tmp) + "에 있다";
    }
}