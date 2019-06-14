/*
https://stackoverflow.com/questions/36134418/preloader-loadingoverlay-is-not-a-function
*/
// Show full page LoadingOverlay
$(document).ready( function () {
 
  // :: VALIDATORS::
  // This makes sure that the dilemma form is valid/filled out.
  dilemma_form_validator();
  // This makes sure the login form is validated.
  login_form_validator();
  // This makes sure the sign up form is validated.
  signup_form_validator();


  // ::DELETE REASON::
  // This will delete a reason element when the user clicks the red X button
  // IMPORTANT! .click() does NOT work for dynamically added elements. So in our case it wouldn't be able to delete an element. (https://stackoverflow.com/a/15090957)(https://stackoverflow.com/questions/9122078/difference-between-onclick-vs-click)
  $(document.body).on("click",".delete_button", function() {
    // ADDED FUNCTIONALTY THAT WILL NOT ALLOW USER TO DELETE LAST REASON. BUT THEN I COMMENTED IT OUT. MAYBE USER CAN'T THINK OF A REASON.
    // This is a beauty! Get the form id and then count all the form-rows in that form( either first ahlf or second)
    // This way you can count to make sure it is not the last reason that a user is trying to delete.
    this_form_id = $(this).parent().parent().parent().parent().parent().attr("id");
    // Get all the rows and store as an array. Must add the "#" beacuse this tells jQuery that it is an id.
    all_form_rows = $("#" + this_form_id).find(".form-row");
    // Do not allow user to delete the last reason. There must be at least *1* reason!
    if (all_form_rows.length != 1)
        $(this).parent().parent().parent().parent().remove();
  });// End delete button function


  // This will ADD reason elements to the page for the first form.
  $("#add-reason-form-1").on("click", function() {
    $("#form-first-half").append(form_1_reason_element);
  });

  // This will ADD reason elements to the page for the second form.
  $("#add-reason-form-2").on("click", function() {
    $("#form-second-half").append(form_2_reason_element);
  });

 }); // END READY function.

 /**
  * This will get all the select elements in the form. and then get the index value for each select element
  *  For example, each select element has five choices. They are displayed in order from least important to more important.
  *  Loop through all the select elements.
  *  Get the index of the selected choice, multiply it by two. then store the result of the value to a running total.
  *  Do this for each form.
  *  Whichever form is bigger then that part of the dilemma wins!
  */

  var get_reasons_weight = function(){
    // ::Form 1::
    // Get the weight for all the reasons for form 1.
    var form_1_total_weight = 0;
    var all_select_elements = [];
    all_select_elements = $("#form-first-half").find("select");

    // Get number of reasons so that we can use in for loop.
    var total_amnt_of_reasons = all_select_elements.length;

    // Loop through and store the total weight of form one.
    for (var index = 0; index < total_amnt_of_reasons; index++) {
      form_1_total_weight += parseInt(all_select_elements[index].value);
    }

    // ::Form 2::
    // Get the weight for all the reasons for form 2
    var form_2_total_weight = 0;
    var all_select_elements = []; // reset the all_select_element.
    all_select_elements = $("#form-second-half").find("select");

    var total_amnt_of_reasons = all_select_elements.length;
    // Loop through and get the total weight of form 2.
    for (var index = 0; index < total_amnt_of_reasons; index++) {
      form_2_total_weight += parseInt(all_select_elements[index].value);
    }
    // Get the winner.
    var winner = dilemma_winner(form_1_total_weight, form_2_total_weight);

    // This will store the text of the part o the dilemma that won in sessionStorage.
    store_winner_results(winner);
  
  };


// Function to calculate which dilemma has more weight.
var dilemma_winner =  function(form_1_total_weight, form_2_total_weight) {
  if (form_1_total_weight > form_2_total_weight) {
    return 1;
  }
  else if(form_1_total_weight < form_2_total_weight) {
    return 2;
  }
  else {
    return 3; // They are a tie.
  }
};

// This function stores the results of the dilemma in: 1) sessionCookie (aka fake database) 
// 2) returns result text so we can add to Reason Modal
var store_winner_results = function(winner) {
  // Get the dilemma count from storage so we can append it to the key when storing it
  var dilemma_count = localStorage.dilemma_count;

  if (winner == 1){
    // Get the text of the first half of the dilemma and store it in session.
    var result_decision = $("#reason-1-title").text();
    localStorage.setItem("result" + dilemma_count, result_decision); 
  }
  else if (winner == 2) {
    // Get the text of the second half of the dilemma and store it in session.
    var result_decision = $("#reason-2-title").text();
    localStorage.setItem("result" + dilemma_count, result_decision);
  }
  else {
    result_decision = "Too close to call. Try again."
    localStorage.setItem("result" + dilemma_count, result_decision);
  }
  // Store the winner in the Modal footer.
  $("#reason-modal-footer").text(result_decision);
}

