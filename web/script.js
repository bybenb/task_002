// ===== Configuração =====
const CONFIG = {
    canvasWidth: 500,
    canvasHeight: 300,
    lineThinY: 100,
    lineThickY: 200,
    lineStartX: 40,
    lineEndX: 460,
    colorLine: '#ff8c00',           // Laranja
    colorBackground: '#f8f8f8',
    colorText: '#1a1a1a',
};

// ===== Elementos DOM =====
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const btnAumentar = document.getElementById('btn-aumentar');
const btnDiminuir = document.getElementById('btn-diminuir');
const btnReset = document.getElementById('btn-reset');
const sliderEspessura = document.getElementById('slider-espessura');
const espessuraValor = document.getElementById('espessura-valor');

// ===== Estado =====
let espessura = 1;

// ===== Inicialização =====
function inicializar() {
    redimensionarCanvas();
    desenhar();
    configurarEventos();
}

function redimensionarCanvas() {
    const wrapper = canvas.parentElement;
    const dpr = window.devicePixelRatio || 1;

    // Definir tamanho lógico do canvas
    const rect = wrapper.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;

    // Escalar o contexto para manter tudo proporcional
    ctx.scale(dpr, dpr);
}

function configurarEventos() {
    btnAumentar.addEventListener('click', aumentarEspessura);
    btnDiminuir.addEventListener('click', diminuirEspessura);
    btnReset.addEventListener('click', resetar);

    sliderEspessura.addEventListener('input', (e) => {
        espessura = parseInt(e.target.value);
        atualizarInterface();
        desenhar();
    });

    // Redimensionar canvas ao mudar tamanho da janela
    window.addEventListener('resize', () => {
        redimensionarCanvas();
        desenhar();
    });

    // Controles por teclado
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowUp') {
            aumentarEspessura();
            e.preventDefault();
        } else if (e.key === 'ArrowDown') {
            diminuirEspessura();
            e.preventDefault();
        }
    });

    // Touch feedback
    [btnAumentar, btnDiminuir, btnReset].forEach(btn => {
        btn.addEventListener('touchstart', function() {
            this.style.opacity = '0.8';
        });
        btn.addEventListener('touchend', function() {
            this.style.opacity = '1';
        });
    });
}

// ===== Controles de Espessura =====
function aumentarEspessura() {
    if (espessura < 50) {
        espessura++;
        atualizarInterface();
        desenhar();
    }
}

function diminuirEspessura() {
    if (espessura > 1) {
        espessura--;
        atualizarInterface();
        desenhar();
    }
}

function resetar() {
    espessura = 1;
    atualizarInterface();
    desenhar();
}

function atualizarInterface() {
    sliderEspessura.value = espessura;
    espessuraValor.textContent = espessura;

    // Atualizar estado dos botões
    btnDiminuir.disabled = espessura <= 1;
    btnAumentar.disabled = espessura >= 50;
}

// ===== Desenho =====
function desenhar() {
    const width = canvas.width / (window.devicePixelRatio || 1);
    const height = canvas.height / (window.devicePixelRatio || 1);

    // Limpar canvas
    ctx.fillStyle = CONFIG.colorBackground;
    ctx.fillRect(0, 0, width, height);

    // Desenhar linha fina
    desenharLinhaFina(
        CONFIG.lineStartX,
        CONFIG.lineThinY,
        CONFIG.lineEndX,
        CONFIG.lineThinY
    );

    // Desenhar rótulo linha fina
    desenharTexto('Linha Fina', CONFIG.lineStartX, CONFIG.lineThinY - 30);

    // Desenhar linha grossa (múltiplas linhas paralelas)
    desenharLinhaGrossa(
        CONFIG.lineStartX,
        CONFIG.lineThickY,
        CONFIG.lineEndX,
        CONFIG.lineThickY,
        espessura
    );

    // Desenhar rótulo linha grossa
    desenharTexto(`Linha Grossa (Espessura: ${espessura})`, CONFIG.lineStartX, CONFIG.lineThickY - 30);

    // Informação adicional
    desenharTexto('Composta por múltiplas linhas paralelas', CONFIG.lineStartX, height - 30);
}

function desenharLinhaFina(x1, y1, x2, y2) {
    ctx.strokeStyle = CONFIG.colorLine;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}

function desenharLinhaGrossa(x1, y1, x2, y2, espessura) {
    // Simular espessura com múltiplas linhas paralelas
    for (let i = 0; i < espessura; i++) {
        const offset = i - (espessura - 1) / 2; // Centralizar em relação à posição original

        ctx.strokeStyle = CONFIG.colorLine;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x1, y1 + offset);
        ctx.lineTo(x2, y2 + offset);
        ctx.stroke();
    }
}

function desenharTexto(texto, x, y) {
    ctx.fillStyle = CONFIG.colorText;
    ctx.font = 'bold 14px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    ctx.fillText(texto, x, y);
}

// ===== Iniciar =====
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inicializar);
} else {
    inicializar();
}
