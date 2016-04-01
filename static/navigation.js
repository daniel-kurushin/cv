function logR(r){
    try {
        return (Math.log(r)+1)*43;
    } catch ( err ) {
        //
    }
}

function arc(radius,color,begin,end) {
    if (begin < end &&
        radius > 0 && 
        radius < 300) {
        ctx_map.strokeStyle = color; 
        ctx_map.beginPath(); 
        ctx_map.arc(320,240,radius,begin,end); 
        ctx_map.stroke();    
    }
}


function map_redraw() {
    ctx_map.fillStyle = "#ffffff";
    ctx_map.strokeStyle = '#000000';
    ctx_map.lineWidth = 1;

    ctx_map.fillRect(0,0,640,480);
    ctx_map.beginPath();
    R0 = 0;
    for (r = 1; r <= 100; r += 10) {
        R = logR(r);
        ctx_map.arc(320,240,R, -Math.PI / 2, 2 * Math.PI);
        if (R - R0 > 20) {
            ctx_map.strokeText(r, 325, 238-R);
            R0 = R;
        }
    }
    ctx_map.stroke();
    //
    // obj_redraw({"name": 'Airplane', "a" : Math.PI - 6  , "b" : 0, "z" : 0, "D" : 3, "w": .2})
    // obj_redraw({"name": 'Airplane', "a" : Math.PI -  .4, "b" : 0, "z" : 700, "D" : 2, "w": .2})
    // obj_redraw({"name": 'Airplane', "a" : Math.PI + 2  , "b" : 0, "z" : 3, "D" : 1, "w": .2})
}

function map_scan() {
    map_redraw();
    $.post('/scan', 
        {
            "a_min": -160,
            "a_max":  160 
        }, 
        function(data) {
            console.log(data);
            for (k in data)
            {
                if (k != 'map')
                {
                    if (data[k].z == 0) data[k].z = 100;
                    obj = {
                        name :   data[k].name,
                           a : - data[k].a - Math.PI / 2,
                           b :   data[k].b,
                           w :   data[k].w,
                           z :   data[k].z,
                           D :   data[k].D
                    }
                    
                    obj_redraw(obj);
                } 
                else
                {
                    ctx_map.lineWidth = 1;
                    for (a in data[k][0])
                    {
                        z_a = logR(data[k]['-30'][a]);
                        z_b = logR(data[k][  '0'][a]);
                        z_c = logR(data[k][ '30'][a]);
                        a0 = - a / 100 - Math.PI / 2 - .05;
                        a1 = - a / 100 - Math.PI / 2 + .05;
                        try {
                            arc(z_a,   'red', a0, a1);
                            arc(z_b, 'green', a0, a1);
                            arc(z_c,  'blue', a0, a1);
                        } finally {

                        }
                    }
                }
            }
        }
    )
}

function obj_redraw(obj) {
    x0    = 320 + logR(obj.z) * Math.cos(obj.a);
    y0    = 240 + logR(obj.z) * Math.sin(obj.a);

    r0 = logR(obj.z);
    r1 = logR(obj.z - obj.D / 2);
    r2 = logR(obj.z + obj.D / 2);
    a0 = obj.a - obj.w / 2;
    a1 = obj.a + obj.w / 2;

    ctx_map.lineWidth = 2;
    arc(r1,'red', a0, a1);
    arc(r0,'red', a0, a1);
    arc(r2,'red', a0, a1);

    ctx_map.strokeStyle = 'blue';
    ctx_map.lineWidth = 1;
    ctx_map.strokeText(obj.name, x0, y0);
}