// 1768. Merge Strings Alternately

//You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
//If a string is longer than the other, append the additional letters onto the end of the merged string.

//Return the merged string.

class Solution {
    public String mergeAlternately(String word1, String word2) {
        int len1 = word1.length();
        int len2= word2.length();
        int len;
        boolean word1Longer;
        if(len1>len2) {
            len = len2;
            word1Longer = true;
        }
        else {
            len = len1;
            word1Longer = false;
        }
        char[] array1 = word1.toCharArray();
        char[] array2 = word2.toCharArray();
        char[] jointArray = new char[len1+len2];
        int j=0;
        for(int i=0;i<len;i++) {
            jointArray[j] = array1[i];
            j++;
            jointArray[j] = array2[i];
            j++;
        }
        if(word1Longer) {
            for(int i=len2;i<len1;i++) {
                jointArray[j] = array1[i];
                j++;
            }
        }
        else {
            for(int i=len1;i<len2;i++) {
                jointArray[j] = array2[i];
                j++;
            }
        }
        return new String(jointArray);
        
    }
}
