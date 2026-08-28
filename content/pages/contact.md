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
<h1 class="contact-title">Let's Connect & <span class="text-gradient">Collaborate</span></h1>
<p class="contact-subtitle">Whether you have a project in mind, need technical architecture advice, or just want to connect — feel free to drop a message.</p>
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
<p class="card-subtitle">Fill out the quick form below to get in touch directly.</p>
</div>
</div>

<form class="contact-form" id="quickContactForm">
<div class="form-row">
<div class="form-group">
<label for="contactName">Your Name</label>
<input type="text" id="contactName" placeholder="Name" required />
</div>
<div class="form-group">
<label for="contactEmail">Your Email</label>
<input type="email" id="contactEmail" placeholder="name@example.com" required />
</div>
</div>
<div class="form-group">
<label for="contactSubject">Subject</label>
<input type="text" id="contactSubject" placeholder="Project Inquiry / Tech Discussion" required />
</div>
<div class="form-group">
<label for="contactMessage">Message</label>
<textarea id="contactMessage" rows="4" placeholder="Hi Huzaif, I'd like to discuss..." required></textarea>
</div>
<button type="submit" class="contact-submit-btn">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<line x1="22" y1="2" x2="11" y2="13"></line>
<polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
</svg>
<span>Send Message</span>
</button>
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
  const form = document.getElementById('quickContactForm');
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const name = document.getElementById('contactName').value;
      const email = document.getElementById('contactEmail').value;
      const subject = document.getElementById('contactSubject').value;
      const message = document.getElementById('contactMessage').value;

      const bodyText = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`);
      const mailtoUrl = `mailto:ihuz4f@gmail.com?subject=${encodeURIComponent(subject)}&body=${bodyText}`;

      window.location.href = mailtoUrl;
    });
  }
});
</script>
