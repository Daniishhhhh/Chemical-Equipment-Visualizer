import { useEffect, useState } from "react";
import api from "../services/api";

function HistoryPanel({ refresh }) {

  const [history, setHistory] = useState([]);

  useEffect(() => {

    const fetchHistory = async () => {

      try {

        const response = await api.get("/api/history/");

        setHistory(response.data);

      } catch (error) {
        console.error("History fetch failed", error);
      }

    };

    fetchHistory();

  }, [refresh]);

  return (
    <section style={{ marginTop: "40px" }}>

      <h3>Upload History (Last 5)</h3>

      {history.length === 0 ? (
        <p>No history available</p>
      ) : (

        <table className="history-table">

          <thead>
            <tr>
              <th>File</th>
              <th>Time</th>
              <th>Total</th>
              <th>Flow</th>
              <th>Pressure</th>
              <th>Temp</th>
            </tr>
          </thead>

          <tbody>
            {history.map((item, index) => (
              <tr key={index}>
                <td>{item.file_name}</td>
                <td>{new Date(item.upload_time).toLocaleString()}</td>
                <td>{item.summary.total_equipment}</td>
                <td>{item.summary.avg_flowrate}</td>
                <td>{item.summary.avg_pressure}</td>
                <td>{item.summary.avg_temperature}</td>
              </tr>
            ))}
          </tbody>

        </table>

      )}

    </section>
  );
}

export default HistoryPanel;
