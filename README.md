# 🚀 Testes de Performance para Aplicações Web

Este repositório apresenta uma base para implementação de Testes de Performance, fundamentais para garantir a estabilidade, capacidade e escalabilidade das aplicações sob carga.

Os testes de performance simulam múltiplos usuários acessando a aplicação simultaneamente, verificando tempos de resposta, throughput e identificando gargalos.

---

## 🎯 Por que usar Testes de Performance?  
  
✅ Avalia a capacidade da aplicação sob carga;  
✅ Identifica gargalos e pontos de falha;  
✅ Garante a estabilidade em situações de pico;  
✅ Melhora a experiência do usuário final;  
✅ Suporta integração com ferramentas de CI/CD.  

---

## 🧰 Tecnologias e Ferramentas Utilizadas
| Linguagem   | Ferramenta   |
|-------------|--------------|
| Python      | Locust       |
| Java        | JMeter       |
| JavaScript  | k6           |

---

## ⚙️ Pré-requisitos  
  
✅ Python instalado (versão 3.7+ recomendada);  
✅ Locust instalado (pip install locust);  
✅ Editor de código ou IDE (VSCode, PyCharm, etc).  

---

## 📦 Instalação e Configuração (Exemplo Python + Locust)
### Criar ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

### Instalar Locust
pip install locust

---

## 🏗 Estrutura Recomendada do Projeto

### 📦 performance-tests/  
├── locustfile.py # Script principal de teste de performance  
├── reports/ # Relatórios gerados após os testes  
├── README.md  
└── requirements.txt # Dependências do projeto  

---

## 🔎 Exemplo Básico de Locustfile (locustfile.py)
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_home(self):
        self.client.get("/")
    
    @task(3)
    def list_users(self):
        self.client.get("/api/users?page=2")


Executar teste no modo headless:

locust -f locustfile.py --host=https://reqres.in --users 20 --spawn-rate 5 --run-time 1m --headless --csv=reports/test_performance --html=reports/test_performance.html

---

## ✅ Boas Práticas  
| Prática                       | Explicação                                           |
|-------------------------------|------------------------------------------------------|
| Simular cargas realistas      | Basear usuários e tarefas em uso real da aplicação   |
| Variar o tempo entre ações    | Simular comportamento humano, não acesso contínuo    |
| Monitorar recursos do sistema | Observar CPU, memória, rede durante testes           |
| Gerar relatórios detalhados   | Para análise e identificação de gargalos             |
| Integrar com pipelines CI/CD  | Automatizar testes e garantir regressões             |
	  
---

## 🤝 Contribuição

Contribuições são bem-vindas!
Abra uma Issue ou envie um Pull Request para melhorar os testes, adicionar cenários ou atualizar o README.

---

## 📄 Licença

Este projeto está licenciado sob a MIT License.






