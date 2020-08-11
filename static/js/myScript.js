$(document).ready(function() {
    $('#myTable').DataTable({
        "responsive": true,
        "paging":   true,
        "searching": true,
        "ordering": true,
        "info":     true,
        "stateSave": true
    });
    $('[data-toggle="tooltip"]').tooltip()
} );



$("myTable").on("click", function(event){
  event.preventDefault()
});


if (document.getElementById('myTable2')) {
    $('#myTable2').DataTable({
        "responsive": true,
        "paging":   false,
        "searching": false,
        "ordering": false,
        "info":     false
    } );
}

$("#myTable").on("click", function(){alert('x')} )





 tinymce.init({
    selector: 'textarea#input-content',
    menubar: false,
    plugins: [
        'advlist autolink lists link image charmap print preview anchor',
        'searchreplace visualblocks code fullscreen',
        'insertdatetime media table paste code help wordcount'
    ],
    toolbar: 'undo redo | formatselect | ' +
    'bold italic backcolor | alignleft aligncenter ' +
    'alignright alignjustify | bullist numlist outdent indent | ' +
    'removeformat | help',
    
    });