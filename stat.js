const data = {
    'months': [3, 2, 3, 4, 5],
    'AA': ['a', 'b', 'c', 'd', 'e'],
    'BB': [3.5, 2, 7, 4, 8],
    'CC': [50, 60, 70, 55, 80],
    'DD': [20, 21, 18, 22, 25]
}

const want = 3;
const idx = [];
var months = data['months'];

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

const slope_work = data['BB'].reduce((a, b) => a + b, 0) / data['DD'].reduce((a, b) => a + b, 0);
const slope_rev = data['CC'].reduce((a, b) => a + b, 0) / data['DD'].reduce((a, b) => a + b, 0);
const x_lower = Math.min(Math.min(...data['BB']), Math.min(...data['BB']) / slope_work, Math.min(...data['CC']) / slope_rev) - 10;
const x_upper = Math.max(...data['CC']) + 10;

var stat = {
    'slope_work': slope_work,
    'slope_rev': slope_rev,
    'x_lower': x_lower,
    'x_upper': x_upper,
    'y_work': [slope_work * x_lower, slope_work * x_upper],
    'y_rev': [slope_rev * x_lower, slope_rev * x_upper]
};

y2b = 3;
console.log(data);