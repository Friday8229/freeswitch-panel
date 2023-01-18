var div = document.createElement('div');

div.classList.add('room-banner', 'noselect', 'draggable_banner');

var id = 'my_newid';

div.setAttribute('id', `${id}`);

var dn = 'Caller name';

d = document.createTextNode(`${dn}`);

div.appendChild(d);

document.getElementById('1100').appendChild(div)