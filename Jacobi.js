const Ab = [
  
  [-1,1,7,-6],
  [4,-1,-1,3],
  [-2,6,1,9]
];




let A = [];
let b = [];
let epsilon = 0.0005;
let err = [];
let X_0 = [];
let X_k = [];
let X_kPlusOne = [];
let k = 1;

for(let i = 0 ;i<Ab.length;i++){
  for(let j = 0;j<Ab[i].length-1;j++){
        if(Ab[i][i]<Ab[i][j]){
          let temp = Ab[i]
          Ab[i] = Ab[j]
          Ab[j] = temp
        }
      
  }
}

for (let i = 0; i < Ab.length; i++) {
  A.push([]);
  for (let j = 0; j < Ab[i].length - 1; j++) {
    A[i].push(Ab[i][j]);
  }
}

for (let i = 0; i < Ab.length; i++) {
  b.push(Ab[i][Ab[i].length - 1]);
}
for (let i = 0; i < A.length; i++) {
  X_0.push(0);
}


for (let i = 0; i < A.length; i++) {
  X_k.push(X_0[i]);
}

while (true) {
  let sum;
  err = [];
  for (let i = 0; i < A.length; i++) {
    sum = 0;
    for (let j = 0; j < A[i].length; j++) {
      if (i !== j) {
        sum += A[i][j] * X_k[j];
      }
    }

    X_kPlusOne.push((b[i] - sum) / A[i][i]);
  }
  for (let i = 0; i < X_k.length; i++) {
    err.push(X_kPlusOne[i] - X_k[i]);
  }
  for (let i = 0; i < X_k.length; i++) {
    X_k[i] = X_kPlusOne[i];
  }
  for (let i = 0; i < X_k.length; i++) {
    X_kPlusOne.pop();
  }

  console.log(`Step ${k} :\n`);
  for (let i = 0; i < X_k.length; i++) {
    console.log(`X_${i+1} = ${X_k[i]} ,`);
  }
  console.log("=========================\n");
  k++;
  if (Math.abs(Math.max(...err)) < epsilon) {
    break;
  }
  
  
}