// This functions makes sure that the main dilemma page is fully validated. If it is not then it displays a beautifull error message from bootstrap.
var dilemma_form_validator = function() {
  $("#dilemma-form").submit(function( event ) {
    var is_valid = true;
    
    // validate the email entry with a regular expression
    var input_1 = $("#input-label-1").val().trim();
    var input_2 = $("#input-label-2").val().trim();
    if (input_1 == "") { 
        // Reset this field to blank so that it will trigger the `required suedo-class which will then trigger the bootstrap design to kick in.
        $("#input-label-1").val("");
        is_valid = false;
    }
    if (input_2 == "") {
        // Reset this field to blank so that it will trigger the `required suedo-class which will then trigger the bootstrap design to kick in.  
        $("#input-label-2").val("");
        is_valid = false;
    }

    // If the form is not valid according to my standards then switch the bootstrap classes to display nice GUI validation message.
    if (!is_valid) {
        $("#dilemma-form").removeClass("needs-validation").addClass( "was-validated" )
        event.preventDefault();
        event.stopPropagation();
    }
    
}); // End submit function.
} // End form validator function

// ADD new reason element HTML.
// This will store the reasons element text and values so we can use in different functions.
var form_1_reason_element = '<div class="form-row">'
    +'<div class="col-md-8">'
    +    '<div class="input-group mb-3">'
    +        '<div class="input-group-prepend">'
    +            '<button class="btn btn-outline-secondary" type="button"><span class="handle">=</span></button>'
    +        '</div>'
    +        '<input type="text" class="form-control" placeholder="Reason..." name="reason1" required>'
    +    '</div>'
    + '</div>'
    +'<div class="col-md-4">'
    +    '<div class="input-group mb-3">'
    +        '<select name="form-first-half-select" class="browser-default custom-select">'
    +            '<option selected>Select Importance...</option>'
    +            '<option value="1">Not really important</option>'
    +            '<option value="2">Somewhat Important</option>'
    +            '<option value="3">Important</option>'
    +            '<option value="4">Very Important</option>'
    +            '<option value="5">Extremely Important</option>'
    +        '</select>'
    +        '<div class="input-group-append">'
    +            '<button class="btn btn-outline-danger delete_button" type="button">X</button>'
    +        '</div>'
    +    '</div>'
    +'</div>'
    +'</div>'


var form_2_reason_element = '<div class="form-row">'
    +'<div class="col-md-8">'
    +    '<div class="input-group mb-3">'
    +        '<div class="input-group-prepend">'
    +            '<button class="btn btn-outline-secondary" type="button"><span class="handle">=</span></button>'
    +        '</div>'
    +        '<input type="text" class="form-control" placeholder="Re..." name="reason_2" required>'
    +    '</div>'
    + '</div>'
    +'<div class="col-md-4">'
    +    '<div class="input-group mb-3">'
    +        '<select name="form-second-half-select" class="browser-default custom-select">'
    +            '<option selected>Select Importance...</option>'
    +            '<option value="1">Not really important</option>'
    +            '<option value="2">Somewhat Important</option>'
    +            '<option value="3">Important</option>'
    +            '<option value="4">Very Important</option>'
    +            '<option value="5">Extremely Important</option>'
    +        '</select>'
    +        '<div class="input-group-append">'
    +            '<button class="btn btn-outline-danger delete_button" type="button">X</button>'
    +        '</div>'
    +    '</div>'
    +'</div>'
    +'</div>'

// This functions makes sure that the loginform is fully validated. If it is not then it displays a beautifull error message from bootstrap.
var login_form_validator = function() {
  $("#btnLogin").on("click", (function( event ) {
    var is_valid = true;

    // validate the username and password fields.
    var username_field = $("#login_username").val().trim();
    var password_field = $("#login_password").val().trim();
    if (username_field == "") { 
        // Reset this field to blank so that it will trigger the `required suedo-class which will then trigger the bootstrap design to kick in.
        $("#login_username").val("");
        is_valid = false;
    }
    if (password_field == "") {
        // Reset this field to blank so that it will trigger the `required suedo-class which will then trigger the bootstrap design to kick in.  
        $("#login_password").val("");
        is_valid = false;
    }

    // If the form is not valid according to my standards then switch the bootstrap classes to display nice GUI validation message.
    if (!is_valid) {
        $("#login-form").removeClass("needs-validation").addClass( "was-validated" )
        event.preventDefault();
        event.stopPropagation();
    }
    
})); // End submit function.
} // End form validator function


