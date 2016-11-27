$(document).ready(function() {
        var table =  $('#expiryTable').DataTable( {

        } );

         $('#select-all').on('click', function(){
	      // Get all rows with search applied
	      // Check/uncheck checkboxes for all rows in the table
	        $('input[type="checkbox"]').prop('checked', this.checked);
        });

         $('button').click( function() {
	         var data = table.$('input').serializeArray();
	         var discount = $('#discount_rate').val();
	         var start_date = $('#start_date').val();
	         var end_date = $('#end_date').val();
	         var event_name = $('#event_name').val();
	 
	         $.ajax({
			        type: 'POST',
			        url: '/sms/sales_management/expiry_food_discount/',
			        data:  JSON.stringify({'data':data,'event_name':event_name,'discount_rate':discount,'start_date':start_date,'end_date':end_date}),
			        dataType: 'json',
			        success: function(data){
			                 if (data.status == 1) {
           				 // data.redirect contains the string URL to redirect to
          						  console.log(window.location.host)
          						  //window.location.href = window.location.host+ '/sms/sales_management/promo_analysis';
          						  document.location.href = '/sms/sales_management/promo_analysis';
       					 }
			        }
   			});
	        return false;
    } );
} );