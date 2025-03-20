`
Write a function that takes a string as input and returns the 
length of the longest substring that contains no repeated characters.

input-"aabccd"

`

function longestSubString(intstr) {
    var l = 0
    var r = 0
    var visitedSet = new Set()
    var maxL= 0

    for (i=0; i<intstr.length;i+=1) {

        while (visitedSet.has(intstr[i])) {
            visitedSet.delete(intstr[l])
            l+=1

        }
        visitedSet.add(intstr[i])
        maxL = Math.max(maxL, r-l+1)
        r+=1

    }
    return maxL
}


answer = longestSubString("aabccdwxyz")
// answer = longestSubString("abcdefgthykukcd")
console.log(answer)