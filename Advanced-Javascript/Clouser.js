// Example of clouser

/*

Real-World Scenario: In a React app, you might use closures to manage internal 
state in custom hooks. For example:
*/

function useCounter(intialValue = 0) {
  let counter = intialValue; // private constructor

  const increment = () => counter++;

  const getCounter = () => counter;

  return {
    increment,
    getCounter,
  };
}


const count = useCounter(5);
console.log(count.getCounter()); // Output: 5
count.increment();
console.log(count.getCounter()); // Output: 6







// Example 02 

/*

In React or frontend development, closures are useful in event handlers or custom hooks. For instance, 
a button click handler might "remember" which specific button it’s handling.

*/


function createButtonHandler(buttonId) {

    

    return function() {
        console.log(`Button ${buttonId} clicked`);
    };
}

// Attach handlers to buttons dynamically
const handleButton1 = createButtonHandler(1);
const handleButton2 = createButtonHandler(2);

handleButton1(); // Output: Button 1 clicked
handleButton2(); // Output: Button 2 clicked