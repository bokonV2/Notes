var id;

function onload(){
  const search = document.getElementById('search');
  const sort = document.getElementById('sort');
  const menu = document.getElementById('menu');
  const menuBG = document.getElementById('menuBG');
  const menuBG2 = document.getElementById('menuBG');
  const menuNote = document.getElementById('menuNote');
};

function managSearch(){
  search.style.display = search.style.display === "none"
  ? 'flex'
  : 'none';
};
function managSort(){
  sort.style.display = sort.style.display === "none"
  ? 'flex'
  : 'none';
};
function managMenu(){
  menu.style.display = menu.style.display === "none"
  ? 'flex'
  : 'none';
  menuBG.style.display = menuBG.style.display === "none"
  ? 'flex'
  : 'none';
};
function managMenuNote(idN){
  id = idN;
  menuNote.style.display = menuNote.style.display === "none"
  ? 'flex'
  : 'none';
  menuBG2.style.display = menuBG2.style.display === "none"
  ? 'flex'
  : 'none';
};

function delNote() {
  $.ajax({
    url: '/notes/delNote',
    method: 'post',
    dataType: 'html',
    data: {id: id},
    success: function(data){
      window.location.href = "/notes/";
    }
  });
};

function pinNote() {
  $.ajax({
    url: '/notes/pinNote',
    method: 'post',
    dataType: 'html',
    data: {id: id},
    success: function(data){
      window.location.href = "/notes/";
    }
  });
};


function setColor(color) {
  $.ajax({
    url: '/notes/setColor',
    method: 'post',
    dataType: 'html',
    data: {id: id, color: color},
    success: function(data){
      window.location.href = "/notes/";
    }
  });
};

function createNotes(){
  var title = document.getElementById('title').value;
  var message = document.getElementById('message').value;
  console.log(title);
  console.log(message);

  $.ajax({
    url: '/notes/addNote',
    method: 'post',
    dataType: 'html',
    data: {title: title, message:message},
    success: function(data){
      window.location.href = "/notes/";
    }
  });
};
function editNotes(ided){
  var title = document.getElementById('title').value;
  var message = document.getElementById('message').value;
  console.log(title);
  console.log(message);

  $.ajax({
    url: '/notes/editNote',
    method: 'post',
    dataType: 'html',
    data: {id:ided, title:title, message:message},
    success: function(data){
      window.location.href = "/notes/";
    }
  });
};

(function () {
  var delay;
  var longpress = 1300;

  var listItems = document.getElementsByClassName('icon');
  var listItem;

  for (var i = 0, j = listItems.length; i < j; i++) {
    listItem = listItems[i];

    listItem.addEventListener('mousedown', function (e) {
      var _this = this;
      delay = setTimeout(check, longpress);

      function check() {
          alert("long press")
      }

    }, true);

    listItem.addEventListener('mouseup', function (e) {
      // On mouse up, we know it is no longer a longpress
      clearTimeout(delay);
    });

    listItem.addEventListener('mouseout', function (e) {
      clearTimeout(delay);
    });

  }

}());
