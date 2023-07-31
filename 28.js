// 28. Find the Index of the First Occurrence in a String

// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
// or -1 if needle is not part of haystack.
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let j = 0;
    let index = 0;
    let next = 0;
    let foundNext = false;
  for (let i = 0; i < haystack.length; i++) {
      if (haystack.charAt(i) === needle.charAt(j)) {
          if(j === 0) {
              index = i;
          }
          if(haystack.charAt(i) === haystack.charAt(index) && !foundNext) {
              foundNext = true;
              next = i;
          }
          j++;
          if (j === needle.length) {
              return index;
          }
      }
      else {
          j = 0;
          if(foundNext) {
              i = next;
              foundNext = false;
          }
      }
  }
  return -1;    
};
