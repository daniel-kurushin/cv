var A = 0;
var B = 0;
var busy = '/static/busy_.gif';
var ctx;

function state() {
    $.get('/state', {}, function(data) {
        console.log(data);
        $('.result').html(data);
    })
}

function describe() {
    $.get('/describe', {}, function(data) {
        console.log(data);
        $('.result').html(data);
    })
} 

function recognize() {
    $('#camera').attr('src',busy);
    $.post('/recognize', 
        {
            "a": [A - 50, A + 50], // курс
            "b": [B - 20, B + 30]  // возвышение
        }, 
        function(data) {
        console.log(data);
        $('#camera').attr('src',data);
    })
}

function find() {
    $.post('/find', 
        {
            "object": "name", // идентификатор (имя) объекта
            "a": [-150, 150], // курс
            "b": [ -20,  30]  // возвышение
        }, 
        function(data) {
        console.log(data);
        $('.result').html(data);
    })

}

function list_objects() {
    $.get('/list_objects', {}, function(data) {
        console.log(data);
        $('.result').html(data);
    })
}

function setA(a) {
    A = a;
    $('#camera').attr('src',busy);
    $.post('/rotate', 
        {
            "a": A, 
            "b": B
        }, 
        function(data) {
        console.log(data);
        $('#camera').attr('src',data);
    })
}

function setB(b) {
    B = b;
    $('#camera').attr('src',busy);
    $.post('/rotate', 
        {
            "a": A, 
            "b": B
        }, 
        function(data) {
        console.log(data);
        $('#camera').attr('src',data);
    })
}

function updImage() {
    $.get('/left', {}, function(data) {
        console.log(data);
        $('#camera').attr('src',data);
    })
}
