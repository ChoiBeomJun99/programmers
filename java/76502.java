import java.util.*;

class Solution {
    public int solution(String s) {        
        int answer = 0;
        
        // Stack 사용        
        // 돌려가며 stack 확인하기
        for (int j = 0; j < s.length(); j++) {
            
            Stack<String> stack = new Stack<>();
            Boolean flag = true;    
            
            String str = s.substring(j, s.length()) + s.substring(0, j);
            
            for (int i = 0; i < s.length(); i++) {
                char tmp = str.charAt(i);
                        
                if (tmp == '[' || tmp == '(' || tmp == '{') {
                    stack.push(Character.toString(tmp));
                } else {
                    
                    // 괄호를 닫는 기호들이 나왔을때
                    if (stack.isEmpty()) {
                        flag = false;
                        break;
                    }

                    if (tmp == ']') {
                        if (stack.peek().equals("[")) {
                            stack.pop();
                        } else {
                            flag = false;
                            break;
                        }

                    } else if (tmp == '}') {
                        if (stack.peek().equals("{")) {
                            stack.pop();
                        } else {
                            flag = false;
                            break;
                        }
                    } else if (tmp == ')') {
                        if (stack.peek().equals("(")) {
                            stack.pop();   
                        } else {
                            flag = false;
                            break;
                        }
                    }
                }
            }
            
            if (flag && stack.isEmpty()) {
                answer ++;
            }
            
        }
        
        return answer;
    }
}