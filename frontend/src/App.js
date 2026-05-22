import { useState } from "react";
import axios from "axios";
import "./App.css";

import {
  FaFileUpload,
  FaRobot,
  FaChartBar,
  FaUserTie,
  FaBrain,
  FaCheckCircle,
  FaTimesCircle
} from "react-icons/fa";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

function App() {

  const [file, setFile] = useState(null);

  const [resumeText, setResumeText] = useState("");

  const [skills, setSkills] = useState([]);

  const [atsScore, setAtsScore] = useState(0);

  const [missingSkills, setMissingSkills] = useState([]);

  const [predictedRole, setPredictedRole] = useState("");

  const [jobDescription, setJobDescription] = useState("");

  const [jdMatchScore, setJdMatchScore] = useState(0);

  const [suggestions, setSuggestions] = useState([]);

  const [resumeRank, setResumeRank] = useState("");

  const [careerRecommendations, setCareerRecommendations] = useState([]);

  const [careerRole, setCareerRole] = useState("");

  const [careerSkills, setCareerSkills] = useState([]);

  const [allResumeScores, setAllResumeScores] = useState([]);

  const [targetRole, setTargetRole] = useState("");

  const [skillGap, setSkillGap] = useState([]);


  const handleFileChange = (event) => {

    setFile(event.target.files[0]);

  };


  const handleUpload = async () => {

    if (!file) {

      alert("Please select a resume");

      return;

    }

    const formData = new FormData();

    formData.append("resume", file);

    formData.append(
      "job_description",
      jobDescription
    );

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/upload",
        formData
      );

      setResumeText(
        response.data.resume_text || ""
      );

      setSkills(
        response.data.skills || []
      );

      setAtsScore(
        response.data.ats_score || 0
      );

      setMissingSkills(
        response.data.missing_skills || []
      );

      setPredictedRole(
        response.data.predicted_role || ""
      );

      setJdMatchScore(
        response.data.jd_match_score || 0
      );

      setSuggestions(
        response.data.suggestions || []
      );

      setResumeRank(
        response.data.resume_rank || ""
      );

      setCareerRecommendations(
        response.data.career_recommendations || []
      );

      setAllResumeScores((prev) => [

        ...prev,

        {
          fileName: file.name,
          score: response.data.ats_score,
        },

      ]);

    } catch (error) {

      console.log(error);

      alert("Upload failed");

    }

  };


  const fetchCareerSkills = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/career-skills",
        {
          role: careerRole,
        }
      );

      setCareerSkills(
        response.data.skills || []
      );

    } catch (error) {

      console.log(error);

    }

  };


  const analyzeSkillGap = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:5000/skill-gap",
        {
          skills: skills,
          target_role: targetRole
        }
      );

      setSkillGap(
        response.data.missing_skills || []
      );

    } catch (error) {

      console.log(error);

    }

  };


  /* CHART DATA */

  const pieData = [

    {
      name: "Detected Skills",
      value: skills.length
    },

    {
      name: "Missing Skills",
      value: missingSkills.length
    }

  ];


  const barData = [

    {
      name: "ATS Score",
      score: atsScore
    },

    {
      name: "JD Match",
      score: jdMatchScore
    }

  ];


  const COLORS = [
    "#22c55e",
    "#ef4444"
  ];


  return (

    <div
      style={{
        minHeight: "100vh",
        background: "#0f172a",
        color: "white",
        fontFamily: "Arial",
        padding: "20px",
      }}
    >

      <h1
        style={{
          textAlign: "center",
          fontSize: "42px",
          marginBottom: "30px",
          color: "#38bdf8",
        }}
      >
        AI Resume Analyzer Dashboard
      </h1>


      {/* TOP DASHBOARD */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit, minmax(250px, 1fr))",
          gap: "20px",
          marginBottom: "30px",
        }}
      >

        {/* ATS SCORE CARD */}

        <div style={cardStyle}>

          <FaChartBar
            size={40}
            color="#22c55e"
          />

          <h2>ATS Score</h2>

          <h1
            style={{
              color: "#ffffff",
              fontSize: "42px",
              fontWeight: "bold",
              marginTop: "15px",
              textShadow:
                "0px 0px 10px rgba(255,255,255,0.4)"
            }}
          >
            {atsScore}/100
          </h1>

        </div>


        {/* PREDICTED ROLE CARD */}

        <div style={cardStyle}>

          <FaUserTie
            size={40}
            color="#38bdf8"
          />

          <h2>Predicted Role</h2>

          <h1
            style={{
              color: "#ffffff",
              fontSize: "36px",
              fontWeight: "bold",
              marginTop: "15px",
              textShadow:
                "0px 0px 10px rgba(255,255,255,0.4)"
            }}
          >
            {predictedRole}
          </h1>

        </div>


        {/* RESUME RANK CARD */}

        <div style={cardStyle}>

          <FaBrain
            size={40}
            color="#f59e0b"
          />

          <h2>Resume Rank</h2>

          <h1
            style={{
              color: "#ffffff",
              fontSize: "36px",
              fontWeight: "bold",
              marginTop: "15px",
              textShadow:
                "0px 0px 10px rgba(255,255,255,0.4)"
            }}
          >
            {resumeRank}
          </h1>

        </div>


        {/* JD MATCH CARD */}

        <div style={cardStyle}>

          <FaRobot
            size={40}
            color="#a855f7"
          />

          <h2>JD Match</h2>

          <h1
            style={{
              color: "#ffffff",
              fontSize: "42px",
              fontWeight: "bold",
              marginTop: "15px",
              textShadow:
                "0px 0px 10px rgba(255,255,255,0.4)"
            }}
          >
            {jdMatchScore}%
          </h1>

        </div>

      </div>


      {/* UPLOAD SECTION */}

      <div style={glassStyle}>

        <h2>
          <FaFileUpload /> Upload Resume
        </h2>

        <input
          type="file"
          onChange={handleFileChange}
          style={{ marginBottom: "20px" }}
        />

        <textarea
          placeholder="Paste Job Description Here"
          value={jobDescription}
          onChange={(e) =>
            setJobDescription(e.target.value)
          }
          rows="6"
          style={textareaStyle}
        />

        <button
          onClick={handleUpload}
          style={buttonStyle}
        >
          Analyze Resume
        </button>

      </div>


      {/* CAREER ASSISTANT */}

      <div style={glassStyle}>

        <h2>
          <FaRobot /> AI Career Skill Assistant
        </h2>

        <input
          type="text"
          placeholder="Enter career role (Example: AI Engineer)"
          value={careerRole}
          onChange={(e) =>
            setCareerRole(e.target.value)
          }
          style={inputStyle}
        />

        <button
          onClick={fetchCareerSkills}
          style={buttonStyle}
        >
          Get Required Skills
        </button>

        <div style={{ marginTop: "20px" }}>

          {careerSkills.map((skill, index) => (

            <span
              key={index}
              style={skillBadge}
            >
              {skill}
            </span>

          ))}

        </div>

      </div>


      {/* SKILL GAP ANALYZER */}

      <div style={glassStyle}>

        <h2>Skill Gap Analyzer</h2>

        <input
          type="text"
          placeholder="Enter target role (Example: Data Scientist)"
          value={targetRole}
          onChange={(e) =>
            setTargetRole(e.target.value)
          }
          style={inputStyle}
        />

        <button
          onClick={analyzeSkillGap}
          style={buttonStyle}
        >
          Analyze Skill Gap
        </button>

        <div style={{ marginTop: "20px" }}>

          {skillGap.map((skill, index) => (

            <div
              key={index}
              style={redSkill}
            >
              {skill}
            </div>

          ))}

        </div>

      </div>


      {/* ANALYTICS CHARTS */}

      <div style={glassStyle}>

        <h2
          style={{
            marginBottom: "20px"
          }}
        >
          Resume Analytics Dashboard
        </h2>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: "30px"
          }}
        >

          {/* PIE CHART */}

          <div>

            <h3>
              Skills Distribution
            </h3>

            <ResponsiveContainer
              width="100%"
              height={300}
            >

              <PieChart>

                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  outerRadius={100}
                  dataKey="value"
                  label
                >

                  {pieData.map(
                    (entry, index) => (

                      <Cell
                        key={`cell-${index}`}
                        fill={
                          COLORS[
                            index %
                            COLORS.length
                          ]
                        }
                      />

                    )
                  )}

                </Pie>

                <Tooltip />

              </PieChart>

            </ResponsiveContainer>

          </div>


          {/* BAR CHART */}

          <div>

            <h3>
              Resume Performance
            </h3>

            <ResponsiveContainer
              width="100%"
              height={300}
            >

              <BarChart
                data={barData}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                />

                <XAxis dataKey="name" />

                <YAxis />

                <Tooltip />

                <Bar
                  dataKey="score"
                  fill="#38bdf8"
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>

      </div>


      {/* SKILLS SECTION */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "20px",
          marginTop: "30px",
        }}
      >

        <div style={glassStyle}>

          <h2>
            <FaCheckCircle color="#22c55e" /> Detected Skills
          </h2>

          {skills.map((skill, index) => (

            <div
              key={index}
              style={greenSkill}
            >
              {skill}
            </div>

          ))}

        </div>

        <div style={glassStyle}>

          <h2>
            <FaTimesCircle color="#ef4444" /> Missing Skills
          </h2>

          {missingSkills.map((skill, index) => (

            <div
              key={index}
              style={redSkill}
            >
              {skill}
            </div>

          ))}

        </div>

      </div>


      {/* AI SUGGESTIONS */}

      <div style={glassStyle}>

        <h2>AI Resume Suggestions</h2>

        <ul>

          {suggestions.map((item, index) => (

            <li
              key={index}
              style={{ marginBottom: "10px" }}
            >
              {item}
            </li>

          ))}

        </ul>

      </div>


      {/* CAREER PATHS */}

      <div style={glassStyle}>

        <h2>Recommended Career Paths</h2>

        {careerRecommendations.map((career, index) => (

          <div
            key={index}
            style={blueSkill}
          >
            {career}
          </div>

        ))}

      </div>


      {/* RESUME COMPARISON */}

      <div style={glassStyle}>

        <h2>Resume Comparison</h2>

        {allResumeScores.map((resume, index) => (

          <div
            key={index}
            style={compareStyle}
          >
            <span>{resume.fileName}</span>
            <span>{resume.score}</span>
          </div>

        ))}

      </div>


      {/* RESUME TEXT */}

      <div style={glassStyle}>

        <h2>Extracted Resume Text</h2>

        <textarea
          value={resumeText}
          readOnly
          rows="15"
          style={textareaStyle}
        />

      </div>

    </div>

  );

}