// This functions makes sure that the loginform is fully validated. If it is not then it displays a beautifull error message from bootstrap.
var signup_form_validator = function() {
  $("#btnSignUp").on("click", (function( event ) {
    var is_valid = true;

    // validate the username and password fields.
    var username_field = $("#sign_up_username").val().trim();
    var password_field = $("#sign_up__password").val().trim();
    if (username_field == "") { 
        // Reset this field to blank so that it will trigger the `required suedo-class which will then trigger the bootstrap design to kick in.
        $("#sign_up_username").val("");
        is_valid = false;
    }
    if (password_field == "") {
        // Reset this field to blank so that it will trigger the `required suedo-class which will then trigger the bootstrap design to kick in.  
        $("#sign_up__password").val("");
        is_valid = false;
    }

    // If the form is not valid according to my standards then switch the bootstrap classes to display nice GUI validation message.
    if (!is_valid) {
        $("#signup-form").removeClass("needs-validation").addClass( "was-validated" )
        event.preventDefault();
        event.stopPropagation();
    }
    
})); // End submit function.
} // End form validator function



/** ## Purpose it to store the entire dilemma for later use. ##//
 * This will get all the reason elements an their text and store it in an array
 * It will then get all  the immportance values and store it in an array
 * It will then loop through them and add them all into one long string seperated only by a * between each reason, a | between group and its importance, and a ~ between each form. 
 */
var store_results = function() {
    // Get all the reason elements for this form.
    var all_reason_elements = [];
    all_reason_elements = $("#form-first-half").find("input");

    // Get all select elements for this form.
    var all_importance_elemnets = [];
    all_importance_elemnets = $("#form-first-half").find("select");

    // Get number of reasons so that we can use in for loop. Reasons and importance are the SAME length.
    var total_amnt_of_reasons = all_reason_elements.length;

    // Initilaize string
    var form1_reasons_table_string = "";
    // Loop through and get the values for each reason and it's corresponding importance. Then store it in a string
    // Then store in string seperated only by a ~ between each one and a a | between group
    for (var index = 0; index < total_amnt_of_reasons; index++) {
      form1_reasons_table_string += all_reason_elements[index].value;
      form1_reasons_table_string += "*";

      // Get the  current select element and store it's selected option text in string
      current_select_item = all_importance_elemnets[index]
      form1_reasons_table_string += current_select_item[current_select_item.selectedIndex].text; // get the text option from this selected item
      form1_reasons_table_string += "|";
    }

    // Repeat process for the second form.
    // Get all the reason elements for this form.
    var all_reason_elements = [];
    all_reason_elements = $("#form-second-half").find("input");

    // Get all select elements for this form.
    var all_importance_elemnets = [];
    all_importance_elemnets = $("#form-second-half").find("select");

    // Get number of reasons so that we can use in for loop. Reasons and importance are the SAME length.
    var total_amnt_of_reasons = all_reason_elements.length;

    // Initilaize string
    var form2_reasons_table_string = "";
    // Loop through and get the values for each reason and it's corresponding importance. Then store it in a string
    // Then store in string seperated only by a ~ between each one and a a | between group
    for (var index = 0; index < total_amnt_of_reasons; index++) {
      form2_reasons_table_string += all_reason_elements[index].value;
      form2_reasons_table_string += "*";

      // Get the current select element and store it's selected option text in string
      current_select_item = all_importance_elemnets[index]
      form2_reasons_table_string += current_select_item[current_select_item.selectedIndex].text; // get the text option from this selected item
      form2_reasons_table_string += "|";
    }

    // ::STORE STUFF::
    // Get the dilemma count so we can use it to store the value in storage
    var dilemma_count = localStorage.dilemma_count;

    // Store the first and second form in storage.
    localStorage.setItem("form_1_dilemma_reasons" + dilemma_count, form1_reasons_table_string);
    localStorage.setItem("form_2_dilemma_reasons" + dilemma_count, form2_reasons_table_string);

    //get the current dilemma and resotre it with the proper dilemmaCount value as a key. EXPLAINED We have to restore it again even though we already stored it earlier because we want to add the dilemma_count as a key so that we can use it in our retirevel loop later in the all_dilemmass page.
    var actual_dilemma = localStorage.getItem("dilemma");
    localStorage.setItem("dilemma" + dilemma_count, actual_dilemma);

}; // End decide button func.

