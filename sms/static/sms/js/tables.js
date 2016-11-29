$(document).ready(function() {
        $('#expiryTable').dataTable({
        	"iDisplayLength": 10
        });
        $('#example').dataTable({
        	"iDisplayLength": 5
        });
  		if($('#mba')){
	  		 $('#mba').dataTable({
	        	"iDisplayLength": 5,
	        	 "aaSorting": [[ 5, "desc" ]]
	        });
  		}
		$('#example1').dataTable({
        	"iDisplayLength": 5
        });

        $('#example2').dataTable({
        	"iDisplayLength": 5
        });
} );