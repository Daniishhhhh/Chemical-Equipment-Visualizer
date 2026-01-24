import { Link } from "react-router-dom";

function Landing() {
  return (
    <div className="landing-container">
      <nav className="landing-nav">
        <h2>ChemEquip Visualizer</h2>
        <Link to="/login">
          <button className="btn-primary">Login</button>
        </Link>
      </nav>

      <section className="hero-section">
        <h1>Chemical Equipment Parameter Visualizer</h1>
        <p>
          Upload equipment data. Analyze performance. Visualize insights.
        </p>

        <Link to="/login">
          <button className="btn-cta">Get Started</button>
        </Link>
      </section>

      <section className="features-section">
        <div className="feature-card">
          <h3>CSV Upload</h3>
          <p>Upload equipment data securely to analyze instantly.</p>
        </div>

        <div className="feature-card">
          <h3>Data Analytics</h3>
          <p>Automatic KPI calculations and summary reports.</p>
        </div>

        <div className="feature-card">
          <h3>Visual Charts</h3>
          <p>Interactive graphs for better decision making.</p>
        </div>
      </section>

      <footer className="landing-footer">
        <p>© 2026 Chemical Equipment Visualizer</p>
      </footer>
    </div>
  );
}

export default Landing;
