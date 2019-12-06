/*
* Add and remove new ingredient lines on user click
* For add_recipe.html & edit_recipe.html pages
*/

let ingCount = $(".ingredients").length;

/* Add new line */
$(".add-ing").click(function() {
    /* Clone line, insert before add/remove btns and clear existing values */
    $(".ingredients:first").clone()
        .insertBefore(".add-ing")
        .find("input[type='text']").val("");
    /* Ensures original line is never removed */
    ingCount += 1;
});

/* Remove last line */
$(".remove-ing").click(function() {
    /* Ensure that the first line can't be removed */
    if (ingCount > 1) {
        $(".ingredients:last").remove();
        ingCount -= 1;
    }
});
