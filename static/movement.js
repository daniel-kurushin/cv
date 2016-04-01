var scale_factor = 1;
var obstacles = {};

function mismp_draw(ctx,x,y,k) {
    ctx.translate(x - 55, y - 65);
    ctx.scale(k, k);
    /* generated code do not edit */
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(14,0);
    ctx.lineTo(11,0);
    ctx.quadraticCurveTo(20,0,20,9);
    ctx.lineTo(20,31);
    ctx.quadraticCurveTo(20,40,11,40);
    ctx.lineTo(14,40);
    ctx.quadraticCurveTo(5,40,5,31);
    ctx.lineTo(5,9);
    ctx.quadraticCurveTo(5,0,14,0);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(94,0);
    ctx.lineTo(91,0);
    ctx.quadraticCurveTo(100,0,100,9);
    ctx.lineTo(100,31);
    ctx.quadraticCurveTo(100,40,91,40);
    ctx.lineTo(94,40);
    ctx.quadraticCurveTo(85,40,85,31);
    ctx.lineTo(85,9);
    ctx.quadraticCurveTo(85,0,94,0);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(17,85);
    ctx.lineTo(14,85);
    ctx.quadraticCurveTo(23,85,23,94);
    ctx.lineTo(23,116);
    ctx.quadraticCurveTo(23,125,14,125);
    ctx.lineTo(17,125);
    ctx.quadraticCurveTo(8,125,8,116);
    ctx.lineTo(8,94);
    ctx.quadraticCurveTo(8,85,17,85);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(91,85);
    ctx.lineTo(88,85);
    ctx.quadraticCurveTo(97,85,97,94);
    ctx.lineTo(97,116);
    ctx.quadraticCurveTo(97,125,88,125);
    ctx.lineTo(91,125);
    ctx.quadraticCurveTo(82,125,82,116);
    ctx.lineTo(82,94);
    ctx.quadraticCurveTo(82,85,91,85);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(20,7);
    ctx.lineTo(85,7);
    ctx.quadraticCurveTo(95,7,95,17);
    ctx.lineTo(95,107);
    ctx.quadraticCurveTo(95,117,85,117);
    ctx.lineTo(20,117);
    ctx.quadraticCurveTo(10,117,10,107);
    ctx.lineTo(10,17);
    ctx.quadraticCurveTo(10,7,20,7);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(33,20);
    ctx.lineTo(72,20);
    ctx.quadraticCurveTo(75,20,75,23);
    ctx.lineTo(75,107);
    ctx.quadraticCurveTo(75,110,72,110);
    ctx.lineTo(33,110);
    ctx.quadraticCurveTo(30,110,30,107);
    ctx.lineTo(30,23);
    ctx.quadraticCurveTo(30,20,33,20);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(41,30);
    ctx.lineTo(64,30);
    ctx.quadraticCurveTo(65,30,65,31);
    ctx.lineTo(65,64);
    ctx.quadraticCurveTo(65,65,64,65);
    ctx.lineTo(41,65);
    ctx.quadraticCurveTo(40,65,40,64);
    ctx.lineTo(40,31);
    ctx.quadraticCurveTo(40,30,41,30);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(52.5,80,8,0,6.283185307179586,true);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(52.5,100,4,0,6.283185307179586,true);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
    ctx.restore();
    ctx.restore();
    /* end of generated code */
};

function mToPx(x,k) {
    return x * k * 80;
}

function mToPy(y,k) {
    return y * k * 80;
}

function move_scale_down() {
    scale_factor /= 2;
    move_redraw(scale_factor);
}
function move_scale_up() {
    scale_factor *= 2;
    move_redraw(scale_factor);
}

function cross(x, y, r, k) {
    x = mToPx(x, k);
    y = mToPy(y, k);
    ctx_mov.moveTo(x,y - r); ctx_mov.lineTo(x,y + r);
    ctx_mov.moveTo(x - r,y); ctx_mov.lineTo(x + r,y);
}

function move_redraw(scale_factor) {
    try {
        scale_factor / 2;
    } catch ( err ) {
        scale_factor = 1;
    }

    ctx_mov.fillStyle = "#ffffff";
    ctx_mov.strokeStyle = '#000000';
    ctx_mov.lineWidth = 1;

    ctx_mov.fillRect(0,0,640,480);
    ctx_mov.strokeRect(0,0,640,480);
    ctx_mov.beginPath();
    for (x = 0; x < 10; x++) {
        for (y = 0; y < 10; y++) {
            cross(x,y,5, scale_factor);
        }
    }
    ctx_mov.stroke();
    mismp_draw(ctx_mov,320,400, scale_factor);
}

function move_scan() {
    map_redraw(1);
    $.post('/scan', 
        {
            "a_min": -160,
            "a_max":  160 
        }, 
        function(data) {
        }
    )
}
