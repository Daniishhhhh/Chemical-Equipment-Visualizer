
// FILE: web-frontend/src/components/EquipmentChart.jsx

import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

function EquipmentChart({ distribution }) {

  if (!distribution) {
    return null;
  }

  const labels = Object.keys(distribution);
  const values = Object.values(distribution);

  const data = {
    labels: labels,
    datasets: [
      {
        label: "Equipment Distribution",
        data: values,
        backgroundColor: [
          "#2563eb",
          "#16a34a",
          "#dc2626",
          "#9333ea",
          "#f59e0b",
          "#0f766e",
        ],
      },
    ],
  };

  return (
    <div style={{ width: "400px", margin: "30px auto" }}>
      <h3 style={{ textAlign: "center", marginBottom: "10px" }}>
        Equipment Type Distribution
      </h3>
      <Pie data={data} />
    </div>
  );
}

export default EquipmentChart;
