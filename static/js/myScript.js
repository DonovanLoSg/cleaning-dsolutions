$(document).ready(function () {

    // HTML editor for article contribution and edition
	tinymce.init({
		selector: 'textarea#input-content',
		menubar: false,
		plugins: [
			"advlist autolink lists link image charmap print preview anchor",
			"searchreplace visualblocks code fullscreen",
            "insertdatetime media table paste code help wordcount",
            "importcss"
		],
		toolbar: "undo redo | formatselect | " +
			"bold italic backcolor | alignleft aligncenter " +
			"alignright alignjustify | bullist numlist outdent indent | " +
            "removeformat | help",
        content_css: '../css/articleContent.css',
        style_formats: [
            {title: 'Header 1', inline: 'h1', styles: {color: 'darkred'}},
                
            ],
            style_formats_merge: true
        });


    // DataTables

	if (document.getElementById("myTable")) {
        $("#myTable").DataTable({
            responsive: true,
            searching: true,
            ordering: true,
            info: true,
            columnDefs: [{
                "orderable": false,
                "targets": -1
            }],

        });
    };

	if (document.getElementById("tableHomePage")) {
		$("#tableHomePage").DataTable({
			responsive: true,
			paging: false,
			searching: false,
			ordering: false,
			info: false,
		});
	}

	if (document.getElementById("tableUsers")) {
		$("#tableUsers").DataTable({
			responsive: true,
			paging: true,
			searching: true,
			ordering: true,
            info: false,
            columnDefs: [{
                "orderable": false,
                "targets": -1
            }],
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
    
	if (document.getElementById("tableComments")) {
		$("#tableComments").DataTable({
			responsive: true,
			paging: true,
			searching: true,
			ordering: true,
            info: false,
            columnDefs: [{
                "orderable": false,
                "targets": -3
            }],
            })};

	// Tooltip
	$('[data-toggle="tooltip"]').tooltip();


	// auto close alert message

	window.setTimeout(function () {
		$(".alert").fadeTo(500, 0).slideUp(500, function () {
			$(this).remove();
		});
	}, 3000);
});

