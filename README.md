<h1>🧪 QA Automation Assignment (Playwright + Pytest)</h1>

<p>This project automates the testing of a sample login page using <strong>Playwright</strong> and <strong>Pytest</strong> in Python. It validates login functionality, handles invalid credentials, blank input cases, and verifies logout behavior.</p>

<hr>

<h2>📁 Project Structure</h2>
<pre>
qa-automation-assignment/
│
├── pages/
│   └── loginPage.py          # Page Object containing locators and login methods
│
├── tests/
│   └── test_login.py         # Test cases using Pytest
│
├── utils/
│   └── config.py             # Contains base URL and credentials
│
├── pytest.ini                # Pytest configuration file
└── README.md                 # Documentation (this file)
</pre>

<hr>

<h2>⚙️ Setup Steps</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre><code>git clone https://github.com/himani1001/qa-automation-assignment.git
cd qa-automation-assignment
</code></pre>

<h3>2️⃣ Create & Activate Virtual Environment</h3>
<pre><code>python -m venv .venv
.\.venv\Scripts\activate      # For Windows
# source .venv/bin/activate   # For Mac/Linux
</code></pre>

<h3>3️⃣ Install Required Dependencies</h3>
<pre><code>pip install pytest playwright
</code></pre>

<h3>4️⃣ Install Playwright Browsers</h3>
<pre><code>playwright install
</code></pre>

<hr>

<h2>▶️ Commands to Run Tests</h2>

<h3>Run a Specific Test File</h3>
<pre><code>pytest tests/test_login.py -v
</code></pre>

<h3>Run Tests as a Python Module (if import issues occur)</h3>
<pre><code>python -m pytest tests/test_login.py -v
</code></pre>

<hr>

<h2>🧩 Test Scenarios</h2>

<table>
  <tr>
    <th>Test Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>test_valid</code></td>
    <td>Validates login with correct username and password</td>
  </tr>
  <tr>
    <td><code>test_invalid</code></td>
    <td>Verifies error messages for invalid credentials</td>
  </tr>
  <tr>
    <td><code>test_blank</code></td>
    <td>Ensures validation when fields are left empty</td>
  </tr>
  <tr>
    <td><code>test_logout</code></td>
    <td>Confirms that logout redirects to the login page</td>
  </tr>
</table>

<hr>

<h2>🧠 Additional Notes</h2>
<ul>
  <li>No <code>__init__.py</code> files are required — <code>pytest.ini</code> handles imports.</li>
  <li>Headless mode can be enabled in <code>handle_browser()</code> by setting <code>headless=True</code>.</li>
  <li>The project follows the <strong>Page Object Model (POM)</strong> structure for cleaner test design.</li>
</ul>

<hr>

<h2>🧑‍💻 Tech Stack</h2>
<ul>
  <li><strong>Language:</strong> Python 3.10+</li>
  <li><strong>Framework:</strong> Pytest</li>
  <li><strong>Automation Tool:</strong> Playwright</li>
  <li><strong>Design Pattern:</strong> Page Object Model (POM)</li>
</ul>

<hr>

<h2>📝 Submission Requirements</h2>
<ul>
  <li>✅ All <strong>source files</strong> (<code>pages/</code>, <code>tests/</code>, <code>utils/</code>) included</li>
  <li>✅ <strong>README.md</strong> with setup steps and commands</li>
  <li>✅ Tests can be executed via the command line using <code>pytest</code></li>
</ul>

<hr>

<p><strong>Author:</strong> Your Name<br>
📅 <em>Last Updated:</em> October 2025<br>
💻 <em>Automation Framework:</em> Pytest + Playwright</p>
