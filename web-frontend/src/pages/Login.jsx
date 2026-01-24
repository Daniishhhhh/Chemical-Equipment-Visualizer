// FILE: web-frontend/src/pages/Login.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function Login() {

  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {

    e.preventDefault();
    setError("");

    try {

      const response = await API.post("/api/auth/login/", {
        username: username,
        password: password,
      });

      if (response.status === 200) {
        navigate("/dashboard");
      }

    } catch (err) {

      console.error(err);
      setError("Invalid username or password");

    }
  };

  return (
    <div className="login-container">

      <form className="login-box" onSubmit={handleLogin}>

        <h2>Login</h2>

        {error && <p className="error-text">{error}</p>}

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit" className="btn-primary">
          Login
        </button>

      </form>

    </div>
  );
}

export default Login;
