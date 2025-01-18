# Here Topic List Thats Should be Covered By JS 



```
 - 1  Clouser 

  A closure gives a function access to its outer scope. In JavaScript, closures are created every time a function is created, at function creation time.


  --------
A closure allows a function to access variables from its outer (enclosing) function even after that function has finished executing

---------------





function makeFunc() {
  const name = "Mozilla";
  function displayName() {
    console.log(name);
  }
  return displayName;
}

const myFunc = makeFunc();
myFunc();







```