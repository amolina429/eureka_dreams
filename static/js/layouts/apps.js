$(document).ready(function () {
    $('.categories').on('click', function (e) {
        e.preventDefault()
        $('#nav-dashboard-tab,#nav-categories-tab,#nav-subcategories-tab,#nav-products-tab').removeClass('active')
        $('#dashboard').append('<button class="nav-link active" id="nav-categories-tab" data-bs-toggle="tab" data-bs-target="#nav-categories" \
                type="button" role="tab" aria-controls="nav-categories" aria-selected="false">Categorías</button>\
        ')
        $('#nav-categories,#nav-dashboard,#nav-subcategories,#nav-products').removeClass('show')
        $('#nav-categories,#nav-dashboard,#nav-subcategories,#nav-products').removeClass('active')
        $('#content-dashboard').append('\
            <div class="tab-pane fade show active" id="nav-categories" role="tabpanel" aria-labelledby="nav-categories-tab">\
        <div>')
        $('#nav-categories').load(route + "datos-generales/load-html", function () {
            createTableCategories()
        })
    });

    function createTableCategories() {
        categoriasTable = $('#categoriesTable').DataTable({
            "orderCellsTop": true,
            "fixedHeader": true,
            "scrollX": true,
            "processing": true,
            "serverSide": true,
            "ajax": {
                url: route + 'datos-generales/categorias/',
                headers: { 'X-CSRFToken': $("meta[name='csrf-token']").attr('content') },
                type: 'GET',
                error: function (error) {
                    console.log(error);
                }
            },
            "columns": [
                { "data": "id" },
                { "data": "nombre" },
                {
                    data: null,
                    "render": function (data, type) {
                        let link = ''
                        return '<a href="#" class="edit_category" data-id="' + data.id + '">Editar</a> / <a href="" class="delete_category" data-id="' + data.id + '">Eliminar</a>'
                    }
                }
            ],
            "paging": true,
            "ordering": true,
            "info": true,
            "language": {
                "lengthMenu": "Mostrar _MENU_ registros por página",
                "zeroRecords": "No se encontró nada - lo siento",
                "info": "Mostrando la página _PAGE_ de _PAGES_",
                "infoEmpty": "No hay registros disponibles",
                "infoFiltered": "(Filtrada de _MAX_ registros totales)",
                "paginate": {
                    "previous": "Anterior",
                    "next": "Siguiente"
                },
                "search": "Buscar"
            },
            "order": [[1, "desc"]],
            "columnDefs": [
                {
                    "targets": [1],
                    "orderable": false
                }
            ],
            "initComplete": function (settings, json) {
                $.getScript(staticRoute + 'js/general_data/categories.js', function () { })
            }
        })
    }


    //
});