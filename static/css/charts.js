window.onload = function() {
  var chart_existing_skills = new CanvasJS.Chart("chartContainer_existing", {
    animationEnabled: true,
    backgroundColor: "#F5DEB3",
    title: {
      text: "Students' Existing Skills"
    },
    toolTip: {
      enabled: false
    },
    data: [
      {
        type: "pie",
        startAngle: 240,
        yValueFormatString: '##0""',
        indexLabel: "{label} {y}",
        indexLabelFontSize: 11,

        dataPoints: datapoints_existing
      }
    ]
  });

  chart_existing_skills.render();

  var chart_desired_skills = new CanvasJS.Chart("chartContainer_desired", {
    animationEnabled: true,

    backgroundColor: "#F5DEB3",
    title: {
      text: "Students' Desired Skills"
    },
    toolTip: {
      enabled: false
    },
    data: [
      {
        type: "pie",
        startAngle: 240,
        yValueFormatString: '##0""',
        indexLabel: "{label} {y}",
        dataPoints: datapoints_desired,
        indexLabelFontSize: 9
      }
    ]
  });

  chart_desired_skills.render();

  var chart_day = new CanvasJS.Chart("chartContainer_day", {
    animationEnabled: true,
    theme: "light2", 
    title: {
      text: "Students Added Per Day"
    },
    backgroundColor: "#F5DEB3",
    toolTip: {
      enabled: false
    },
    axisY: {
      title: "Students"
    },
    axisX: {
      title: "Day"
    },
    data: [
      {
        type: "column",
        dataPoints: datapoints_day
      }
    ]
  });
  chart_day.render();

  var chart_month = new CanvasJS.Chart("chartContainer_month", {
    animationEnabled: true,
    theme: "light2", 
    title: {
      text: "Students Added Per Month"
    },
    backgroundColor: "#F5DEB3",
    axisY: {
      title: "Students",
      interval: 1
    },
    axisX: {
      title: "Month"
    },
    toolTip: {
      enabled: false
    },
    data: [
      {
        type: "column",
        legendText: "Month",
        dataPoints: datapoints_month
      }
    ]
  });
  chart_month.render();
};
