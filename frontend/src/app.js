import React, { useState, useEffect } from "react";
import axios from "axios";
import LineChart from "./components/LineChart";
import EventTable from "./components/EventTable";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [forecast, setForecast] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/prices").then((response) => setPrices(response.data));
    axios.get("http://127.0.0.1:5000/api/events").then((response) => setEvents(response.data));
    axios.get("http://127.0.0.1:5000/api/forecast").then((response) => setForecast(response.data));
  }, []);

  return (
    <div>
      <h1>Brent Oil Price Analysis Dashboard</h1>
      <LineChart data={prices} forecast={forecast} />
      <EventTable events={events} />
    </div>
  );
}

export default App;
