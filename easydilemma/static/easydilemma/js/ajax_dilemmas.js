$( document ).ready( function() {
    $("#get-more-dilemmas").on("click", function() {

        $.ajax({
            type: 'GET',
            url: './more_dilemmas.json',
            success: function( data ) {
                for (var i = 0; i < data.length; i++) {
                    // Write code that loops through and appends                                        
                    var dilemma_header = data[i].dilemma;

                    var card_header_html = '<div class="container mb-5"><div class="card w-75 mx-auto">'
                                            + '<div class="card-header"><h5>Dilemma: <span id="reason-card-header">'
                                            + dilemma_header
                                            + '</span></h5></div>'
                                                // Add card body html [Card part 3]
                                            + '<div class="card-body" id="reason-card-body">';
                    // Get all the reaosns stored in json. Loop through the array and store results into html                        
                    var all_reasons = data[i].reasons;
                    var all_importance = data[i].importance;

                    for ( var index = 0; index < all_reasons.length; index++) {
                        var reason = all_reasons[index];
                        var importance = all_importance[index];

                            var card_body_html = '<div class="row mb-3"><div class="col-md-8"><input type="text" class="form-control font-weight-bold expand-reason text-truncate" value=' 
                                                + '"' + reason + '" ' + ' readonly>'
                                                +'<div class="p-2 mb-3 rounded text-dark font-weight-bold border text-center bg-light" style="display: none" id="full-reason-div">' 
                                                + reason + '</div>'
                                                + '</div><div class="col-md-4"><input type="text" class="form-control text-center font-weight-bold" value=' 
                                                + "'" 
                                                + importance + "' " + 'placeholder="*" readonly></div></div>';

                    }
                    // get the result and store it in html
                    var result_string = data[i].result;
                    var card_footer_html = '</div><div class="card-footer"><h5 class="font-weight-bold">Result: <span id="reason-card-footer">' 
                                            + result_string + '</span></h5></div></div></div>';
                    // Combine entire card;                        
                    var complete_html_card = card_header_html + card_body_html + card_footer_html;
            
                    // Add the entire new card to the page
                    $("#add-content").append( complete_html_card );
                } // end data loop
        







            } // End success funtion
        }); //  End ajax

    }); // End click func

}); // End ready
