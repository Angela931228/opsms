$(document).ready(function() {

    $('input[type="checkbox"]').change( function() {
            
            if ($(this).is(':checked')) {
                $('#itemPrice').css("visibility", "visible") ;      
            }else{
                $('#itemPrice').css("visibility", "hidden") ; 
            }

    })
     $('button').click( function() {
             var data = [{'name':'liquor'},{'name':'red/blush wine'},{'name':'bottled beer'}];
             var discount = $('#discount_rate').val();
             var priority = $('#priority').val();
             var start_date = $('#start_date').val();
             var end_date = $('#end_date').val();
             var event_name = $('#event_name').val();
     
             $.ajax({
                    type: 'POST',
                    url: '/sms/sales_management/mb_analysis/',
                    data:  JSON.stringify({'data':data,'event_name':event_name,'priority':priority,'discount_rate':discount,'start_date':start_date,'end_date':end_date}),
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