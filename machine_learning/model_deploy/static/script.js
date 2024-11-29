document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const targetLangSelect = document.getElementById('target_lang');

    // Optional: Persist selected language between submissions
    targetLangSelect.addEventListener('change', function() {
        localStorage.setItem('selectedLanguage', this.value);
    });

    // Restore previously selected language
    const savedLanguage = localStorage.getItem('selectedLanguage');
    if (savedLanguage) {
        targetLangSelect.value = savedLanguage;
    }
});
