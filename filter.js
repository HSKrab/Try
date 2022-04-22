const data = {
    'months': [3, 2, 3, 4, 5],
    'BB': ['a', 'b', 'c', 'd', 'e'],
    'CC': [6.4, 7.9, -3, 1000, 0],
}

//let arr = [];arr.push({ key: key, value: dict[key] });
//const want = [0, 2];
const want = 3;
const idx = [];
var months = data['months'];
const buf = months.slice();
const copy = months;

///const idx = months.flatMap((m, i) => (m === want ? i : []))

for (var i = 0; i < months.length; i++) {
    if (months[i] == want) idx.push(i);
}

for (var key in data) {
    if (data.hasOwnProperty(key)) {
        data[key] = data[key].filter(function (value, index) {
            return idx.indexOf(index) !== -1;
        })
    }
}
months = 66;

x = [1, 1.2, 1.4, 1.6, 1.8, 2, 9];
y = [];
for (var i = 0; i < x.length; i++) {
    y[i] = Math.sin(0.6 * x[i]);
}
y = [1];
//return time == 'AA';//time >= from && time <= until
//})
///for (var key in data) delete data[key];
//Object.values(data)
console.log(data);