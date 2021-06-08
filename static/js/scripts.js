// Code structure used and changed to suit the purpose of this website https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery 

// Load function once document is loaded
$(document).ready(function () {
// Declaration of variables used
    var ingred_max_fields = 15; //maximum input boxes allowed
    var instruc_max_fields = 15; //maximum input boxes allowed
    var ingred_wrapper = $(".input_ingred_wrap"); //Fields wrapper
    var instruc_wrapper = $(".input_instruc_wrap"); //Fields wrapper
    var add_ingredient = $(".add_ingredient_button"); //Add button ID
    var add_instruction = $(".add_instruction_button"); //Add button ID

    var x = 1; //initlal text box count
    $(add_ingredient).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < ingred_max_fields) { //max input box allowed
            x++; //text box increment
            $(ingred_wrapper).append('<div><input type="text" input id="dessert_ingredients" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

// Remove form field upon click
    $(ingred_wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })

    var x = 1; //initlal text box count
    $(add_instruction).click(function (e) { //on add input button click
        e.preventDefault();
        if (x < instruc_max_fields) { //max input box allowed
            x++; //text box increment
            $(instruc_wrapper).append('<div><input type="text" input id="dessert_instructions" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

// Remove form field upon click
    $(instruc_wrapper).on("click", ".remove_field", function (e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })

});