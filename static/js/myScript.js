$(document).ready(function () {
	// DataTables
	$("#myTable").DataTable({
		responsive: true,
		paging: true,
		searching: true,
		ordering: true,
		info: true,
		stateSave: false,
	});

	// Tooltip
    $('[data-toggle="tooltip"]').tooltip();

  


// DataTables
$("myTable").on("click", function (event) {
	event.preventDefault();
});

if (document.getElementById("myTable2")) {
	$("#myTable2").DataTable({
		responsive: true,
		paging: false,
		searching: false,
		ordering: false,
		info: false,
	});
}

// HTML editor for article contribution and edition

tinymce.init({
	selector: "textarea#input-content",
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

// auto close alert message

window.setTimeout(function () {
	$(".alert").fadeTo(500, 0).slideUp(500, function () {
		$(this).remove();
	});
}, 2000);