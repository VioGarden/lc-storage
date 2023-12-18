const arr = [5,7,2,8]

for(let i in arr){
    console.log(i)
    //0,1,2,3
    //loops over keys
}

for(let i of arr){
    console.log(i)
    //5,7,2,8
    //loops over values
}