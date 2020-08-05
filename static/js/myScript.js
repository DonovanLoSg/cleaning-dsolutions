$(document).ready( function () {
    $('#myTable').DataTable( "stateSave": true);

    $('#myTable2').DataTable({
        "paging" : false,
        "ordering" : false,
        "info" : false,
        "stateSave": true
    });

    
} );

