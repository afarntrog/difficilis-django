// var input_counter = 0;
// var good_numbers = [];
// var ignore_numbers = [];
// var good_numbers_string = '';
// var ignore_numbers_string = '';
// var SEP = "-"; // This will be the string that seperates the values.

// $(document).ready( function () {
//     // #https://stackoverflow.com/a/4581301

//     $("#myButton").on("click", (function( event ) {
//         // Get all the reason elements for this form.
//         var all_reason_elements = [];
//         all_reason_elements = $("#form-first-half").find("input");
        
    
//         // Get all select elements for this form.
//         var all_importance_elemnets = [];
//         all_importance_elemnets = $("#form-first-half").find("select");
    
//         // Get number of reasons so that we can use in for loop. Reasons and importance are the SAME length.
//         var total_amnt_of_reasons = all_reason_elements.length;
    
//         // Initilaize string
//         var form1_reasons_table_string = "";
//         // Loop through and get the values for each reason and it's corresponding importance. Then store it in a string
//         // Then store in string seperated only by a ~ between each one and a a | between group
//         // Goal: Change each name attribute so that we can parse and use it in the form.
//         // Must start from index 1 because in django the first index name is 'csrfmiddleware'
//         for (var index = 1; index < total_amnt_of_reasons; index++) {
//           all_reason_elements[index].name = "input_" + index;
//         }
//         // Set value of hidden input field for form 1
//         $("#total_form_1_elem").val(total_amnt_of_reasons);

//         for ( var index = 0; index < all_importance_elemnets.length; index++) {
//             current_select_item = all_importance_elemnets[index]
//             // This gets the selected choice
//             current_select_item[current_select_item.selectedIndex].text;
//         }
//     }))
//     // Store good and bad numbers in this global list.


//   // ::DELETE REASON::
//   // This will delete a reason element when the user clicks the red X button
//   // IMPORTANT! .click() does NOT work for dynamically added elements. So in our case it wouldn't be able to delete an element. (https://stackoverflow.com/a/15090957)(https://stackoverflow.com/questions/9122078/difference-between-onclick-vs-click)
//   $(document.body).on("click",".delete_button", function() {
//     // ADDED FUNCTIONALTY THAT WILL NOT ALLOW USER TO DELETE LAST REASON.
//     // This is a beauty! Get the form id and then count all the form-rows in that form( either first ahlf or second)
//     // This way you can count to make sure it is not the last reason that a user is trying to delete.
//     this_form_id = $(this).parent().parent().parent().parent().parent().attr("id");
//     // Get all the rows and store as an array. Must add the "#" beacuse this tells jQuery that it is an id.
//     all_form_rows = $("#" + this_form_id).find(".form-row");
//     // var hello = $(this).parent().parent().parent().parent().next();//.parent().parent().parent().parent().parent().parent().html();//.parent().parent().parent().prev().prev().prev('input').attr("id");
//     // $(hello).find("div").html();
//     // Do not allow user to delete the last reason. There must be at least *1* reason!
//     if (all_form_rows.length != 1)
//         $(this).parent().parent().parent().parent().remove();
//         // Remove this input field from our list of good values.
//         // Get the number we need to remove
//         // var this_input_num = 
//         // good_numbers.indexOf();
//   });// End delete button function


//   // This will ADD reason elements to the page for the first form.
//   $("#add-reason-form-1").on("click", function() {
//       // Store this as a good number 
//     //   good_numbers.push(input_counter);
//     //   input_counter +=1;
//     //   alert(input_counter);
//     // $("#form-first-half").append(new_reason_element);
//     $("#form-first-half").append(reason_part_one + input_counter + reason_part_two);
//   });

//   // This will ADD reason elements to the page for the second form.
//   $("#add-reason-form-2").on("click", function() {
//     $("#form-second-half").append(new_reason_element);
//   });

//  }); // END READY function.


//  /**
//   * This will get all the select elements in the form. and then get the index value for each select element
//   *  For example, each select element has five choices. They are displayed in order from least important to more important.
//   *  Loop through all the select elements.
//   *  Get the index of the selected choice, multiply it by two. then store the result of the value to a running total.
//   *  Do this for each form.
//   *  Whichever form is bigger then that part of the dilemma wins!
//   */

//  var get_reasons_weight = function(){
//     // ::Form 1::
//     // Get the weight for all the reasons for form 1.
//     var form_1_total_weight = 0;
//     var all_select_elements = [];
//     all_select_elements = $("#form-first-half").find("select");

//     // Get number of reasons so that we can use in for loop.
//     var total_amnt_of_reasons = all_select_elements.length;

//     // Loop through and store the total weight of form one.
//     for (var index = 0; index < total_amnt_of_reasons; index++) {
//       form_1_total_weight += parseInt(all_select_elements[index].value);
//     }

