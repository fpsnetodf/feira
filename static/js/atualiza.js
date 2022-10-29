$("#id_atual").click(function(){
    $("#id_anterior").val($("#id_atual").val())
    $("#id_atual").val('')
})
