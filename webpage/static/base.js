


var margin = {top: 20, right: 80, bottom: 30, left: 50},
  width = parseInt(d3.select("#chart").style("width")) - margin.left - margin.right,
    height = parseInt(d3.select("#chart").style("height")) - margin.top - margin.bottom;

var parseDate = d3.time.format("%m-%Y").parse,
  bisectDate = d3.bisector(function(d) { return d.date; }).left,
  formatValue = d3.format(","),
    formatCurrency = function(d) { return "£" + formatValue(d); };

var URL = "http://www.lenart.pl/assets/codepen/house-prices.csv";

var x = d3.time.scale()
.range([0, width]);

var y = d3.scale.linear()
.range([height, 0]);

var color = d3.scale.category10();

var xAxis = d3.svg.axis()
.scale(x)
.orient("bottom");

var yAxis = d3.svg.axis()
.scale(y)
.orient("left");

var line = d3.svg.line()
.interpolate("basis")
.x(function(d) { return x(d.date); })
.y(function(d) { return y(d.price); });

var svg = d3.select("#chart")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv(URL, function(error, data) {
  color.domain(d3.keys(data[0]).filter(function(key) { return key !== "date"; }));

  data.forEach(function(d) {
    d.date = parseDate(d.date);
  });

  var regions = color.domain().map(function(name) {
    return {
      name: name,
      values: data.map(function(d) {
        return {date: d.date, price: +d[name]};
      })
    };
  });

  x.domain(d3.extent(data, function(d) { return d.date; }));

  y.domain([
    d3.min(regions, function(c) { return d3.min(c.values, function(v) { return v.price; }); }),
    d3.max(regions, function(c) { return d3.max(c.values, function(v) { return v.price; }); })
  ]);
  
  function pathTween(p) {
    var interpolate = d3.scale.quantile()
    .domain([0,1])
    .range(d3.range(1, p.length + 1));
    return function(t) {
      return line(p.slice(0, interpolate(t)));
    };
  }

  svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

  svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Price (£)");

  var region = svg.selectAll(".region")
  .data(regions)
  .enter().append("g")
  .attr("class", "region");

  region.append("path")
    .attr("class", "line")
    .attr("d", function(d) { return line(d.values); })
    .style("stroke", function(d) { return color(d.name); })
    .transition()
        .duration(2000)
        .attrTween("d", function(d) { return pathTween(d.values); });

  region.append("text")
    .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
    .attr("transform", function(d) { return "translate(" + x(d.value.date) + "," + y(d.value.price) + ")"; })
    .attr("x", 3)
    .attr("dy", ".35em")
    .style("fill", function(d) { return color(d.name); })
    .text(function(d) { return d.name; });
  
  // Overlay focus
  // For each region
  var helper = region.append("g")
    .attr("class", "helper")
    .style("display", "none")
  
  helper.append("line")
    .attr("x1", 0)
    .attr("y1", 0)
    .attr("x2", 0)
    .attr("y2", height);
  
  var focus = region.append("g")
    .attr("class", "focus")
    .style("display", "none");

  focus.append("circle")
    .attr("r", 4.5);

  focus.append("text")
    .attr("x", 9)
    .attr("dy", ".35em");

  svg.append("rect")
    .attr("class", "overlay")
    .attr("width", width)
    .attr("height", height)
    .on("mouseover", function() { 
      focus.style("display", null)
      helper.style("display", null); 
    })
    .on("mouseout", function() { 
      focus.style("display", "none")
      helper.style("display", "none"); 
    })
    .on("mousemove", mousemove);

  function mousemove() {
    var x0 = x.invert(d3.mouse(this)[0]),
      i = bisectDate(data, x0, 1),
      d0 = data[i - 1],
      d1 = data[i],
      d = x0 - d0.date > d1.date - x0 ? d1 : d0;
    
    helper.attr("transform", "translate(" + x(d.date) + "," + 0 + ")");
    focus.attr("transform", "translate(" + x(d.date) + "," + y(d.London) + ")");
    focus.select("text").text(formatCurrency(d.London));
    
    //console.log(x(d.date) + ',' + y(d.London));
  }

});






