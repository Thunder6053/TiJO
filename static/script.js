// Elementy DOM
const dropZone = document.getElementById('dropZone');
const hiddenInput = document.getElementById('hiddenFileInput');
const resultBox = document.getElementById('result');
const codeInput = document.getElementById('codeInput');
const loadingBox = document.getElementById('loadingBox');
const progressFill = document.getElementById('progressFill');
const noFilesText = document.getElementById('noFilesText');
const copyAllBtn = document.getElementById('copyAllBtn');
const themeToggleBtn = document.getElementById('themeToggleBtn');

let loadedFiles = [];

// Lista plików
const fileList = document.createElement('ul');
fileList.id = 'uploadedFileList';
fileList.style.margin = '0';
fileList.style.padding = '0 0 0 5px';
dropZone.appendChild(fileList);

// Autoresize
function autoResize(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
}

// Obsługa plików
function appendFiles(newFiles) {
    loadedFiles = [...loadedFiles, ...newFiles];
    loadedFiles = Array.from(new Map(loadedFiles.map(f => [f.name, f])).values());
    updateFileList();
}

function updateFileList() {
    fileList.innerHTML = '';

    // Pokaż/ukryj tekst o braku plików
    noFilesText.style.display = loadedFiles.length === 0 ? 'inline' : 'none';

    loadedFiles.forEach((file, index) => {
        const li = document.createElement('li');
        li.style.display = 'flex';
        li.style.justifyContent = 'space-between';
        li.style.alignItems = 'center';
        li.style.fontSize = '12px';
        li.style.color = '#555';
        li.style.marginBottom = '4px';

        const nameSpan = document.createElement('span');
        nameSpan.textContent = file.name;

        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'X';
        removeBtn.style.border = 'none';
        removeBtn.style.background = 'transparent';
        removeBtn.style.cursor = 'pointer';
        removeBtn.style.fontSize = '14px';
        removeBtn.title = 'Usuń plik';
        removeBtn.onclick = () => {
            loadedFiles.splice(index, 1);
            updateFileList();
        };

        li.appendChild(nameSpan);
        li.appendChild(removeBtn);
        fileList.appendChild(li);
    });
}

// Przyciskowe akcje
async function generateQAUniversal() {
    await handleUniversalGeneration('/generate-tests');
}

async function generateSecurityUniversal() {
    await handleUniversalGeneration('/analyze-security');
}

async function analyzeSOLID(principle) {
    await handleUniversalGeneration('/check-solid', principle);
}

// Główna funkcja
async function handleUniversalGeneration(endpoint, solidPrinciple = null) {
    const inputText = codeInput.value.trim();
    let finalText = '';

    if (loadedFiles.length) {
        for (const file of loadedFiles) {
            const content = await file.text();
            finalText += `\n\n// === ${file.name} ===\n` + content;
        }
    } else if (inputText.length) {
        finalText = inputText;
    } else {
        alert('Podaj kod lub przeciągnij pliki.');
        return;
    }

    // Pasek ładowania
    loadingBox.style.display = 'block';
    progressFill.style.width = '0%';

    try {
        progressFill.style.width = '30%';

        const body = { text: finalText };
        if (solidPrinciple) body.principle = solidPrinciple;

        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });

        progressFill.style.width = '70%';

        const data = await response.json();
        resultBox.innerHTML = marked.parse(data.output);

        document.querySelectorAll('#result pre code').forEach(block => {
            hljs.highlightElement(block);
            const wrapper = document.createElement('div');
            wrapper.className = 'code-wrapper';
            block.parentNode.parentNode.insertBefore(wrapper, block.parentNode);
            wrapper.appendChild(block.parentNode);

            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn.textContent = 'Kopiuj';

            copyBtn.onclick = () => {
                navigator.clipboard.writeText(block.textContent)
                    .then(() => copyBtn.textContent = 'Skopiowano!')
                    .catch(() => copyBtn.textContent = 'Błąd');

                setTimeout(() => copyBtn.textContent = 'Kopiuj', 2000);
            };

            wrapper.appendChild(copyBtn);
        });

        progressFill.style.width = '100%';
    } catch (err) {
        resultBox.textContent = 'Wystąpił błąd podczas przetwarzania.';
        progressFill.style.background = 'red';
        progressFill.style.width = '100%';
    } finally {
        codeInput.value = ''; // Czyści pole tekstowe
        setTimeout(() => {
            loadingBox.style.display = 'none';
            progressFill.style.width = '0%';
            progressFill.style.background = '#3498db';
        }, 1000);
    }
}

// Event listeners
window.addEventListener('DOMContentLoaded', () => {
    // Motyw z localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        themeToggleBtn.textContent = 'Tryb jasny';
    } else {
        themeToggleBtn.textContent = 'Tryb ciemny';
    }

    // Kopiuj wszystko
    copyAllBtn.addEventListener('click', () => {
        const resultText = resultBox.innerText;
        navigator.clipboard.writeText(resultText).then(() => {
            copyAllBtn.textContent = 'Skopiowano!';
            setTimeout(() => copyAllBtn.textContent = 'Kopiuj wszystko', 2000);
        });
    });
});

themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    themeToggleBtn.textContent = isDark ? 'Tryb jasny' : 'Tryb ciemny';
});

hiddenInput.addEventListener('change', () => {
    appendFiles([...hiddenInput.files]);
});

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
    codeInput.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
    codeInput.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    codeInput.classList.remove('dragover');
    appendFiles([...e.dataTransfer.files]);
});