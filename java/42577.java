// 이중 포문 이용 -> 시간초과 ㅜㅜ
// import java.util.*;

// class Solution {
//     public boolean solution(String[] phone_book) {
//         boolean answer = true;
//         Arrays.sort(phone_book);
        
//         for (String tmp : phone_book) {
            
//             for (int i = 0; i < phone_book.length; i++) {
//                 String compare = phone_book[i];
                
//                 // 길이가 길면 접두어로 존재 할 수 없음 or 자기 자신과는 비교 x
//                 if (tmp.length() > compare.length() || tmp.equals(compare)) { 
//                     continue;
//                 }
                
//                 // 접두어가 된다면 false를 바로 return.
//                 if (tmp.equals(compare.substring(0, tmp.length()))) {
//                     return false;
//                 }
                
//             }
            
//         }
        
//         return answer;
//     }
// }



import java.util.*;

class Solution {
    public boolean solution(String[] phoneBook) {
        Map <String, Integer> map = new HashMap<>();
        
        int value = 0;
        for (String tmp : phoneBook) {
            map.put(tmp, value);
            value++;
        }
        
        for (String tmp : phoneBook) {
            
            for (int i = 0; i < tmp.length(); i++) {
                if(map.containsKey(tmp.substring(0, i))) {
                    return false;
                }
            }
            
        }
        return true;
    }
}