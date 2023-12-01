let accountID = 0;

const login = document.getElementById("loginBtn");
const signUp = document.getElementById("signUpBtn");

login.addEventListener("click", () => {
    const uName = document.getElementById("uName");
    const password = document.getElementById("password");

    if (uName.value === "" || password.value === ""){
        alert("Please enter a username and password");
        return;
    }

    console.log("test");
    fetch(`/account/${uName.value}/${password.value}`)
    .then((res) => res.json())
    .then((data) => {
        const id = data.id;
        if (id === "admin"){
            window.location.href = "/admin";
        }
        else if (id > 0){
            accountID = id;
            localStorage.setItem("accountID", accountID);
            window.location.href = "/homePage";
        }
        else {
            alert("Invalid username or password")
        }
    })
    .catch((err) => console.log(err));
});

signUp.addEventListener("click", () => {
    window.location.href = "/account";
});
