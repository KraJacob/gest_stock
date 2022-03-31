console.log("approvisionnement.js");
if (!$) {
    $ = django.jQuery;
}
$(document).ready(function(){
    console.log("ready!");
    // Add event listener to "price" input
    $("#id_ligneapprovisionnement_set-0-quantite").change(function(e){
        // Get entered value
        let price = parseFloat($(this).val());

        console.log(price);

        // Get discount value from another field 
        let discount = parseFloat($("#id_discount").val())

        // Compute total price in whatever way you want
        let total_price = price - price*discount;

        // Set value in read-only "total_price" field.
        $("div.field-total_price").find("div.readonly").text(total_price);
    });
})