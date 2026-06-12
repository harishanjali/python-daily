//reverse string

let x,res,length;
x = 'harish'
lengths = x.length-1
res = ''
for(let i=0;i<lengths;i++){
    res += x[lengths-i]
}
console.log('reverse string',res)
    
//factorial of number
let n,fact;
n=5
fact=1
for(let i=1;i<=n;i++){
    fact*=i
}
console.log('factorial',fact)

//duplicates from list
let lst,out;
lst = [1,2,2,3,4,4]
out=[]
for(let item of lst){
    if(out.includes(item)===false){
        out.push(item)
    }
}
console.log('remove duplicates',out)

let setA,setB;
setA = new Set('silenth'.split(''))
setB = new Set('listen'.split(''))
// myset = new Set([1,2,3,3,3])
res = setA.symmetricDifference(setB)
console.log(res.size == 0?'anagram':'not anagram')

//merge two arrays without duplicates
setA = new Set([1,2,3])
setB = new Set([2,3,4])
res = setA.union(setB)
console.log(Array(res))