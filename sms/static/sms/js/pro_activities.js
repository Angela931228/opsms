$(document).ready(function() {

		$('.edit').click( function() {
			idx = this.id
	         $.ajax({
			        type: 'get',
			        url: '/sms/sales_management/proact_editview'+idx,
			        success: function(data){
           				 // data.redirect contains the string URL to redirect to
          						  //window.location.href = window.location.host+ '/sms/sales_management/promo_analysis';
          				document.location.href = '/sms/sales_management/proact_editview'+idx;
			        }
   			});
	        return false;
    } );

         $('.delete').click( function() {

	 		 idx = this.id
	         $.ajax({
			        type: 'POST',
			        url: '/sms/sales_management/proact_delete',
			        data:  JSON.stringify({'data':idx}),
			        dataType: 'json',
			        success: function(data){
			                 if (data.status == 1) {
           				 // data.redirect contains the string URL to redirect to
          						  console.log(window.location.host)
          						  //window.location.href = window.location.host+ '/sms/sales_management/promo_analysis';
          						  document.location.href = '/sms/sales_management/proact_management/';
       					 }
			        }
   			});
	        return false;
    } );

		 $('#search').click( function() {
    		 var name = $('#searchtext').val();
    		 console.log(name)
	         $.ajax({
			        type: 'POST',
			        url: '/sms/sales_management/proact_search',
			        data:  JSON.stringify({'data':name}),
			        dataType: 'json',
			        success: function(data){
			        	  $('#dis_detail').html(data)
			        }		
   			});
	        return false;
    	} );         
           $('.pause').click( function() {
         	console.log(this.id)
	 		 idx = this.id
	         $.ajax({
			        type: 'POST',
			        url: '/sms/sales_management/proact_pause',
			        data:  JSON.stringify({'data':idx}),
			        dataType: 'json',
			        success: function(data){
			                 if (data.status == 1) {
           				 // data.redirect contains the string URL to redirect to
          						  console.log(window.location.host)
          						  //window.location.href = window.location.host+ '/sms/sales_management/promo_analysis';
          						  document.location.href = '/sms/sales_management/proact_management/';
       					 }
			        }
   			});
	        return false;
    	} );
         $('.reopen').click( function() {
         		
	 		 idx = this.id
	         $.ajax({
			        type: 'POST',
			        url: '/sms/sales_management/proact_reopen',
			        data:  JSON.stringify({'data':idx}),
			        dataType: 'json',
			        success: function(data){
			                 if (data.status == 1) {
           				 // data.redirect contains the string URL to redirect to
          						  console.log(window.location.host)
          						  //window.location.href = window.location.host+ '/sms/sales_management/promo_analysis';
          						  document.location.href = '/sms/sales_management/proact_management/';
       					 }
			        }
   			});
	        return false;
    	} );
         $('.view_detail').click( function() {
         		
	 		 idx = this.id
	         $.ajax({
			        type: 'get',
			        url: '/sms/sales_management/proact_view'+idx,
			        success: function(data){
			        	  $('#dis_detail').html(data)
			        }
   			});
	        return false;
    	} );
       
} );