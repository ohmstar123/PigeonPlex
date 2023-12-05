let movieID = localStorage.getItem("movieID");
let accountID = localStorage.getItem("accountID");

let seats = [];
let morningSeats = 0;
let afternoonSeats = 0;
let eveningSeats = 0;

document.getElementById("logo").addEventListener('click', () => {
    window.location.href = "/homePage"
})

document.getElementById("account").addEventListener('click', () => {
    localStorage.setItem("signUp", "false");
    window.location.href = "/account"
})

document.getElementById("logout").addEventListener('click', () => {
    window.location.href = "/login"
})

document.getElementById("purchase").addEventListener('click', async () => {
    let selectedTime = document.getElementById("time").value;
    let tickets = document.getElementById("input").value;
    let amount = tickets * 10;
    try {
        if (selectedTime === "Morning"){
            if (tickets > seats[1]){
                alert("Not enough seats available");
                return;
            }
            await fetch(`/purchases/buyTicket/${accountID}/${movieID}/${seats[0]}/morning/${amount}`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error);
            })
            
            await fetch(`/schedule/removeSeat/${movieID}/${amount}/${seats[0]}/morning`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error);
            })
        }
        else if (selectedTime === "Afternoon"){
            if (tickets > seats[2]){
                alert("Not enough seats available");
                return;
            }
            await fetch(`/purchases/buyTicket/${accountID}/${movieID}/${seats[0]}/afternoon/${amount}`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error);
            })
            
            await fetch(`/schedule/removeSeat/${movieID}/${amount}/${seats[0]}/afternoon`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error);
            })
        }
        else if (selectedTime === "Evening"){
            if (tickets > seats[3]){
                alert("Not enough seats available");
                return;
            }
            await fetch(`/purchases/buyTicket/${accountID}/${movieID}/${seats[0]}/evening/${amount}`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error);
            })
            
            await fetch(`/schedule/removeSeat/${movieID}/${amount}/${seats[0]}/evening`)
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.log(error);
            })
        }

        loadData();
    }
    catch (error) {
        console.log(error);
    }
})

let counter = 0;

function increment() {
  counter++;
}

function decrement() {
  counter--;
}

function get() {
  return counter;
}

const inc = document.getElementById("increment");
const input = document.getElementById("input");
const dec = document.getElementById("decrement");
const time = document.getElementById("time");

inc.addEventListener("click", () => {
    if (time.value === "Morning"){
        if (input.value < morningSeats) {
            increment();
        }
    }
    else if (time.value === "Afternoon"){
        if (input.value < afternoonSeats) {
            increment();
        }
    }
    else if (time.value === "Evening"){
        if (input.value < eveningSeats) {
            increment();
        }
    }
    input.value = get();
});

dec.addEventListener("click", () => {
    if (input.value > 0) {
        decrement();
    }
    input.value = get();
});

document.addEventListener('DOMContentLoaded', loadData)

function loadData() {
    console.log(movieID);
    fetch(`/movies/info&Schedule/${movieID}`)
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        let title = document.getElementById("title");
        let description = document.getElementById("description");
        let img = document.getElementById("image");
        let cast = document.getElementById("cast");
        let director = document.getElementById("director");
        let duration = document.getElementById("duration");
        let genre = document.getElementById("genre");
        let rating = document.getElementById("rating");
        let trailer = document.getElementById("trailer");
        let datesDiv = document.getElementById("dates");
        title.textContent = data[0][0][1];
        description.textContent = data[0][0][3];
        img.src = data[0][0][2];
        cast.textContent = data[0][0][4];
        director.textContent = data[0][0][5];
        duration.textContent = data[0][0][6];
        genre.textContent = data[0][0][7];
        rating.textContent = data[0][0][8];
        if (rating.textContent === "-1"){
            rating.textContent = "Not Rated";
        }
        trailer.src = data[0][0][9];
        let date = document.createElement("h2");
        let dateAmount = data[0][0][10];
        let dateText = dateAmount.split(" ");
        seats.push(dateText[0]);
        seats.push(data[0][0][11]);
        morningSeats = data[0][0][11];
        seats.push(data[0][0][12]);
        afternoonSeats = data[0][0][12];
        seats.push(data[0][0][13]);
        eveningSeats = data[0][0][13];
        date.textContent = `${dateText[0]}: Morning: ${data[0][0][11]}, Afternoon: ${data[0][0][12]}, Evening: ${data[0][0][13]}`;
        if (datesDiv.hasChildNodes()){
            datesDiv.removeChild(datesDiv.childNodes[0]);
        }
        datesDiv.appendChild(date);
    })
    .catch((error) => {
        console.log(error);
    })
}