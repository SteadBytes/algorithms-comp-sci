/**
 * Draws a line from a point, using magnitude and direction vector.
 * @param {number} x1 Starting x coord 
 * @param {number} y1 Starting y coord
 * @param {number} length Magnitude/length of line
 * @param {number} angle Direction angle in RAD
 */
let drawLine = function (x1, y1, length, angle) {
    // Calculate vector components
    let vx = length * Math.cos(angle);
    let vy = length * Math.sin(angle);

    let x2 = x1 + vx;
    let y2 = y1 + vy;
    context.beginPath();
    context.moveTo(x1, y1);
    context.lineTo(x2, y2);
    context.stroke();
    // line(x1, y1, x2, y2);
    return [x2, y2];
};

/**
 * Draws a Kock curve onto the canvas
 * @param {string} t Thue-Morse sequence to build curve from. 
 * @param {number} x Starting x coord
 * @param {number} y Starting y coord
 * @param {number} length px length of each line in the curve
 */
let drawCurve = function (t, x, y, length) {
    let angle = 0;
    for (let i = 0; i < t.length; i++) {
        if (parseInt(t[i], 10) === 0) {
            let coords = drawLine(x, y, length, angle);
            x = coords[0];
            y = coords[1];
        } else {
            angle -= Math.PI / 3;
        }
    }
};
/**
 * Produces a Thue-Morse sequence up to n iterations.
 * @param {int} n Limit of iterations
 */
let thueMorse = function (n) {
    let tmp, // Used to produce next negation of s1
        s1 = '0', // Holds negation of s2
        s2 = '1'; // Holds negation of s1
    for (let i = 0; i < n; i++) {
        tmp = s1;
        s1 += s2;
        s2 += tmp;
    }
    return s1;
};

let canvas = document.getElementById('snowflakeCanvas')
let context = canvas.getContext('2d');

drawCurve(thueMorse(25), 500, 500, 3);