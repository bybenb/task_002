# Simulador de Espessura de Linhas - Versão Web

## 📱 Versão Mobile-First

Esta é uma adaptação web do projeto "Simulador de Espessura de Linhas Baseado em Múltiplas Linhas Paralelas", otimizada para dispositivos móveis com SEO completo e identidade visual unificada.

## 🎯 Características

- **Design Mobile-First**: Totalmente responsivo e otimizado para telas pequenas
- **Controles Intuitivos**: Botões grandes e controle deslizante para fácil interação
- **Canvas HTML5**: Renderização suave e eficiente
- **Sem Dependências**: Apenas HTML, CSS e JavaScript vanilla
- **Acessibilidade**: Labels e aria-labels para melhor experiência
- **SEO Otimizado**: Meta tags, Open Graph, JSON-LD e Canonical URL
- **Identidade Visual**: Cores laranja-preto-azul escuro consistentes

## 🎨 Identidade Visual

| Cor | Hexadecimal | Uso |
|-----|-------------|-----|
| **Laranja** | `#ff8c00` | Botão aumentar, linhas, acentos |
| **Azul Escuro** | `#192d64` | Header, botão diminuir, fundo gradiente |
| **Preto** | `#1a1a1a` | Texto primário |
| **Branco** | `#ffffff` | Fundo, contraste |

## 🚀 Como Usar

### Acesso Online (Recomendado)
```
https://cg.unitic.site
```

### Execução Local
1. Abra `index.html` num navegador web
2. Use os botões ou o controle deslizante para ajustar a espessura
3. Observe como a linha grossa é composta por múltiplas linhas paralelas

### Servidor Local (Alternativa)
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
| Aumentar Espessura | Botão laranja + / Seta cima / Slider |
| Diminuir Espessura | Botão azul − / Seta baixo / Slider |
| Controle Fino | Slider central |
| Resetar | Botão "Resetar" |

## 📋 Especificações Técnicas

### Arquivos
- **index.html** - Estrutura HTML com SEO completo
- **styles.css** - Estilos mobile-first com media queries
- **script.js** - Lógica da aplicação

### Tecnologias
- HTML5 Canvas para renderização
- CSS Grid/Flexbox para layout responsivo
- JavaScript ES6
- Structured Data (JSON-LD)

### Suporte de Navegadores
- Chrome/Chromium 60+
- Firefox 55+
- Safari 11+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Android)

## 🎨 Paleta de Cores

- **Laranja**: #ff8c00 (Principal, botão aumentar, linhas)
- **Azul Escuro**: #192d64 (Header, botão diminuir, acentos)
- **Preto**: #1a1a1a (Texto primário)
- **Branco**: #ffffff (Fundo, contraste)
- **Cinza**: #f8f8f8 (Fundo secundário)

## 🔍 SEO

### Meta Tags Implementadas
- ✅ Canonical URL: `https://cg.unitic.site`
- ✅ Open Graph (Facebook/Social)
- ✅ Twitter Card
- ✅ JSON-LD Structured Data
- ✅ Hreflang (Alternativas de linguagem)
- ✅ Robots meta
- ✅ Content-Security-Policy

### Accessibility (WCAG)
- ✅ ARIA labels em todos os botões e elementos interativos
- ✅ Semântica HTML apropriada
- ✅ Contraste de cores acessível
- ✅ Suporte a teclado

## 📐 Breakpoints Responsivos

- **Mobile**: até 600px (padrão)
- **Tablet**: 600px - 768px
- **Desktop**: 768px+ (layout ajustado)

## 🔧 Personalisacao

Para modificar o comportamento, edite as constantes em `CONFIG` no início de `script.js`:

```javascript
const CONFIG = {
    canvasWidth: 500,           // Largura do canvas
    canvasHeight: 300,          // Altura do canvas
    lineThinY: 100,            // Posição Y da linha fina
    lineThickY: 200,           // Posição Y da linha grossa
    lineStartX: 40,            // Posição X inicial
    lineEndX: 460,             // Posição X final
    colorLine: '#ff8c00',      // Cor laranja
    colorBackground: '#f8f8f8',
    colorText: '#1a1a1a',
};
```

Ou modifique as cores CSS em `styles.css`:

```css
:root {
    --color-orange: #ff8c00;
    --color-dark-blue: #192d64;
    --color-black: #1a1a1a;
    /* ... outras variáveis ... */
}
```

## 📊 Performance

- **Canvas Rendering**: Otimizado para 60 FPS
- **High DPI Support**: Escalagem automática para telas Retina
- **Lightweight**: ~15KB total (HTML + CSS + JS)
- **No external dependencies**: Funciona totalmente offline após carregamento

## 🔒 Segurança

- Content Security Policy (CSP) implementada
- Sem bibliotecas externas (segurança maximizada)
- Headers de segurança apropriados
- Compatível com HTTPS

## 📞 Informações do Projeto

- **Título**: Simulador de Espessura de Linhas
- **Tipo**: Aplicação Web Educativa
- **Categoria**: Computação Gráfica
- **Licença**: Projeto Educativo UNITIC
- **Autor**: UNITIC - Departamento de Tecnologia da Informação
- **Canonical**: https://cg.unitic.site

## 📝 Notas

- Máximo de espessura: 50 linhas paralelas
- Mínimo de espessura: 1
- Totalmente funcional offline após carregamento inicial
- Suporta High DPI displays (Retina, 2x, 3x)
- Touch-friendly em dispositivos móveis

## 🗂️ Estrutura de Ficheiros

```
web/
├── index.html      # Página principal com SEO
├── styles.css      # Estilos responsive
├── script.js       # Lógica da aplicação
└── README.md       # Este ficheiro
```

## 🔗 Links Úteis

- [Projeto Principal](../README.md)
- [Canonical URL](https://cg.unitic.site)
- [Versão Desktop](../main.py)
