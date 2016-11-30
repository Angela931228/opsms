$(document).ready(function() {

	 	ed = moment(new Date($('#end_date').attr('name'))).format('YYYY-MM-DD');
	 	sd = moment(new Date($('#start_date').attr('name'))).format('YYYY-MM-DD');
	 	$('#start_date').val(sd)
	 	$('#end_date').val(ed)

		$('button').click( function() {
	         var discount = $('#discount_rate').val();
	         var start_date = $('#start_date').val();
	         var priority = $('#priority').val();
	         var end_date = $('#end_date').val();
	         var event_name = $('#event_name').val();
	         var event_id = $('#event_id').val();
	         var staff = $('#staff').val();
	        $.ajax({
			        type: 'POST',
			        url: '/sms/sales_management/proact_edit/',
			        data:  JSON.stringify({'event_name':event_name,'priority':priority,'discount_rate':discount,'start_date':start_date,'end_date':end_date,'event_id':event_id,'staff':staff}),
			        dataType: 'json',
			        success: function(data){
			                 if (data.status == 1) {
           				 // data.redirect contains the string URL to redirect to
          						  console.log(window.location.host)
          						  //window.location.href = window.location.host+ '/sms/sales_management/promo_analysis';
          						  document.location.href = '/sms/sales_management/proact_management';
       					 }
			        }
   			});
	        return false;
    } );

         
       
} );