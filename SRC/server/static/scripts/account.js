let accountID = localStorage.getItem("accountID");
let signUp = localStorage.getItem("signUp");

document.addEventListener('DOMContentLoaded', loadData)

document.getElementById("saveBtn").addEventListener('click', () => {
    console.log("test");
    const password = document.getElementById("password");
    const email = document.getElementById("email");
    const phone = document.getElementById("phoneNumber");
    const cardNumber = document.getElementById("cardNumber");
    const cardExpiration = document.getElementById("cardExpiry");
    const cvv = document.getElementById("cvv");

    if (password.value === "" || email.value === "" || phone.value === "" || cardNumber.value === "" || cardExpiration.value === "" || cvv.value === ""){
        alert("Please fill out all fields");
        return;
    }
    if (phone.value.length !== 10){
        alert("Please enter a valid phone number");
        return;
    }
    if (cardNumber.value.length !== 16){
        alert("Please enter a valid card number");
        return;
    }
    if (cvv.value.length !== 3){
        alert("Please enter a valid cvv");
        return;
    }
    if (cardExpiration.value.length !== 6){
        alert("Please enter a valid card expiration date");
        return;
    }

    fetch(`/users/updateInfo/${accountID}/${password.value}/${email.value}/${phone.value}/${cardNumber.value}/${cardExpiration.value}/${cvv.value}`)
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        loadData();
        alert("Account information updated");
    })
    .catch((error) => {
        console.log(error);
    })
})

document.getElementById("account").addEventListener('click', () => {
    localStorage.setItem("signUp", "false");
    window.location.href = "/account"
})

document.getElementById("logout").addEventListener('click', () => {
    window.location.href = "/login"
})

document.getElementById("logo").addEventListener('click', () => {
    window.location.href = "/homePage"
})

document.addEventListener('click', function(event) {
    if (event.target.matches('.refund-btn')) {
        console.log(event.target.id);
        fetch(`/purchases/refund/${event.target.id}`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            loadData();
            alert("Refund successful");
        })
        .catch((error) => {
            console.log(error);
        })
    }
});

async function loadData() {
    if (signUp === "true"){
        const username = document.getElementById("username");
        const password = document.getElementById("password");
        const firstName = document.getElementById("firstName");
        const lastName = document.getElementById("lastName");
        const email = document.getElementById("email");
        const phone = document.getElementById("phoneNumber");
        const cardNumber = document.getElementById("cardNumber");
        const cardExpiration = document.getElementById("cardExpiry");
        const cvv = document.getElementById("cvv");

        username.value = "";
        password.value = "";
        firstName.value = "";
        lastName.value = "";
        email.value = "";
        phone.value = "";
        cardNumber.value = "";
        cardExpiration.value = "";
        cvv.value = "";
    }
     
    else{
        await fetch(`/users/getInfo/${accountID}`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            const username = document.getElementById("username");
            const password = document.getElementById("password");
            const firstName = document.getElementById("firstName");
            const lastName = document.getElementById("lastName");
            const email = document.getElementById("email");
            const phone = document.getElementById("phoneNumber");
            const cardNumber = document.getElementById("cardNumber");
            const cardExpiration = document.getElementById("cardExpiry");
            const cvv = document.getElementById("cvv");
    
            username.value = data[0][1];
            username.disabled = true;
            password.value = data[0][2];
            firstName.value = data[0][3];
            firstName.disabled = true;
            lastName.value = data[0][4];
            lastName.disabled = true;
            email.value = data[0][5];
            phone.value = data[0][6];
            cardNumber.value = data[0][7];
            cardExpiration.value = data[0][8];
            cvv.value = data[0][9];
        })
        .catch((error) => {
            console.log(error);
        })

        await fetch(`/purchases/history/${accountID}`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            
            const movieList = document.getElementById("moviesList");
            while (movieList.firstChild) {
                movieList.removeChild(movieList.firstChild);
            }
            for (let index of data[0]){
                console.log(index);
                let li = document.createElement("li");
                li.className = "purchase-card";
                let h3 = document.createElement("h3");
                h3.textContent = `Purchase ID: ${index[0]}`;
                let h3second = document.createElement("h3");
                h3second.textContent = `Movie Name: ${index[3]}`;
                let h3third = document.createElement("h3");
                h3third.textContent = `Amount: $${index[2]}`;
                let h3fourth = document.createElement("h3");
                h3fourth.textContent = `Date: ${index[1]}`;
                let btn = document.createElement("button");
                btn.className = "refund-btn";
                btn.id = index[0];
                btn.textContent = "Refund";
                li.appendChild(h3);
                li.appendChild(h3second);
                li.appendChild(h3third);
                li.appendChild(h3fourth);
                li.appendChild(btn);
                movieList.appendChild(li);
            }
        })
        .catch((error) => {
            console.log(error);
        })

        await fetch(`/refunds/${accountID}`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            const refundList = document.getElementById("refundList");
            while (refundList.firstChild) {
                refundList.removeChild(refundList.firstChild);
            }
            for (let index of data[0]){
                console.log(index);
                let li = document.createElement("li");
                li.className = "refund-card";
                let h3 = document.createElement("h3");
                h3.textContent = `Refund ID: ${index[0]}`;
                let h3second = document.createElement("h3");
                h3second.textContent = `Movie Name: ${index[4]}`;
                let h3third = document.createElement("h3");
                h3third.textContent = `Amount: $${index[3]}`;
                let h3fourth = document.createElement("h3");
                let date = index[2].split(",");
                h3fourth.textContent = `Date: ${date[0]}`;
                li.appendChild(h3);
                li.appendChild(h3second);
                li.appendChild(h3third);
                li.appendChild(h3fourth);
                refundList.appendChild(li);
            }
        })
        .catch((error) => {
            console.log(error);
        })
    }
}