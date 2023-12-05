document.addEventListener('DOMContentLoaded', function () {


    var movieTitle = document.getElementById('movie-title')
    var movieIDForSales = document.getElementById('userName').value; // Note: The ID 'userName' seems incorrect for a movie ID. Consider renaming it for clarity.
    var userListMovieID = document.getElementById('listView').value;

    var addMovieTitle = document.getElementById('movie-title').value; // Note: This ID is duplicated. Ensure unique IDs for each input.
    var addMovieGenre = document.getElementById('movie-genre').value;
    var addMovieDescription = document.getElementById('movie-description').value;
    var addMovieDirector = document.getElementById('movie-director').value;
    var addMovieCast = document.getElementById('movie-cast').value;
    var addMovieRating = document.getElementById('movie-rating').value;
    var addMovieTrailer = document.getElementById('movie-trailer').value;
    var addMovieImage = document.getElementById('movie-image').value;

    var scheduleMovieID = document.getElementById('movie-id').value;
    var scheduleDate = document.getElementById('add-movie-date').value;

    var deleteScheduleMovieID = document.getElementById('search-movie-id').value;
    var deleteUserUsername = document.getElementById('userName').value; // Note: This ID is used for multiple purposes. Ensure unique IDs.

    // Event listener for LOG OUT button
    document.querySelector('.logout-button').addEventListener('click', function () {
        logout();
    });

    // Event listener for SEARCH movie button
    document.querySelector('#search-movie').addEventListener('click', function () {
        // searchMovie();
    });

    // Event listener for VIEW sales button
    document.querySelector('#view-sales').addEventListener('click', function () {
        viewSales();
    });

    // Event listener for VIEW users list per movie purchase button
    document.querySelector('#view-list').addEventListener('click', function () {
        viewUserList();
    });

    // Event listener for ADD movie button
    document.querySelector('#add-movie').addEventListener('click', function () {
        addMovie();
    });

    // Event listener for ADD schedule button
    document.querySelector('#add-schedule').addEventListener('click', function () {
        addSchedule();
    });

    // Event listener for DELETE schedule button
    document.querySelector('#delete-schedule').addEventListener('click', function () {
        deleteSchedule();
    });

    // Event listener for VIEW users button
    document.querySelector('#deleteUsers').addEventListener('click', function () {
        viewUsers();
    });

    // Event listener for DELETE user button
    document.querySelector('#delete-user').addEventListener('click', function () {
        deleteUser();
    });

    // Event listener for ADD Public Service Announcement button
    document.querySelector('#addAnnouncement').addEventListener('click', function () {
        addAnnouncement();
    });

    // Event listener for DELETE Public Service Announcement button
    document.querySelector('#deleteAnnouncement').addEventListener('click', function () {
        deleteAnnouncement();
    });

    function logout() {
        alert("Hello")
    }
    
    function searchMovie() {
        // movieName = movieTitle.value
        // fetch(`/movies/searchMovieName/${movieName}`)
        // .then((res) => res.json())
        // .then((data) => {
        //     const tableBody = document.querySelector('table tbody'); // Select the tbody element where you want to append the data

        //     // Clear existing rows if you want to refresh the data
        //     tableBody.innerHTML = '';
    
        //     // Assuming data[0] is an array of movies
        //     data[0].forEach((movie, index) => {
        //         if(index < 100) {
        //             const movieID = movie[0]; // ID Code
        //             const movieTitle = movie[1]; // Movie Title
    
        //             // Create a new row and cells
        //             const row = document.createElement('tr');
        //             const idCell = document.createElement('td');
        //             const titleCell = document.createElement('td');
    
        //             // Append the text to the cells
        //             idCell.textContent = movieID;
        //             titleCell.textContent = movieTitle;
    
        //             // Append the cells to the row
        //             row.appendChild(idCell);
        //             row.appendChild(titleCell);
    
        //             // Append the row to the tbody
        //             tableBody.appendChild(row);
        //         }
        //     });
        // })
        // .catch((err) => console.log(err));
    }
    
    function viewSales() {
        // Logic for viewing sales
    }
    
    function viewUserList() {
        // Logic for viewing user list
    }
    
    function addMovie() {
        // Logic for adding a movie
    }
    
    function addSchedule() {
        // Logic for adding a schedule
    }
    
    function deleteSchedule() {
        // Logic for deleting a schedule
    }
    
    function viewUsers() {
        // Logic for viewing users
    }
    
    function deleteUser() {
        // Logic for deleting a user
    }
    
    function addAnnouncement() {
        // Logic for adding a public service announcement
    }
    
    function deleteAnnouncement() {
        // Logic for deleting a public service announcement
    }
    
    // ... Define more functions for other buttons as needed
    

});

