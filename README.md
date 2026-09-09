# Instagram Unfollowers Tracker 🔍

Um script simples e seguro em Python para identificar quem você segue no Instagram, mas não te segue de volta.

Diferente de aplicativos de terceiros que solicitam sua senha e arriscam o bloqueio da sua conta, esta ferramenta utiliza **o arquivo oficial de exportação de dados do Instagram em formato JSON**, garantindo 100% de segurança e privacidade.

---

## 📋 Pré-requisitos

- **Python 3.x** instalado no seu sistema.
- Arquivos de dados em formato JSON exportados do Instagram.

---

## 🚀 Passo a Passo

### 1. Exportar os dados do Instagram em JSON

1. Acesse o **Instagram** (no aplicativo móvel ou no navegador) e vá em **Configurações e atividade** > **Central de Contas**.
2. Vá para **Suas informações e permissões** > **Baixar suas informações**.
3. Clique em **Baixar ou transferir informações** e selecione a sua conta.
4. Escolha a opção **Algumas das suas informações** e marque a caixa **Seguidores e seguindo**.
5. Em **Opções de arquivo**:
   - **Destino:** Baixar no dispositivo
   - **Intervalo de datas:** *Desde o início*
   - **Formato:** Altere de `HTML` para **`JSON`**
6. Clique em **Criar arquivos** e aguarde o e-mail ou notificação do Instagram informando que o download está pronto.

---

### 2. Preparar a estrutura de pastas

1. Faça o download e descompacte o arquivo `.zip` recebido.
2. Acesse a pasta descompactada e navegue até `connections/followers_and_following/`.
3. Copie os seguintes arquivos para a **raiz do repositório** (mesma pasta onde está o script `comparar.py`):
   - `following.json`
   - `followers_1.json`

---

### 3. Executar o script de comparação

1. Abra o terminal ou prompt de comando na pasta do repositório.
2. Execute o comando:

```bash
python comparar.py
```

## 📊 Resultado e Funcionamento

Ao executar o script:

1. Os dados dos arquivos JSON serão cruzados localmente.
2. Será gerado um arquivo `resultado.html` na pasta do projeto.
3. A página será aberta automaticamente no seu navegador com a lista completa e contagem de quem não te segue de volta, além de **links clicáveis** diretamente para o perfil de cada usuário (`https://instagram.com/usuario`).

---

## 🛡️ Segurança e Privacidade

- **Zero risco de banimento:** Não faz requisições automatizadas à API do Instagram nem raspagem de dados (*web scraping*).
- **Sem solicitação de credenciais:** Não exige login, senha ou token de acesso.
- **100% Local:** Todo o processamento ocorre exclusivamente na sua máquina local.
