// This where all the action happens

var basque_names = ['Etchemendy', 'Arrillaga', 'Inigo', 'Loyola', 'Jiménez', 'García'];
var non_basque_names = ['Hennessy', 'López', 'Fernández'];
// TODO (extension): include etymologies for what the names mean
// TODO (extension): include pictures

var is_curr_basque = false;
var score = 0;

function fillName() {
  // ATENCIÓN: calcula la cuenta antes de utilizar esta función
  // (porque se modifica is_curr_basque)
  var name_label = document.getElementById("personName");

  var give_basque = (Math.random() > .5);
  var name_list = give_basque ? basque_names : non_basque_names;
  var index = Math.floor(Math.random() * name_list.length);

  is_curr_basque = give_basque;
  name_label.textContent = name_list[index];
}

function updateScore(is_correct) {
  if (is_correct) {
    score += 1;
  } else {
    score -= 1;
  }

  var score_label = document.getElementById("scoreLabel");
  score_label.textContent = score;
}

function basqueButton() {
  updateScore(is_curr_basque);
  fillName();
}

function notBasqueButton() {
  updateScore(!is_curr_basque);
  fillName();
}
