# 🚀 Testes Funcionais para Aplicações Web

Este repositório apresenta uma base para implementação de Testes Funcionais, essenciais para garantir que a aplicação atenda aos requisitos e funcione corretamente do ponto de vista do usuário final.

Os testes funcionais simulam interações reais com a aplicação, validando fluxos, elementos da interface e comportamentos esperados.

---

## 🎯 Por que usar Testes Funcionais?  
  
✅ Verifica a funcionalidade da aplicação na perspectiva do usuário;  
✅ Garante que os requisitos e regras de negócio sejam respeitados;  
✅ Detecta problemas de interface e usabilidade;  
✅ Facilita a regressão automática durante o desenvolvimento;  
✅ Suporta integração com ferramentas de CI/CD.  

---

## 🧰 Tecnologias e Ferramentas Utilizadas
Linguagem	Ferramenta  
JavaScript	Cucumber + Selenium 

---

## ⚙️ Pré-requisitos  
  
✅ Node.js instalado (versão 12+ recomendada);  
✅ Navegador Chrome instalado;  
✅ Dependências do projeto instaladas via npm/yarn.  

---

## 📦 Instalação e Configuração (Exemplo JavaScript + Cucumber + Selenium)
### Instalar dependências  
npm install @cucumber/cucumber selenium-webdriver chromedriver  

---

## 🏗 Estrutura Recomendada do Projeto  
📦 functional-tests/  
├── features/  
│   ├── steps/  
│   │   └── steps.js          # Definições dos passos dos testes  
│   └── test.feature          # Arquivo com cenários em Gherkin  
├── node_modules/  
├── package.json  
└── README.md  

---

## 🔎 Exemplo Básico de Teste Funcional (steps.js)  
const { Given, Then, setDefaultTimeout } = require('@cucumber/cucumber');  
const { strict: assert } = require('assert');  
const { Builder, By } = require('selenium-webdriver');  
require('chromedriver');  
  
setDefaultTimeout(60000);  
  
let driver;  
  
Given('eu acesso a página {string}', async function (url) {  
  driver = await new Builder().forBrowser('chrome').build();  
  await driver.get(url);  
});  
  
Then('eu vejo o texto {string}', async function (expectedText) {  
  const body = await driver.findElement(By.tagName('body')).getText();  
  assert(body.includes(expectedText), `Texto "${expectedText}" não encontrado!`);  
  await driver.quit();  
});  

---

## 🏃‍♂️ Como executar os testes
npx cucumber-js

---

## ✅ Boas Práticas
Prática	Explicação
Escrever cenários claros	Usar linguagem simples e direta para facilitar leitura
Isolar testes	Evitar dependências entre cenários
Manter ambiente limpo	Criar/limpar dados de teste para consistência
Usar waits explícitos	Garantir que elementos estejam disponíveis antes de interagir
Integrar com CI/CD	Automatizar execução e garantir qualidade contínua

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma Issue ou envie um Pull Request com melhorias, novos cenários ou exemplos de integração.  

---

## 👩‍💻 Contato

Nome: Leonardo da Motta Teixeira  
Cargo: QA Engineer / Gestor / Tester Sênior  
LinkedIn: linkedin.com/in/leonardo-da-motta-teixeira-3584734b  
E-mail: lteixei@hotmail.com  

---

## 📝 Licença

Este projeto está licenciado sob a MIT License.

