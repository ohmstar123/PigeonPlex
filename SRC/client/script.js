document.getElementById('deleteButton').addEventListener('click', function() {
    var table = document.getElementById('excel-like-table');
    var checkboxes = table.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            var row = checkbox.parentElement.parentElement;
            row.parentNode.removeChild(row);
        }
    });
});
