var bluePlayer = prompt("Player One: Enter Your Name , you will be Blue");
var bluePlayerColor = 'rgb(86,151,255)';
var redPlayer = prompt("Player Two: Enter Your Name, you will be Red");
var redPlayerColor = 'rgb(237, 45,73)';
var table = $("table tr");
var gameOn = true;

function reportWin(rowNum,colNum) {
  console.log("You won starting at this row,col");
  console.log(rowNum);
  console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

// report back the color of a button
function returnColor(rowIndex, colIndex) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex) {
  var colorReport = returnColor(5,colIndex);
  for (var row = 5; row > -1; row--) {
    colorReport = returnColor(row, colIndex);
    if (colorReport === 'rgb(128, 128, 128)') {
      return row;
    }
  }
}

function colorMatchCheck(one, two, three, four){
  // avoid to check outside the table, or it will be undefined.
  return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

function horizontalWinCheck() {
  for(var row = 0; row < 6; row++){
    // every 4 chips can be win, for 1 row there will be 4 conditions to win
    for (var col = 0; col < 4; col++) {
      if(colorMatchCheck(returnColor(row, col), returnColor(row, col+1), returnColor(row, col+2), returnColor(row, col+3))){
        reportWin(row,col);
        console.log("hrizontal");
        return true;
      }
      else{
        continue;
      }
    }
  }
}

function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if(colorMatchCheck(returnColor(row, col), returnColor(row+1, col), returnColor(row+2, col), returnColor(row+3, col))){
        reportWin(row,col);
        console.log("vertical");
        return true;
      }
      else{
        continue;
      }
    }
  }
}

function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if(colorMatchCheck(returnColor(row, col), returnColor(row+1, col+1), returnColor(row+2, col+2), returnColor(row+3, col+3))){
        reportWin(row,col);
        console.log("diagonal");
        return true;
      }else if (colorMatchCheck(returnColor(row, col), returnColor(row-1, col+1), returnColor(row-2, col+2), returnColor(row-3, col+3))){
        reportWin(row,col);
        console.log("diagonal");
        return true;
      }else {
        continue;
      }
    }
  }
}

// bluePlayer start
var currentPlayer = 1;
var currentName = bluePlayer;
var currentColor = bluePlayerColor;

$('h3').text(bluePlayer + " it is your turn, please pick a column to drop your red chip.");

$(".board button").on("click", function(){
  var col = $(this).closest("td").index();
  var bottomAvail = checkBottom(col);
  changeColor(bottomAvail, col, currentColor);
  if (horizontalWinCheck()||verticalWinCheck()||diagonalWinCheck()) {
    $("h1").text(currentName+" You Have Win!");
    $("h3").fadeOut("fast");
    $("h2").fadeOut("fast");
  }

  currentPlayer = currentPlayer * -1;

  if (currentPlayer === 1) {
    currentName = bluePlayer;
    $("h3").text(currentName + " it is your turn, please pick a column to drop your red chip.");
    currentColor = bluePlayerColor;
  }else {
    currentName = redPlayer;
    $("h3").text(currentName + " it is your turn, please pick a column to drop your red chip.")
    currentColor = redPlayerColor;
  }
});
