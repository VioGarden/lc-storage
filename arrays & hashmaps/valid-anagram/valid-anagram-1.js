var isAnagram = function(s, t) {
    if(s.length !== t.length){
        return false
    }
    let countS = {}
    let countT = {}

    for(let i = 0;i < s.length; i++){
        if(countS.hasOwnProperty(s[i])){
            countS[s[i]]++
        } else {
            countS[s[i]] = 1;
        }
        if(countT.hasOwnProperty(s[i])){
            countT[s[i]]++
        } else {
            countT[s[i]] = 1;
        }
    }
    for(let j in countS){
        if(countS[j] !== countT[j]){
            return false;
        }
    } 
    return true;
};