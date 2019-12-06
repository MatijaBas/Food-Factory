/*
* Add and remove new ingredient lines on user click
* For add_recipe.html & edit_recipe.html pages
*/

let ingredientsCount = $(".ingredients").length;

/* Add new line */
$(".add-ing").click(function () {
    $(".ingredients:first").clone()
        .insertBefore(".add-ing")
        .find("input[type='text']").val("");
    ingredientsCount += 1;
});

/* Remove last line */
$(".remove-ing").click(function () {
    if (ingredientsCount > 1) {
        $(".ingredients:last").remove();
        ingredientsCount -= 1;
    }
});

/*
* Add and remove new instruction lines on user click
*/
let instructionCount = $(".instructions").length;

/* Add new line */
$(".add-instruction").click(function () {
    $(".instructions:first").clone()
        .insertBefore(".add-instruction")
        .find("input[type='text']").val("");
    instructionCount += 1;
});

/* Remove last line */
$(".remove-instruction").click(function () {
    if (instructionCount > 1) {
        $(".instructions:last").remove();
        instructionCount -= 1;
    }
});