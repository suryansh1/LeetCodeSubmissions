class Solution {
public:
    bool isdigit(char c){
        return c>='0' && c<='9';
    }
    bool isalpha(char c){
        return (c>='a'&&c<='z') || (c>='A' && c<='Z');
    }
    bool isPalindrome(string s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if(s.size()==0)  return true;
        int len = s.size();
        for(int i = 0,j=len-1;i<=j;i++,j--){
            while(i<=j &&!isalpha(s[i]) && !isdigit(s[i])) i++;
            while(i<=j &&!isalpha(s[j]) && !isdigit(s[j])) j--;
            if(i<=j&&!s[i]==s[j]) return false;
        }
        return true;
    }
};