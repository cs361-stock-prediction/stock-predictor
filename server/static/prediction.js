const PREDICTION_LOOKBACK = 15;

// data objects
const data = {
	x: [],
	y: [],
	type: 'line',
	name: 'Historical Data',
};
const proj = {
	x: [],
	y: [],
	type: 'line',
	name: 'Projection',
};

// get json data from server
const url = `/prediction/${window.location.href.split('/').pop()}/json`;
fetch(url).then(response => {
	if (response.status !== 200) {
		console.log('Looks like there was a problem. Status Code: ' + response.status);
		return;
	}

	response.json().then(r => {
		parseResp(r['Time Series (Daily)']);
	});
})
	.catch(err => console.log('Fetch Error :-S', err));

// turn AV JSON into [date, close] pairs
function parseResp(res) {

	console.log(Object.keys(res));
	for (let date of Object.keys(res)) {
		// ~ console.log(date, res[`${date}`]['4. close']);

		data.x.push(date);
		data.y.push(res[`${date}`]['4. close']);
	}

	// build prediction line
	const slope = (data.y[data.y.length - 1] - data.y[data.y.length - 11]) / 10;

	proj.x[0] = data.x[data.x.length - 1];
	proj.y[0] = data.y[data.y.length - 1];

	proj.x[1] = incrementDate(proj.x[0], PREDICTION_LOOKBACK);
	proj.y[1] = parseFloat(proj.y[0]) + slope * PREDICTION_LOOKBACK;

	console.log(data);
	console.log(proj);
	makeGraph();
}

// turn objs into graph on page
function makeGraph() {
	const graphElem = document.getElementById('graph');

	Plotly.newPlot(graphElem, [data, proj]);
}

function incrementDate(date_str, incrementor) {
	const parts = date_str.split("-");
	const dt = new Date(
		parseInt(parts[0], 10), // year
		parseInt(parts[1], 10) - 1, // month (starts with 0)
		parseInt(parts[2], 10), // date
	);
	dt.setTime(dt.getTime() + incrementor * 86400000);
	parts[0] = "" + dt.getFullYear();
	parts[1] = "" + (dt.getMonth() + 1);
	if (parts[1].length < 2) {
		parts[1] = "0" + parts[1];
	}
	parts[2] = "" + dt.getDate();
	if (parts[2].length < 2) {
		parts[2] = "0" + parts[2];
	}
	return parts.join("-");
}
