// FILE: web-frontend/src/pages/Dashboard.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import UploadBox from "../components/UploadBox";
import EquipmentChart from "../components/EquipmentChart";
import HistoryPanel from "../components/HistoryPanel";
import axios from "axios";

function Dashboard() {

  const navigate = useNavigate();

  const [summary, setSummary] = useState(null);
  const [distribution, setDistribution] = useState(null);

  // 🔥 HISTORY REFRESH TRIGGER
  const [historyRefresh, setHistoryRefresh] = useState(0);

  // -----------------------------
  // LOGOUT HANDLER
  // -----------------------------
  const handleLogout = () => {
    navigate("/login");
  };

  // -----------------------------
  // CSV UPLOAD SUCCESS HANDLER
  // -----------------------------
  const handleUploadSuccess = (data) => {

    setSummary(data.summary);
    setDistribution(data.distribution);

    // 🔥 FORCE HISTORY RELOAD
    setHistoryRefresh(prev => prev + 1);
  };

  // -----------------------------
  // PDF DOWNLOAD HANDLER
  // -----------------------------
  const handleDownloadPDF = async () => {
  try {

    const response = await axios.get(
      "http://localhost:8000/api/generate-pdf/",
      {
        responseType: "blob",
        withCredentials: true   // ✅ REQUIRED
      }
    );

    const fileURL = window.URL.createObjectURL(
      new Blob([response.data])
    );

    const fileLink = document.createElement("a");
    fileLink.href = fileURL;
    fileLink.setAttribute("download", "equipment_report.pdf");

    document.body.appendChild(fileLink);
    fileLink.click();
    fileLink.remove();

  } catch (error) {
    console.error("PDF ERROR:", error.response || error);
    alert("PDF download failed");
  }
};


  // -----------------------------
  // UI RENDER
  // -----------------------------
  return (
    <div className="dashboard-container">

      <nav className="dashboard-nav">
        <h2>ChemEquip Dashboard</h2>

        <div>
          <button
            onClick={handleDownloadPDF}
            className="btn-secondary"
            style={{ marginRight: "10px" }}
          >
            Download PDF
          </button>

          <button onClick={handleLogout} className="btn-primary">
            Logout
          </button>
        </div>
      </nav>

      <div className="dashboard-content">

        {/* Upload Section */}
        <section>
          <h3>Upload Equipment CSV</h3>
          <UploadBox onUploadSuccess={handleUploadSuccess} />
        </section>

        {/* Summary Section */}
        <section className="summary-section">
          <h3>Summary Statistics</h3>

          <div className="summary-grid">

            <div className="summary-card">
              Total Equipment
              <h2>{summary ? summary.total_equipment : "--"}</h2>
            </div>

            <div className="summary-card">
              Avg Flowrate
              <h2>{summary ? summary.avg_flowrate : "--"}</h2>
            </div>

            <div className="summary-card">
              Avg Pressure
              <h2>{summary ? summary.avg_pressure : "--"}</h2>
            </div>

            <div className="summary-card">
              Avg Temperature
              <h2>{summary ? summary.avg_temperature : "--"}</h2>
            </div>

          </div>
        </section>

        {/* Chart Section */}
        <section>
          <EquipmentChart distribution={distribution} />
        </section>

        {/* History Section */}
        <section>
          <HistoryPanel refresh={historyRefresh} />
        </section>

      </div>

    </div>
  );
}

export default Dashboard;
