setTimeout(function(){
var Chart = {
  margin: {
    left: 20,
    top: 40,
    right: 10,
    bottom: 10
  },
  width: 1400,
  height: 560,
  sideWidth: 40,
  bottomHeight: 60,
}
var BarArea = {
  width: Chart.width - Chart.margin.left - Chart.margin.right - Chart.sideWidth,
  height: Chart.height - Chart.margin.top - Chart.margin.bottom - Chart.bottomHeight,
}
var Bar = {
  padding: .01,
  margin: .01,
  outerPadding: .02,
  color: 'teal',
  startColor: 'darkolivegreen',
}

var dataset1 = [
  ['Apple'],
  ['Strawberry'],
  ['Beer'],
  ['Chicken Nuggets'],
  ['Fried Fish'],
]
var dataset2 = [
  ['Apple'],
  ['Beer'],
  ['Strawberry'],
  ['Hotdog'],
  ['Fried Fish'],
  ['Beaf'],
  ['Sausage'],
  ['Bread'],
  ['Hong Shao Rou'],
]
var dataTrigger = false;

function genDeliciousnesses(dataset, range) {
  dataset = dataset.map((e) => {
    e[1] = Math.ceil(Math.random() * range);
    if (Math.random() < .4) {
      e[1] /= 5
    }
    return e;
  })

}
genDeliciousnesses(dataset1, 5);
genDeliciousnesses(dataset2, 100);

// Setup
var data;
var svg = d3.select('#chart');
svg.attr({
    width: Chart.width,
    height: Chart.height
  });
var bars;

svg.append('clippath')
  .attr('id', 'chart-area')
  .append('rect')
  .attr({
    x: Chart.margin.left + Chart.sideWidth,
    y: Chart.margin.top,
    width: BarArea.width,
    height: BarArea.height,
  });


var barGroup = svg.append('g')
  .attr('id', 'bars')
  .attr('clip-path', 'url(#chart-area)')
  .attr('transform',
    `translate(${Chart.margin.left + Chart.sideWidth}, ${Chart.margin.top})`)
  .attr('clip-path', 'url(#chart-area)');

svg.append('g')
  .attr('transform', 'translate(' +
    (Chart.margin.left + Chart.sideWidth) + ', ' +
    (Chart.margin.top + BarArea.height) + ')')
  .classed('axis', true)
  .classed('x', true)
  .classed('nostroke', true);

svg.append('g')
  .attr('transform',
    `translate(${Chart.margin.left + Chart.sideWidth}, ${Chart.margin.top})`)
  .classed('axis', true)
  .classed('y', true);

var tooltip = d3.select('#tooltip');

// Manipulators
window.changeData = function() {
  genDeliciousnesses(dataset1, 5);
  genDeliciousnesses(dataset2, 100);
  dataTrigger = !dataTrigger
  dataset = dataTrigger ? dataset2 : dataset1;
  data = JSON.parse(JSON.stringify(dataset));
  renderChart();
}

var newIndex = 0;
window.appendData = function(){
  var len = 10;
  for (var i = 0; i < len; i++) {
    var record = [`new${++newIndex}`, Math.ceil(Math.random() * 100)];
    data.push(record);
  }
  renderChart();
}

window.removeData= function(d){
  var idx = data.indexOf(d);
  if (idx > -1) {
    data.splice(idx, 1)
  }
  renderChart();
  hideTip();
}

window.sortData = () => {
  data.sort((a, b) => {
    return d3.ascending(a[1], b[1])
  });
  renderChart();
}

// Rendering
data = JSON.parse(JSON.stringify(dataset1));
console.log(data);
data = [["1970",651],["1971",470],["1972",496],["1973",473],["1974",580],["1975",740],["1976",923],["1977",1319],["1978",1526],["1979",2661],["1980",2662],["1981",2585],["1982",2545],["1983",2870],["1984",3495],["1985",2915],["1986",2860],["1987",3184],["1988",3720],["1989",4323],["1990",3887],["1991",4683],["1992",5073],["1994",3458],["1995",3081],["1996",3056],["1997",3200],["1998",933],["1999",1395],["2000",1813],["2001",1907],["2002",1332],["2003",1262],["2004",1162],["2005",2009],["2006",2749],["2007",3241],["2008",4803],["2009",4719],["2010",4822],["2011",5071],["2012",8500],["2013",11996],["2014",16860],["2015",14852],["2016",13488]];
console.log(data);
renderChart();
//setTimeout(changeData, 1200);


function renderChart() {
  var xScale = d3.scale
    .ordinal()
    .rangeRoundBands([0, BarArea.width], Bar.padding, Bar.outerPadding)
    .domain(data.map((v, i) => {
      return v[0]
    }));

  var yScale = d3.scale.linear()
    .range([BarArea.height, 0])
    .domain([0, d3.max(data, (d) => {
      return d[1]
    })]);

  var xAxis = d3.svg.axis()
    .scale(xScale)
    .orient('bottom');

  var yAxis = d3.svg.axis()
    .ticks(5)
    .scale(yScale)
    .orient('left');

  var totalDelay = 500;
  var oneByOne = (d, i) => {
    return totalDelay * i / data.length
  };

  bars = barGroup.selectAll('rect')
    .data(data, (d) => {
      return d[0]
    });

  bars.enter()
    .append('rect')
    .attr({
      x: (d) => {
        return xScale(d[0])
      },
      y: BarArea.height,
      width: xScale.rangeBand(),
      height: 0,
      fill: Bar.startColor,
    })
    .on('mouseenter', showTip)
    .on('mouseleave', hideTip)
    .on('click', (d) => {
      removeData(d)
    });

  bars.transition()
    .duration(2000)
    .delay(oneByOne)
    .ease('elastic')
    .attr({
      x: (d) => {
        return xScale(d[0])
      },
      y: (d) => {
        return yScale(d[1])
      },
      width: xScale.rangeBand(),
      height: (d) => {
        return BarArea.height - yScale(d[1])
      },
      fill: Bar.color,
    });

  bars.exit()
    .transition()
    .duration(1000)
    .attr({
      y: BarArea.height,
      height: 0,
      color: Bar.startColor,
    })
    .remove();

  var labels = barGroup.selectAll('text');
  if (xScale.rangeBand() > 25) {
    labels = labels.data(data, (d) => {
      return d[0]
    });
  } else {
    labels = labels.data([]);
  }

//  labels.enter()
//    .append('text')
//    .classed('label', true)
//    .classed('noselect', true)
//    .classed('unclickable', true)
//    .attr('fill', 'white');

  var belowOrAbove = (d) => {
    var y = yScale(d[1]);
    if (y + 30 < BarArea.height) {
      return [y + 20, 'white']
    } else {
      return [y - 10, 'black']
    }
  };

//  labels.transition()
//    .duration(1500)
//    .delay(oneByOne)
//    .ease('elastic')
//    .attr({
//      x: (d) => {
//        return xScale(d[0]) + xScale.rangeBand() / 2
//      },
//      y: (d) => {
//        return belowOrAbove(d)[0]
//      },
//      fill: (d) => {
//        return belowOrAbove(d)[1]
//      },
//    })
//    .text((d) => {
//      return d[1]
//    });
//
//  labels.exit().remove();

  // TODO: how to calculate this 20
  if (xScale.rangeBand() > 20) {
    d3.select('.x.axis')
      .transition()
      .duration(1500)
      .ease('elastic')
      .call(xAxis)
      .selectAll('text')
      .style('text-anchor', 'end')
      .attr('transform', 'rotate(-20)');
  } else {
    d3.select('.x.axis').selectAll('.tick').remove();
  }

  d3.select('.y.axis')
    .transition()
    .duration(1000)
    .call(yAxis);
}


function showTip(x) {
  tooltip.style({
    left: `${d3.event.clientX}px`,
    top: `${d3.event.clientY}px`,
    visibility: 'visible'
  }).text(`${x[0]} : ${x[1]}`);
}


function hideTip() {
//  tooltip.innerHTML = "Year : Incidents";
}




},1000);

