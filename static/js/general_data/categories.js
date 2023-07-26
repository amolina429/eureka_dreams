$(document).ready(function () {
    var domainUrl = document.location.protocol + '//' + document.domain + ':' + document.location.port
    var route = domainUrl + '/'
    $('#container-tab').on('click','#create_category', function () {
        $('#categories').addClass('d-none');
        $('#create_categories').removeClass('d-none');
    })

    $('#container-tab').on('click', '#back_create_category', function () {
        $('#categories').removeClass('d-none');
        $('#create_categories').addClass('d-none');
        categoriasTable.ajax.reload(null, false)
    })


    $('#container-tab').on('click','#createCategory', function (e) {
        e.preventDefault();
        $.ajax({
            headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
            type: 'POST',
            url: route + 'datos-generales/categorias/',
            data: {
                nombre: $('#category_name').val()
            },
            success: function (resp) {
                alertify.success("Categoría Creada!")
            },
            error: function () {
            }
        });
    });

    $('#container-tab').on('click', '#updateCategory', function (e) {
        e.preventDefault();
        let id = $('#category_id').val();
        $.ajax({
            headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
            type: 'PUT',
            url: route + 'datos-generales/categorias/' + id,
            data: {
                id: $('#category_id').val(),
                nombre: $('#category_name').val()
            },
            success: function (resp) {
                alertify.success("Categoría Actualizado!")
                $('#categories').removeClass('d-none');
                $('#create_categories').addClass('d-none');
                categoriasTable.ajax.reload(null, false)
            },
            error: function () {
            }
                    
        });
    });

    $('#container-tab').on('click', '.edit_category', function (e) {
        e.preventDefault()
        let id = $(this).data('id')
        $.ajax({
            headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
            type: 'GET',
            url: route + 'datos-generales/categorias/' + id,
            data: {
                id: id
            },
            beforSend: function () {
                $('#create_categoriesForm')[0].reset()
            },
            success: function (resp) {
                console.log(resp);
                let data = resp.data
                $('#category_id').val(data.id)
                $('#category_name').val(data.nombre)
                $('#categories,#createCategory').addClass('d-none');
                $('#create_categories,#updateCategory').removeClass('d-none');
            },
            error: function () {
            }
        });
    });


    $('#container-tab').on('click', '.delete_category', function (e) {
        e.preventDefault()
        let id = $(this).data('id')
        $.ajax({
            headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
            type: 'DELETE',
            url: route + 'datos-generales/categorias/' + id,
            data: {
                id: id
            },
            beforSend: function () {
                $('#create_categoriesForm')[0].reset()
            },
            success: function (resp) {
                categoriasTable.ajax.reload(null, false)
            },
            error: function () {
            }
        });
    });

});