$('.nav-tabs a').click(function (e) {
	console.log("click detected")
	$.get( "/sms/1/", function( data ) {
	  	$( "#result" ).html( data );
		});
})