// Example of setTimeout , console.log() and Promise ;

// setTimeout()

console.log("Start"); // Execute first

setTimeout(() => {
  console.log("Inside setTimeout");
}, 0); // Execute last  call

// Promise

Promise.resolve().then(() => {
  console.log("Inside Promise / Promise Callback");
}); // Execute third

console.log("End"); // Execute second


// Output: 


// Start
// End

// Inside Promise / Promise Callback

// Inside setTime Out


/**
 * Step-by-Step Explanation:
- Synchronous Code:

- "Start" is logged immediately (console.log("Start")).
- setTimeout is sent to Web APIs, and its callback is queued after 0ms.
- Promise.resolve() adds its .then callback to the microtask queue.
- "End" is logged.

Microtask Queue:

The promise callback ("Promise Callback") is executed next.
Task Queue:

The setTimeout callback ("Timeout Callback") is executed last.

 */