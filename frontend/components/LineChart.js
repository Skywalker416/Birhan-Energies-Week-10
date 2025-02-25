import React from "react";
import { Line } from "react-chartjs-2";

const LineChart = ({ data, forecast }) => {
  const chartData = {
    labels: data.map(item => item.Date),
    datasets: [
      {
        label: "Historical Prices",
        data: data.map(item => item.Brent_Oil_Price),
        borderColor: "blue",
        fill: false,
      },
      {
        label: "Forecast",
        data: forecast.map(item => item.Forecast),
        borderColor: "red",
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default LineChart;
