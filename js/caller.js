function show_usert() {
    $.ajax({
        // la URL para la petición
        url : 'http://localhost:8000/api/usert-list/',
    
        // la información a enviar
        // (también es posible utilizar una cadena de datos)
        data : "12",
    
        // especifica si será una petición POST o GET
        type : 'GET',
    
        // el tipo de información que se espera de respuesta
        dataType : 'json',
    
        // código a ejecutar si la petición es satisfactoria;
        // la respuesta es pasada como argumento a la función
        success : function(json) {
            document.getElementById("name").innerHTML= json[1].firstName;
            //$('<div class="content"/>')
                //.html(json.html).appendTo('body');
            console.log(json)
        },
    
        // código a ejecutar si la petición falla;
        // son pasados como argumentos a la función
        // el objeto de la petición en crudo y código de estatus de la petición
        error : function(xhr, status) {
            alert('Disculpe, existió un problema');
        },
    
        // código a ejecutar sin importar si la petición falló o no
        complete : function(xhr, status) {
            //alert('Petición realizada');
        }
    });
}