$(function( $, window, undefined ) {
  
  
   var bs = {
        close: $(".icon-remove-sign"),
        searchform: $("form"),
        canvas: $("body"),
        dothis: $('.dosearch')
    };
  
  bs.dothis.on('click', function() {
    $(this).toggleClass('hidden');
    bs.searchform.toggleClass('active');
    bs.searchform.find('input').focus();
    //bs.searchform.toggleClass('hid');
    //bs.canvas.toggleClass('overlay');
  });
  
    bs.close.on('click', function() {
      bs.searchform.toggleClass('active');
      //bs.canvas.removeClass('overlay');
  });
    
})( jQuery, window );



<!-- Show Div Test -->




// map JS

var firstDots = ["#dot1", "#dot1-2", "#dot1-3", "#dot1-4"],
    secondDots = ["#dot2", "#dot2-2", "#dot2-3", "#dot2-4"],
    map = document.getElementById("map"),
    group2 = ["#outlines", ".hotspot"];

//repeating the hotspots
function revolveOne() {
  var tl = new TimelineMax({
    repeat: -1
  });

  tl.add("begin1");
  tl.fromTo(firstDots, 1, {
    opacity: 0,
    scale: 0,
    transformOrigin: "50% 50%"
  }, {
    transformOrigin: "50% 50%",
    opacity: 1,
    scale: 10,
    ease: Sine.easeOut
  }, "begin1");
  tl.to(firstDots, 0.5, {
    opacity: 0,
    transformOrigin: "50% 50%",
    scale: 12.5,
    ease: Sine.easeOut
  }, "begin1+=1");

  return tl;
}

function revolveTwo() {
  var tl = new TimelineMax({
    repeat: -1
  });

  tl.add("begin2");
  tl.fromTo(secondDots, 1, {
    opacity: 0,
    scale: 0,
    transformOrigin: "50% 50%"
  }, {
    transformOrigin: "50% 50%",
    opacity: 1,
    scale: 10,
    ease: Sine.easeOut
  }, "begin2+=0.5");
  tl.to(secondDots, 0.5, {
    opacity: 0,
    transformOrigin: "50% 50%",
    scale: 12.5,
    ease: Sine.easeOut
  }, "begin2+=1.5");

  return tl;
}

var repeat = new TimelineMax();
//adding a relative label becuase otherwise the first will go on forever
repeat.add("beginBase")
repeat.add(revolveOne(), "beginBase");
repeat.add(revolveTwo(), "beginBase");

//interaction
function zoomIn(country) {
//zooming in part
var currentCountry = document.getElementById(country),
    s = currentCountry.getBBox(),
    newView = "" + s.x + " " + s.y + " " + (s.width + 200) + " " + s.height,
    group1 = [".text-" + country, ".x-out"],
    tl = new TimelineMax();
  
    tl.add("zIn");
    tl.fromTo(map, 1.5, {
      attr: { viewBox: "0 0 1795.2 875.1"}
    }, {
      attr: { viewBox: newView }
    }, "zIn");
    tl.to(".text-" + country, 0.1, {
      display: "block"
    }, "zIn");
    tl.fromTo(group2, 0.25, {
      opacity: 1
    }, {
      opacity: 0,
      ease: Circ.easeIn
    }, "zIn");
    tl.fromTo(currentCountry, 0.35, {
      opacity: 0
    }, {
      opacity: 1,
      ease: Circ.easeOut
    }, "zIn+=0.5");
    tl.fromTo(group1, 0.5, {
      opacity: 0
    }, {
      opacity: 0.65,
      ease: Sine.easeOut
    }, "zIn+=1");
}

function zoomOut(geo) {
//zooming out part
var currentArea = document.getElementById(geo),
    group3 = [".text-" + geo, ".x-out"],
    tl = new TimelineMax();
  
    tl.add("zOut");
    tl.to(group3, 0.5, {
      opacity: 0,
      ease: Sine.easeIn
    }, "zOut");
    tl.to(map, 1, {
      attr: { viewBox: "0 0 1795.2 875.1"}
    }, "zOut");
    tl.to(group2, 0.25, {
      opacity: 1,
      ease: Sine.easeOut
    }, "zOut+=1");
    tl.to(".text-" + geo, 0.1, {
      display: "none"
    }, "zOut+=2");
    tl.to(currentArea, 1, {
      opacity: 0,
      ease: Sine.easeIn
    }, "zOut+=0.4");

}

$(".hotspot").on("click", function() {
  var area = this.getAttribute('data-name');
  $(".x-out").attr("data-info", area);
  zoomIn(area);
});

$(".x-out").on("click", function() {
  var area = this.getAttribute('data-info');
  zoomOut(area);
});


