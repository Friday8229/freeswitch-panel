

var un = "";
var n = "";

function edit_modal(elem_id){
    var name = document.getElementById(elem_id);
    un = elem_id;
    n = name;
    $('#details').modal('show');
    $('#user_name').val(name.innerHTML);
    $('#user_phone').val(elem_id);
}

$("#save_details").on("click", function() {
    cun = $('#user_name').val();
    cn = $('#user_phone').val();
    var name = document.getElementById(un);
    name.innerHTML = cun;
    $(n).attr("id",cn)
    $('#details').modal('hide');
});