// When the reason page Modal begins to appear then this function will populate the table and display the results
// to the dilemma. It will also call all the other functions to calculate the winner and store the result in sessionCookie.
$(document).on("show.bs.modal","#reason-result-modal", function() {
  $('body').plainOverlay('show', {
    show: function(event) {

          // CREATE a localStorage element to store the amount of dilemmas we have
          // we will use that number to append it to the key of the value to store many dilemmas. EXPLAINED: We have to be able to create many dilemmas and store them in storage. i don't want to have to keep on parsing them et. so we will just dynamically create keys based on the dilemma number we are up to and store that dilemma count inn storage. Then when we need to get a dilemma from storage we will check the dilemma count and loop through all the dilemmas stored in storage by appending the dilemma count to the key and pulling that keys value from storage.
          if ( localStorage.dilemma_count >= parseInt(1) ) {
            var dilemma_count = parseInt(localStorage.dilemma_count) + 1;
            // Now set it back into storage
            localStorage.dilemma_count = dilemma_count;
          }
          else {
            localStorage.dilemma_count = 1;
          }
          // Stores all the results in session cookie
          store_results();
          // Calculates the winner and stores the result in sessionCookie and in the modal footer.
          get_reasons_weight();

        // Get all the reasons and their importance
        // Store each forms results in an array
        // Loop through and display the results in the html
        // Get all the reason elements for this form.
        var all_reason_elements = [];
        all_reason_elements = $("#form-first-half").find("input");

        // Get all select elements for this form.
        var all_importance_elemnets = [];
        all_importance_elemnets = $("#form-first-half").find("select");

        // Get number of reasons so that we can use in for loop. Reasons and importance are the SAME length.
        var total_amnt_of_reasons = all_reason_elements.length;

        // Initilaize string
        // Loop through and get the values for each reason and it's corresponding importance. Then store it in a string
        // Then store in string seperated only by a ~ between each one and a a | between group
        for (var index = 0; index < total_amnt_of_reasons; index++) {
          // Get the current reason and store it in the html
          var reason = all_reason_elements[index].value;
          reasons_html = '<div class="row mb-3"><div class="col-md-8"><input type="text" class="form-control font-weight-bold" value=' 
                          + '"' + reason + '" ' + ' readonly>';

          // Get the  current select element and store it's selected optionin html
          current_select_item = all_importance_elemnets[index]
          var importance = current_select_item[current_select_item.selectedIndex].text;
          var importance_html = '</div><div class="col-md-4"><input type="text" class="form-control text-center font-weight-bold" value=' + "'" + importance + "' " +'placeholder="*" readonly></div></div>';
          var whole_element = reasons_html + importance_html;
      
          $("#reason-modal-body").append(whole_element);
        }
          


        // Repeat process for the second form.
        // Get all the reason elements for this form.
        var all_reason_elements = [];
        all_reason_elements = $("#form-second-half").find("input");

        // Get all select elements for this form.
        var all_importance_elemnets = [];
        all_importance_elemnets = $("#form-second-half").find("select");

        // Get number of reasons so that we can use in for loop. Reasons and importance are the SAME length.
        var total_amnt_of_reasons = all_reason_elements.length;

        // Initilaize string
        var form2_reasons_table_string = "";
        // Loop through and get the values for each reason and it's corresponding importance. Then store it in a string
        // Then store in string seperated only by a ~ between each one and a a | between group
        for (var index = 0; index < total_amnt_of_reasons; index++) {
          // Get the current reason and store it in the html
          var reason = all_reason_elements[index].value;
          reasons_html = '<div class="row mb-3"><div class="col-md-8"><input type="text" class="form-control font-weight-bold" value=' 
                        + '"' + reason + '" ' + ' readonly>';

          // Get the  current select element and store it's selected optionin html
          current_select_item = all_importance_elemnets[index]
          var importance = current_select_item[current_select_item.selectedIndex].text;
          var importance_html = '</div><div class="col-md-4"><input type="text" class="form-control text-center font-weight-bold" value=' + "'" + importance + "' " +'placeholder="*" readonly></div></div>';
          var whole_element = reasons_html + importance_html;

          $("#reason-modal-body").append(whole_element);
        } // End forloop 

        // Close the spiinning waiting overlay.
        $('body').plainOverlay('hide');
        }
        });

}); // END MODAL SHOWN FUNCTION
