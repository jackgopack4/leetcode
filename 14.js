// 14. Longest Common Prefix

// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  let shortest = 200;
  let ret = "";
  for(let i = 0; i<strs.length; i++) {
    if(strs[i].length < shortest) { shortest = strs[i].length; }
  }
  for(let i = 0; i<shortest; i++) {
      let current = strs[0].charAt(i);
      for(let j = 0; j<strs.length; j++) {
          if(strs[j].charAt(i)!==current) {
              return ret;
          }
      }
      ret+=current;
  }
  return ret;
};
