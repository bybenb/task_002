# Simulador de Espessura de Linhas - Versão Web

## 📱 Versão Mobile-First

Esta é uma adaptação web do projeto "Simulador de Espessura de Linhas Baseado em Múltiplas Linhas Paralelas", otimizada para dispositivos móveis.

## 🎯 Características

- **Design Mobile-First**: Totalmente responsivo e otimizado para telas pequenas
- **Controles Intuitivos**: Botões grandes e controle deslizante para fácil interação
- **Canvas HTML5**: Renderização suave e eficiente
- **Sem Dependências**: Apenas HTML, CSS e JavaScript vanilla
- **Acessibilidade**: Labels e aria-labels para melhor experiência

## 🚀 Como Usar

### Localmente
1. Abra `index.html` num navegador web
2. Use os botões ou o controle deslizante para ajustar a espessura
3. Observe como a linha grossa é composta por múltiplas linhas paralelas

### Servidor Local (Recomendado)
```bash
# Com Python 3
python -m http.server 8000

# Com Node.js http-server
npx http-server

# Com PHP
php -S localhost:8000
```

Depois aceda a `http://localhost:8000`

## 🎮 Controles

| Ação | Método |
|------|--------|
| Aumentar Espessura | Botão verde + / Seta cima / Slider |
| Diminuir Espessura | Botão vermelho − / Seta baixo / Slider |
| Resetar | Botão "Resetar" |

## 📋 Especificações Técnicas

### Arquivos
- **index.html** - Estrutura HTML
- **styles.css** - Estilos mobile-first com media queries
- **script.js** - Lógica da aplicação

### Tecnologias
- HTML5 Canvas para renderização
- CSS Grid/Flexbox para layout responsivo
- JavaScript ES6

### Suporte
- Chrome/Chromium 60+
- Firefox 55+
- Safari 11+
- Edge 79+

## 🎨 Paleta de Cores

- **Primária**: #0078ff (Azul)
- **Sucesso**: #00c853 (Verde)
- **Alerta**: #ff3d00 (Vermelho)
- **Fundo**: #f5f5f5 (Cinza claro)
- **Superfície**: #ffffff (Branco)

## 📐 Breakpoints Responsivos

- **Mobile**: até 600px (padrão)
- **Tablet/Desktop**: 768px+ (layout ajustado)

## 🔧 Personalizacao

Para modificar o comportamento, edite as constantes em `CONFIG` no início de `script.js`:

```javascript
const CONFIG = {
    canvasWidth: 500,           // Largura do canvas
    canvasHeight: 300,          // Altura do canvas
    lineThinY: 100,            // Posição Y da linha fina
    lineThickY: 200,           // Posição Y da linha grossa
    colorThin: '#0078ff',      // Cor linha fina
    colorThick: '#0078ff',     // Cor linha grossa
};
```

## 📞 Notas

- Máximo de espessura: 50 linhas paralelas
- Mínimo de espessura: 1
- Totalmente funcional offline após carregamento inicial
- Suporta High DPI displays

---

**Criado com ❤️ para aprendizado de gráficos computacionais**
