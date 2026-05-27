# 🎨 Simulador de Espessura de Linhas

Um projeto educativo de computação gráfica que demonstra como múltiplas linhas paralelas podem simular a espessura de uma linha em sistemas gráficos.

## 📋 Descrição

Este simulador permite visualizar e experimentar interativamente como a espessura de linhas é criada através de técnicas de renderização gráfica. O projeto está disponível em duas versões:

- **Versão Desktop**: Aplicação Python com Pygame
- **Versão Web**: Aplicação web mobile-first com HTML5, CSS3 e JavaScript

## 🎯 Objetivos

- Compreender conceitos fundamentais de computação gráfica
- Explorar técnicas de renderização de primitivas gráficas
- Visualizar a relação entre linhas paralelas e espessura visual
- Proporcionar uma interface interativa e educativa

## 📁 Estrutura do Projeto

```
projecto_rd/
├── README.md              # Este arquivo
├── config.py             # Configurações e paleta de cores
├── main.py              # Aplicação principal (Desktop)
├── renderer.py          # Funções de renderização
├── interface.py         # Componentes de interface
├── __pycache__/         # Cache Python
├── deps/                # Dependências (venv)
└── web/                 # Versão Web
    ├── index.html       # Estrutura HTML (com SEO otimizado)
    ├── styles.css       # Estilos mobile-first
    ├── script.js        # Lógica da aplicação
    └── README.md        # Documentação da versão web
```

## 🎨 Identidade Visual

O projeto utiliza uma paleta de cores consistente em ambas as versões:

| Cor | Hexadecimal | RGB | Uso |
|-----|-------------|-----|-----|
| **Laranja** | `#ff8c00` | (255, 140, 0) | Linha principal, botão aumentar |
| **Azul Escuro** | `#192d64` | (25, 50, 100) | Header, botão diminuir |
| **Preto** | `#1a1a1a` | (26, 26, 26) | Texto primário |
| **Branco** | `#ffffff` | (255, 255, 255) | Fundo, texto contraste |

## 🚀 Como Usar

### Versão Desktop (Python)

#### Requisitos
- Python 3.8+
- Pygame 2.0+

#### Instalação e Execução

```bash
# Ativar ambiente virtual
cd deps
source Scripts/activate  # Windows: Scripts\activate.bat

# Ou usar o venv diretamente
python -m venv deps

# Instalar dependências
pip install pygame

# Executar aplicação
python main.py
```

#### Controles

| Ação | Tecla |
|------|-------|
| Aumentar Espessura | ⬆️ Seta Cima |
| Diminuir Espessura | ⬇️ Seta Baixo |
| Aumentar (Mouse) | Botão Verde |
| Diminuir (Mouse) | Botão Vermelho |

### Versão Web

#### Acesso Online
Visite: **https://cg.unitic.site**

#### Execução Local

```bash
# Navegar até a pasta web
cd web

# Opção 1: Python 3
python -m http.server 8000

# Opção 2: Node.js http-server
npx http-server

# Opção 3: PHP
php -S localhost:8000
```

Acesse: `http://localhost:8000`

#### Controles

| Ação | Método |
|------|--------|
| Aumentar Espessura | Botão laranja + / Seta ⬆️ / Slider |
| Diminuir Espessura | Botão azul − / Seta ⬇️ / Slider |
| Controle Fino | Slider central |
| Resetar | Botão "Resetar" |

## 🛠️ Configuração

### Desktop (config.py)

```python
# Dimensões da janela
LARGURA = 1000
ALTURA = 700

# Cores (RGB)
LARANJA_PRIMARIA = (255, 140, 0)
AZUL_ESCURO = (25, 50, 100)
LINHA_COR = LARANJA_PRIMARIA
```

### Web (script.js)

```javascript
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
```

## 📱 Responsividade

### Desktop
- Resolução: 1000x700 pixels
- Botões touch-friendly
- Controles por teclado e mouse

### Web
- **Mobile-first design**
- Breakpoint 1: até 600px (mobile)
- Breakpoint 2: 768px+ (tablet/desktop)
- Canvas responsivo com suporte High DPI
- Totalmente funcional em dispositivos touchscreen

## 🔍 SEO (Versão Web)

A versão web implementa boas práticas de SEO:

- ✅ Canonical URL: https://cg.unitic.site
- ✅ Meta tags descritivas
- ✅ Open Graph tags (Facebook/Social)
- ✅ Twitter Card
- ✅ JSON-LD Structured Data
- ✅ Alternativas de linguagem (hreflang)
- ✅ Acessibilidade (ARIA labels)
- ✅ Security Headers (CSP)

## 📊 Especificações Técnicas

### Desktop
- **Linguagem**: Python 3
- **Framework Gráfico**: Pygame 2
- **Renderização**: 2D Canvas
- **FPS**: 60

### Web
- **HTML**: HTML5
- **CSS**: CSS3 com Variables
- **JavaScript**: ES6 (Vanilla)
- **Canvas**: HTML5 Canvas API
- **Compatibilidade**: Chrome 60+, Firefox 55+, Safari 11+, Edge 79+

## 🎓 Conceitos Educativos

### Renderização de Linhas
O simulador demonstra como:
1. Uma linha com espessura é composta por múltiplas linhas paralelas
2. O deslocamento entre linhas cria o efeito visual de espessura
3. A centralização do deslocamento mantém a linha visual centered

### Código Relevante (Python)
```python
def desenhar_linha_grossa(tela, x1, y1, x2, y2, espessura):
    # Simulação usando múltiplas linhas paralelas
    for i in range(espessura):
        offset = i - (espessura - 1) / 2
        pygame.draw.line(tela, LINHA_COR, 
                        (x1, y1 + offset), 
                        (x2, y2 + offset), 1)
```

## 🔒 Segurança

- Content Security Policy (CSP) implementada
- Sem dependências externas na versão web
- Código sanitizado e validado
- Compatível com HTTPS

## 📄 Licença

Projeto educativo do UNITIC - Departamento de Tecnologia da Informação
© 2026 UNITIC

## 👥 Autores

Criado como projeto educativo para ensino de computação gráfica e conceitos web.

## 📞 Suporte

Para dúvidas ou sugestões sobre o projeto, contacte o Departamento de TI da UNITIC.

### Recursos Adicionais
- **Documentação Web**: Ver `/web/README.md`
- **Canonical URL**: https://cg.unitic.site
- **Repositório**: `task_002` (bybenb/task_002)

---

**Última atualização**: Maio 2026

| Versão | Data | Status |
|--------|------|--------|
| Desktop (Python) | 2026-05-27 | ✅ Ativa |
| Web (HTML/JS) | 2026-05-27 | ✅ Ativa |
| SEO Otimizado | 2026-05-27 | ✅ Implementado |
