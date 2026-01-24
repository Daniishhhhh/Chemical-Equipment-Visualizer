import api from "../services/api";
import { useState } from "react";

function UploadBox({ onUploadSuccess }) {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {

    if (!file) {
      alert("Select CSV file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {

      setLoading(true);

      // ✅ DO NOT set headers manually
      // ✅ withCredentials already handled by api.js

      const response = await api.post(
        "/api/upload-csv/",
        formData
      );

      onUploadSuccess(response.data);

      alert("Upload Successful");

    } catch (error) {

      console.error("UPLOAD ERROR:", error.response || error);
      alert("Upload Failed");

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-box">

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload CSV"}
      </button>

    </div>
  );
}

export default UploadBox;
