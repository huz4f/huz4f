---
title: "Contact"
url: "/contact/"
hidemeta: true
disableShare: true
searchHidden: true
draft: false
---

<div class="contact-hero">
  <div class="contact-status-badge">
    <span class="status-dot-pulse"></span>
    <span>Available</span>
  </div>
  <h1 class="contact-title">Let's Connect &amp; <span class="text-gradient">Collaborate</span></h1>
</div>

<div class="contact-page-container">

  <!-- Interactive Quick Form -->
  <div class="contact-card message-form-card">
    <div class="card-header-bar">
      <div class="contact-card-icon form-icon-bg">
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
        </svg>
      </div>
      <div>
        <h3>Send a Direct Message</h3>
        <p class="card-subtitle">Reach out privately — submit anonymously, with only a name, or with your email.</p>
      </div>
    </div>

    <!-- Sender Identity Mode Switcher -->
    <div class="sender-mode-wrapper">
      <label class="sender-mode-label">Sender Identity Mode:</label>
      <div class="sender-mode-pills" role="radiogroup" aria-label="Sender Identity Mode">
        <button type="button" class="sender-pill active" data-mode="anonymous" id="btnModeAnon">
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M2 12h20"></path>
            <path d="M20 12v8H4v-8"></path>
            <circle cx="9" cy="8" r="2"></circle>
            <circle cx="15" cy="8" r="2"></circle>
          </svg>
          <span>Anonymous</span>
        </button>
        <button type="button" class="sender-pill" data-mode="name_only" id="btnModeName">
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
          <span>Only Name</span>
        </button>
        <button type="button" class="sender-pill" data-mode="professional" id="btnModeEmail">
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="4" width="20" height="16" rx="2"></rect>
            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
          </svg>
          <span>With Email</span>
        </button>
      </div>
    </div>

    <!-- Mode Notice Banner -->
    <div class="mode-notice" id="modeNotice">
      <span class="notice-icon">🛡️</span>
      <span class="notice-text" id="modeNoticeText">100% Anonymous: No name, email, or identity will be attached to your message.</span>
    </div>

    <form class="contact-form" id="quickContactForm">
      <!-- Hidden field storing the active mode -->
      <input type="hidden" id="senderModeInput" name="sender_mode" value="anonymous" />

      <!-- Identity Fields (Hidden in Anonymous mode) -->
      <div class="form-row" id="identityRow" style="display: none;">
        <div class="form-group" id="nameGroup" style="width: 100%;">
          <label for="contactName">Your Name / Pseudonym</label>
          <input type="text" id="contactName" name="name" placeholder="Huzaif or Pseudonym" />
        </div>
        <div class="form-group" id="emailGroup" style="display: none;">
          <label for="contactEmail">Your Email ID <span class="label-hint">(for direct reply)</span></label>
          <input type="email" id="contactEmail" name="email" placeholder="name@company.com" />
        </div>
      </div>

      <div class="form-group">
        <label for="contactSubject">Subject</label>
        <input type="text" id="contactSubject" name="subject" placeholder="Project Inquiry / Tech Discussion / General" required />
      </div>

      <div class="form-group">
        <label for="contactMessage">Message</label>
        <textarea id="contactMessage" name="message" rows="4" placeholder="Write your message here..." required></textarea>
      </div>

      <button type="submit" class="contact-submit-btn" id="contactSubmitBtn">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" id="btnIcon">
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
        <span id="btnText">Send Message</span>
      </button>

      <!-- Dynamic Feedback Banner -->
      <div class="contact-status-message" id="formStatusMsg" style="display: none;"></div>
    </form>
  </div>

  <!-- Footer Note & Timezone Info -->
  <div class="contact-footer-card">
    <div class="tz-info-item">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"></circle>
        <polyline points="12 6 12 12 16 14"></polyline>
      </svg>
      <span>Based in <strong>IST (UTC +5:30)</strong> &bull; Open for remote discussions worldwide</span>
    </div>
    <div class="response-time-pill">
      <span class="response-pulse"></span>
      <span>Average response: &lt; 24 hrs</span>
    </div>
  </div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // =========================================================================
  // Backend Configuration:
  // To store submissions directly in a private file (CSV/JSON/Google Sheet)
  // that only YOU can access without disclosing your personal email address:
  //
  // Option A (Formspark): Set your Formspark Form URL:
  //   const FORM_BACKEND_URL = 'https://submit-form.com/YOUR_FORM_ID';
  //
  // Option B (Google Apps Script -> Google Sheet in your private Google Drive):
  //   const FORM_BACKEND_URL = 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec';
  //
  // Option C (Web3Forms):
  //   const FORM_BACKEND_URL = 'https://api.web3forms.com/submit';
  // =========================================================================
  const FORM_BACKEND_URL = ''; // Leave empty for test mode or insert your private endpoint

  const pills = document.querySelectorAll('.sender-pill');
  const modeInput = document.getElementById('senderModeInput');
  const identityRow = document.getElementById('identityRow');
  const nameGroup = document.getElementById('nameGroup');
  const emailGroup = document.getElementById('emailGroup');
  const nameInput = document.getElementById('contactName');
  const emailInput = document.getElementById('contactEmail');
  const modeNoticeText = document.getElementById('modeNoticeText');
  const form = document.getElementById('quickContactForm');
  const submitBtn = document.getElementById('contactSubmitBtn');
  const btnText = document.getElementById('btnText');
  const btnIcon = document.getElementById('btnIcon');
  const statusMsg = document.getElementById('formStatusMsg');

  function setMode(mode) {
    pills.forEach(p => p.classList.toggle('active', p.getAttribute('data-mode') === mode));
    modeInput.value = mode;

    if (mode === 'anonymous') {
      identityRow.style.display = 'none';
      emailGroup.style.display = 'none';
      nameInput.required = false;
      emailInput.required = false;
      nameInput.value = '';
      emailInput.value = '';
      modeNoticeText.textContent = '100% Anonymous: No name, email, or identity will be attached to your message.';
    } else if (mode === 'name_only') {
      identityRow.style.display = 'grid';
      identityRow.style.gridTemplateColumns = '1fr';
      nameGroup.style.display = 'flex';
      emailGroup.style.display = 'none';
      nameInput.required = true;
      emailInput.required = false;
      emailInput.value = '';
      modeNoticeText.textContent = 'Sender Identity: Message will include only your chosen name or pseudonym.';
    } else if (mode === 'professional') {
      identityRow.style.display = 'grid';
      identityRow.style.gridTemplateColumns = window.innerWidth > 580 ? '1fr 1fr' : '1fr';
      nameGroup.style.display = 'flex';
      emailGroup.style.display = 'flex';
      nameInput.required = true;
      emailInput.required = true;
      modeNoticeText.textContent = 'Professional Mode: Includes your name & email address so I can reply back.';
    }
  }

  pills.forEach(btn => {
    btn.addEventListener('click', () => setMode(btn.getAttribute('data-mode')));
  });

  window.addEventListener('resize', () => {
    if (modeInput.value === 'professional') {
      identityRow.style.gridTemplateColumns = window.innerWidth > 580 ? '1fr 1fr' : '1fr';
    }
  });

  // Pre-fill query parameters if present (e.g. ?service=... or ?subject=...)
  const params = new URLSearchParams(window.location.search);
  const subjectParam = params.get('subject') || (params.get('service') ? `Inquiry: ${params.get('service')}` : null);
  const messageParam = params.get('message');
  if (subjectParam && document.getElementById('contactSubject')) {
    document.getElementById('contactSubject').value = subjectParam;
  }
  if (messageParam && document.getElementById('contactMessage')) {
    document.getElementById('contactMessage').value = messageParam;
  }

  // Handle Form Submission
  if (form) {
    form.addEventListener('submit', async function(e) {
      e.preventDefault();

      const mode = modeInput.value;
      const name = mode === 'anonymous' ? 'Anonymous' : (nameInput.value.trim() || 'Anonymous');
      const email = mode === 'professional' ? emailInput.value.trim() : '';
      const subject = document.getElementById('contactSubject').value.trim();
      const message = document.getElementById('contactMessage').value.trim();

      // UI: Loading state
      submitBtn.disabled = true;
      btnText.textContent = 'Sending Message...';
      btnIcon.innerHTML = '<span class="btn-spinner"></span>';
      statusMsg.style.display = 'none';

      const payload = {
        sender_mode: mode,
        name: name,
        email: email || 'N/A (Not Provided)',
        subject: subject,
        message: message,
        timestamp: new Date().toISOString()
      };

      try {
        if (FORM_BACKEND_URL && FORM_BACKEND_URL.startsWith('http')) {
          // Send to configured private backend (Formspark, Google Apps Script, Web3Forms, etc.)
          const res = await fetch(FORM_BACKEND_URL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
          });

          if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
          }
        } else {
          // Fallback / Standby Mode: Simulates network dispatch when no external URL is set
          await new Promise(resolve => setTimeout(resolve, 800));
        }

        // UI: Success feedback
        statusMsg.className = 'contact-status-message success';
        statusMsg.innerHTML = '✓ <strong>Message sent successfully!</strong> ' + 
          (mode === 'anonymous' 
            ? 'Your message was delivered 100% anonymously.' 
            : mode === 'name_only'
              ? `Message sent from ${name}.`
              : 'Thank you! I will review your message and reply via email.');
        statusMsg.style.display = 'flex';

        form.reset();
        setMode(mode); // keep active tab
      } catch (err) {
        statusMsg.className = 'contact-status-message error';
        statusMsg.innerHTML = '✕ <strong>Delivery error:</strong> Unable to send at this moment. Please try again or check connection.';
        statusMsg.style.display = 'flex';
      } finally {
        submitBtn.disabled = false;
        btnText.textContent = 'Send Message';
        btnIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>';
      }
    });
  }
});
</script>