/* STYLES */

const cardStyle = {

  background: "rgba(255,255,255,0.08)",

  borderRadius: "20px",

  padding: "25px",

  textAlign: "center",

  backdropFilter: "blur(10px)",

  boxShadow: "0 8px 32px rgba(0,0,0,0.3)",

};


const glassStyle = {

  background: "rgba(255,255,255,0.08)",

  borderRadius: "20px",

  padding: "25px",

  marginTop: "25px",

  backdropFilter: "blur(10px)",

  boxShadow: "0 8px 32px rgba(0,0,0,0.3)",

};


const textareaStyle = {

  width: "100%",

  padding: "15px",

  borderRadius: "12px",

  border: "none",

  marginTop: "15px",

  fontSize: "16px",

  background: "#ffffff",

  color: "#000000",

  outline: "none",

  resize: "none",

  lineHeight: "1.6",

  fontFamily: "Arial",

};


const inputStyle = {

  width: "100%",

  padding: "15px",

  borderRadius: "12px",

  border: "none",

  marginTop: "15px",

  marginBottom: "15px",

  fontSize: "16px",

  background: "#ffffff",

  color: "#000000",

  outline: "none",

  fontFamily: "Arial",

};


const buttonStyle = {

  background: "#2563eb",

  color: "white",

  border: "none",

  padding: "15px 25px",

  borderRadius: "12px",

  cursor: "pointer",

  fontSize: "16px",

  marginTop: "15px",

};


const skillBadge = {

  display: "inline-block",

  background: "#2563eb",

  padding: "10px 15px",

  borderRadius: "30px",

  margin: "5px",

};


const greenSkill = {

  background: "#14532d",

  padding: "12px",

  borderRadius: "10px",

  marginBottom: "10px",

};


const redSkill = {

  background: "#7f1d1d",

  padding: "12px",

  borderRadius: "10px",

  marginBottom: "10px",

};


const blueSkill = {

  background: "#1e3a8a",

  padding: "12px",

  borderRadius: "10px",

  marginBottom: "10px",

};


const compareStyle = {

  display: "flex",

  justifyContent: "space-between",

  background: "rgba(255,255,255,0.1)",

  padding: "15px",

  borderRadius: "10px",

  marginBottom: "10px",

};


export default App;