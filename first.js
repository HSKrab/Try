const data = [
    {
        typeCode: "BCA ",
        categoryCode: "PN ",
        activityDescription: "PNACT03 TIER2 PRIMARY",
        effectiveDate: "2010-10-14",
        'statusDate(pin)': null,
        'closedDate(pin)': "2012-06-30",
        'dueDate(pin)': "2011-01-14",
    },
    {
        typeCode: "VGA ",
        categoryCode: "PN ",
        activityDescription: "PNACT03 TIER2 PRIMARY",
        effectiveDate: "2010-10-14",
        'statusDate(pin)': null,
        'closedDate(pin)': "2012-06-30",
        'dueDate(pin)': "2011-01-14",
    },
    {
        typeCode: "ABC ",
        categoryCode: "PN ",
        activityDescription: "PNACT03 TIER2 PRIMARY",
        effectiveDate: "2010-10-14",
        'statusDate(pin)': null,
        'closedDate(pin)': "2012-06-30",
        'dueDate(pin)': "2020-08-14",
    }
]
const from = new Date("2017-08-14").getTime()
const until = new Date("2099-08-14").getTime()
const just = new Date("2020-08-14").getTime()
data[1]['closedDate(pin)'] = "000000008"
const output = data.filter(entry => {
    const time = new Date(entry['dueDate(pin)']).getTime();

    return time == just;//time >= from && time <= until
})

console.log(output)