$(document).ready(function() {

    // HTML editor for article contribution and edition
    tinymce.init({
        selector: 'textarea#input-content',
        menubar: false,
        plugins: [
            "advlist autolink lists link image charmap print preview anchor",
            "searchreplace visualblocks code fullscreen",
            "insertdatetime media table paste code help wordcount",
        ],
        toolbar: "undo redo | formatselect | " +
            "bold italic backcolor | alignleft aligncenter " +
            "alignright alignjustify | bullist numlist outdent indent | " +
            "removeformat | help",
    });

 
    // DataTables
    $("#myTable").DataTable({
        responsive: true,
        searching: true,
        ordering: true,
        info: true,
        columnDefs: [{ "orderable": false, "targets": -1 }],

    });

    $("myTable").on("click", function(event) {
        event.preventDefault();

        if (document.getElementById("tableHomePage")) {
            $("#tableHomePage").DataTable({
                responsive: true,
                paging: false,
                searching: false,
                ordering: false,
                info: false,
            });
        }
    });

    if (document.getElementById("tableUsers")) {
        $("#tableUsers").DataTable({
            responsive: true,
            paging: false,
            searching: false,
            ordering: false,
            info: false,
        });
    }

    if (document.getElementById("tableLocations")) {
        $("#tableLocations").DataTable({
            responsive: true,
            paging: false,
            searching: false,
            ordering: false,
            info: false,
        });
    }

    // Tooltip
    $('[data-toggle="tooltip"]').tooltip();







    // auto close alert message

    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function() {
            $(this).remove();
        });
    }, 2000);
});


