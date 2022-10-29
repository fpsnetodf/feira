
var lista = $('.soma');
var ant = $('.ant');
var atual = $('.atual');
var total = $('.total')
var subtotal = $('.subtotal')
var qtd = $('.qtd')
var ip = $('.il-p')
var ac = $('.comum')
var kwh = $('.kwh')
var totals = 0;
var formato = { minimumFractionDigits: 2 , style: 'currency', currency: 'BRL' }

var st = 0;
for (i = 0; i <= lista.length; i ++){
  var Qtd = $(qtd[i]).textContent;
  var Atual = $(atual[i]).html();
  var Ant =  $(ant[i]).html();
          
  var Total = parseFloat(Atual - Ant)
  $(lista[i]).html(Total);
  $(subtotal[i]).html(parseFloat((Atual - Ant) * 0.75).toFixed(2))
  $(ip[i]).html((parseFloat(ip[i].textContent.replace(",", ".")) * parseFloat(qtd[i].textContent)).toFixed(2));
  $(ac[i]).html(parseFloat(qtd[i].textContent) * parseFloat(ac[i].textContent.replace(",", ".")));
  $(total[i]).html( Math.ceil(parseFloat(Total * 0.75)  + parseFloat(ip[i].textContent) + parseFloat(ac[i].textContent)).toFixed(2));
  totals += parseFloat(total[i].textContent);  
}
$('.subtotal').html("<p>Total arrecadado: R$ </p>" + totals)


// $(document).ready(()=>{
//     var lista = $('.soma');
//     var ant = $('.ant');
//     var atual = $('.atual');
//     var total = $('.total');
//     var qtd = $('.qtd');
//     var ip = $('.il-p');
//     var ac = $('.comum');
//     var totals = 0;
   
//     var formato = { minimumFractionDigits: 2 , style: 'currency', currency: 'BRL' }

//     var st = 0;
//     for (i = 0; i <= lista.length; i ++){         
//         $(lista[i]).html(atual[i].textContent - ant[i].textContent);
//         $(total[i]).html()                 
//         $(ip[i]).html("R$ " + (txilu).toFixed(2))
//         $(ac[i]).html("R$ " + (txcom).toFixed(2))
//         $(lista[i]).html(soma);
//         $(total[i]).html(Math.ceil(((soma * 0.75) + txcom + txilu).toFixed(2)));       
//         st =  $(total[i]).html(Math.ceil(((soma * 0.75))) + txcom + txilu).toFixed(2)  
//         totals += parseFloat($(st).text())
                
//     } 
// })

