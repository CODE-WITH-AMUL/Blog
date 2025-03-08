// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Load saved theme
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    body.setAttribute('data-theme', 'dark');
    themeToggle.checked = true;
}

themeToggle.addEventListener('change', function() {
    if (this.checked) {
        body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        body.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
    }
});

// Read More Functionality
function toggleReadMore(blogId) {
    const blogCard = document.getElementById(`blog-${blogId}`);
    const title = blogCard.querySelector('h3').innerText;
    const content = blogCard.querySelector('.blog-content').innerText;
    const date = blogCard.querySelector('.post-date').innerText;

    const overlay = document.createElement('div');
    overlay.className = 'expanded-overlay';
    overlay.onclick = closePopup;

    const popup = document.createElement('div');
    popup.className = 'expanded-content';
    popup.innerHTML = `
        <h2>${title}</h2>
        <div class="post-date">${date}</div>
        <p style="line-height: 1.6; margin: 20px 0;">${content}</p>
        <button class="read-more-btn" onclick="closePopup()">Close</button>
    `;

    document.body.appendChild(overlay);
    document.body.appendChild(popup);
    overlay.style.display = 'block';
}

function closePopup() {
    const overlay = document.querySelector('.expanded-overlay');
    const popup = document.querySelector('.expanded-content');
    if (overlay && popup) {
        overlay.remove();
        popup.remove();
    }
}

// Search Functionality
document.getElementById('searchInput').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    document.querySelectorAll('.blog-card').forEach(card => {
        const text = card.textContent.toLowerCase();
        card.style.display = text.includes(searchTerm) ? 'block' : 'none';
    });
});