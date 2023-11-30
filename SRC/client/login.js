// document.getElementById('deleteButton').addEventListener('click', function() {
//     var table = document.getElementById('excel-like-table');
//     var checkboxes = table.querySelectorAll('input[type="checkbox"]');
//     checkboxes.forEach(function(checkbox) {
//         if (checkbox.checked) {
//             var row = checkbox.parentElement.parentElement;
//             row.parentNode.removeChild(row);
//         }
//     });
// });

// let counter = 0;

// function increment() {
//   counter++;
// }

// function decrement() {
//   counter--;
// }

// function get() {
//   return counter;
// }

// const inc = document.getElementById("increment");
// const input = document.getElementById("input");
// const dec = document.getElementById("decrement");

// inc.addEventListener("click", () => {
//   increment();
//   input.value = get();
// });

// dec.addEventListener("click", () => {
//   if (input.value > 0) {
//     decrement();
//   }
//   input.value = get();
// });

const login = document.getElementById("loginBtn");

login.addEventListener("click", () => {
    const uName = document.getElementById("uName");
    const password = document.getElementById("password");

    const data = {
        username: uName.value,
        password: password.value,
    };

    // $.ajax({ 
    //     url: '/testing/data', 
    //     type: 'POST', 
    //     contentType: 'application/json', 
    //     data: JSON.stringify(data),
    //     success: function(response) { 
    //         alert(response); 
    //     }, 
    //     error: function(error) { 
    //         console.log(error); 
    //     } 
    // }); 

    console.log("test");
    fetch(`/testing/data`)
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
    })
    .catch((err) => console.log(err));
});