//     // ::Form 2::
//     // Get the weight for all the reasons for form 2
//     var form_2_total_weight = 0;
//     var all_select_elements = []; // reset the all_select_element.
//     all_select_elements = $("#form-second-half").find("select");

//     var total_amnt_of_reasons = all_select_elements.length;
//     // Loop through and get the total weight of form 2.
//     for (var index = 0; index < total_amnt_of_reasons; index++) {
//       form_2_total_weight += parseInt(all_select_elements[index].value);
//     }
//     // Get the winner.
//     var winner = dilemma_winner(form_1_total_weight, form_2_total_weight);

//     // This will store the text of the part o the dilemma that won in sessionStorage.
//     store_winner_results(winner);
  
//   };


// // Function to calculate which dilemma has more weight.
// var dilemma_winner =  function(form_1_total_weight, form_2_total_weight) {
//   if (form_1_total_weight > form_2_total_weight) {
//     return 1;
//   }
//   else if(form_1_total_weight < form_2_total_weight) {
//     return 2;
//   }
//   else {
//     return 3; // They are a tie.
//   }
// };

// // This function stores the results of the dilemma in: 1) sessionCookie (aka fake database) 
// // 2) returns result text so we can add to Reason Modal
// var store_winner_results = function(winner) {
//   // Get the dilemma count from storage so we can append it to the key when storing it
//   var dilemma_count = localStorage.dilemma_count;

//   if (winner == 1){
//     // Get the text of the first half of the dilemma and store it in session.
//     var result_decision = $("#reason-1-title").text();
//     localStorage.setItem("result" + dilemma_count, result_decision); 
//   }
//   else if (winner == 2) {
//     // Get the text of the second half of the dilemma and store it in session.
//     var result_decision = $("#reason-2-title").text();
//     localStorage.setItem("result" + dilemma_count, result_decision);
//   }
//   else {
//     result_decision = "Too close to call. Try again."
//     localStorage.setItem("result" + dilemma_count, result_decision);
//   }
//   // Store the winner in the Modal footer.
//   $("#reason-modal-footer").text(result_decision);
// }


// // ADD new reason element HTML.
// // This will store the reasons element text and values so we can use in different functions.
// var new_reason_element = '<div class="form-row">'
//     +'<div class="col-md-8">'
//     +    '<div class="input-group mb-3">'
//     +        '<div class="input-group-prepend">'
//     +            '<button class="btn btn-outline-secondary" type="button"><span class="handle">=</span></button>'
//     +        '</div>'
//     +        '<input type="text" class="form-control" name="number_' + input_counter + '"' + 'placeholder="Reason...">'
//     +    '</div>'
//     + '</div>'
//     +'<div class="col-md-4" id="number_' + input_counter + '"' +'>'
//     +    '<div class="input-group mb-3">'
//     +        '<select class="browser-default custom-select">'
//     +            '<option selected>Select Importance...</option>'
//     +            '<option value="1">Not really important</option>'
//     +            '<option value="2">Somewhat Important</option>'
//     +            '<option value="3">Important</option>'
//     +            '<option value="4">Very Important</option>'
//     +            '<option value="5">Extremely Important</option>'
//     +        '</select>'
//     +        '<div class="input-group-append">'
//     +            '<button class="btn btn-outline-danger delete_button" type="button">X</button>'
//     +        '</div>'
//     +    '</div>'
//     +'</div>'
//     +'</div>'

//     var reason_part_one = '<div class="form-row">'
//     +'<div class="col-md-8">'
//     +    '<div class="input-group mb-3">'
//     +        '<div class="input-group-prepend">'
//     +            '<button class="btn btn-outline-secondary" type="button"><span class="handle">=</span></button>'
//     +        '</div>'
//     +        '<input type="text" class="form-control" name="number_' + input_counter + '"' + 'placeholder="Reason...">'
//     +    '</div>'
//     + '</div>'
//     +'<div class="col-md-4" id="number_';
//      var reason_part_two = '">'
//     +    '<div class="input-group mb-3">'
//     +        '<select class="browser-default custom-select">'
//     +            '<option selected>Select Importance...</option>'
//     +            '<option value="1">Not really important</option>'
//     +            '<option value="2">Somewhat Important</option>'
//     +            '<option value="3">Important</option>'
//     +            '<option value="4">Very Important</option>'
//     +            '<option value="5">Extremely Important</option>'
//     +        '</select>'
//     +        '<div class="input-group-append">'
//     +            '<button class="btn btn-outline-danger delete_button" type="button">X</button>'
//     +        '</div>'
//     +    '</div>'
//     +'</div>'
//     +'</div>'


