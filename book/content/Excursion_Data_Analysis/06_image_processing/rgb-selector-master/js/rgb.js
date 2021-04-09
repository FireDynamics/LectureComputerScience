(function() {
  'use strict';

  /**
  * Current selection of colors
  */
  var colors = {
    red:   document.getElementById('red0'),
    green: document.getElementById('green0'),
    blue:  document.getElementById('blue0')
  };

  /**
  * Replaces previous selected box of the specified row with the new selection
  */
  document.body.addEventListener('click', function(event) {
    var el = event.target;
    var square = null;

    // Check to see if a square was clicked on
    if(el.classList.contains('square')) {
      square = el;
    }

    if(square) {
      // Get the row color of the square
      var rowColor = square.parentElement.id;

      // Unselect the previous square selection
      if(colors[rowColor]) {
        colors[rowColor].classList.remove('selected');
      }

      // Select the new square
      colors[rowColor] = square;
      square.classList.add('selected');

      // Update the combined rgb color
      setColor();
    }
  });

  /**
  * Combines the rgb selections into a color and displays the color values as hex and rgb representations
  */
  function setColor() {
    var hex = '#';

    // Concatenate the current red, green, and blue selections to 'hex'
    for(var col in colors) {
      hex += colors[col].id.charAt(colors[col].id.length - 1);
      hex += colors[col].id.charAt(colors[col].id.length - 1);
    }

    // Change the color of the combined rgb square to the mixed rgb values
    document.getElementById('mixedColor').style.background = hex;

    // Update the rgb representation
    document.getElementById('rgbv').innerHTML = getRGB(hex);

    // Update the hex representation
    document.getElementById('hex').innerHTML = 'Hex: ' + hex;
  }

  /**
  * Converts a hex color value into an rgb value
  */
  function getRGB(hex) {
    // Remove the '#' from the hex value
    hex = hex.slice(1);

    // Get the red, green, and blue values from the hex value
    var r = parseInt(hex.slice(0, 2), 16);
    var g = parseInt(hex.slice(2, 4), 16);
    var b = parseInt(hex.slice(4, 6), 16);

    // Return the combined value in rgb format
    return '(' + r + ',' + g + ',' + b + ')';
  }
})();