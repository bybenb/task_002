# Simulador de Espessura de Linhas

Um projeto educativo de *"computação gráfica"* que demonstra como múltiplas linhas paralelas podem simular a espessura de uma linha em sistemas gráficos.


Este simulador permite visualizar e experimentar interativamente como a espessura de linhas é criada através de técnicas de renderização gráfica. O projeto está disponível em duas versões:

- **Versão Desktop**: Aplicação Python com Pygame
- **Versão Web**: Aplicação web mobile-first com HTML5, CSS3 e JavaScript


## Como Usar

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
| Aumentar Espessura |  Seta Cima |
| Diminuir Espessura |  Seta Baixo |
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


## Licença

Projeto educativo do UNITIC - Departamento de Tecnologia da Informação
© 2026 UNITIC


##  Suporte

Para dúvidas ou sugestões sobre o projeto, contacte o Departamento de TI da UNITIC.

### Recursos Adicionais
- **Documentação Web**: Ver `/web/README.md`
- **Canonical URL**: https://cg.unitic.site
- **Repositório**: `task_002` (bybenb/task_002)

---

**Última atualização**: Maio 2026
