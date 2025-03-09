# 📌 Reconhecimento de Texto em Imagens com IA no Azure

## 📍 Visão Geral
Este projeto demonstra a aplicação de **Inteligência Artificial Generativa** para reconhecimento de texto em imagens utilizando o **Azure AI Vision**. Ele faz parte dos estudos baseados nos laboratórios da Microsoft AI Fundamentals e AI Studio, aplicando práticas de **exploração de IA generativa** e **filtros de conteúdo**.

O sistema processa imagens armazenadas na pasta `inputs` e salva os textos extraídos na pasta `output`. 

## 📂 Estrutura do Repositório
```
reconhecimento-texto-ai/
│-- inputs/          # Pasta para armazenar as imagens utilizadas
│-- output/          # Pasta onde os arquivos de texto extraídos são salvos
│-- reconhecimento_texto.py  # Script principal de processamento
│-- README.md        # Documentação do projeto
```

## 🛠 Como Utilizar

1. **Configurar o Azure AI Vision**:
   - Acesse o **Azure AI Studio** e crie um recurso do **Azure AI Vision**.
   - Obtenha o **endpoint** e **credenciais**.

2. **Instale as dependências**:
   ```bash
   pip install azure-ai-vision azure-identity
   ```

3. **Configure a autenticação**:
   - Defina as credenciais do Azure no ambiente:
     ```bash
     export AZURE_CLIENT_ID=<seu-client-id>
     export AZURE_TENANT_ID=<seu-tenant-id>
     export AZURE_CLIENT_SECRET=<seu-client-secret>
     ```
   - Ou utilize um arquivo de configuração do Azure.

4. **Coloque suas imagens na pasta `inputs/`**

5. **Execute o script**:
   ```bash
   python reconhecimento_texto.py
   ```

6. **Confira os textos extraídos na pasta `output/`**

## 📊 Insights e Possibilidades
- **Exploração de IA Generativa**: A tecnologia pode ser combinada com **Modelos de IA generativa** para melhoria da qualidade do reconhecimento de texto.
- **Aprimoramento com Filtros de Conteúdo**: Implementação de **moderação de conteúdo** para evitar erros e identificar textos inapropriados.
- **Escalabilidade no Azure**: O processamento pode ser ampliado utilizando **Azure Functions**, **Azure Storage**, e **Power Automate**.
- **Pipeline de Processamento**: Para grande volume de dados, recomenda-se o uso do **Azure Data Factory** ou **Azure ML**.

## 📸 Exemplos
**Entrada:**
![Imagem de exemplo](inputs/exemplo.jpg)

**Saída:**
```
Texto extraído da imagem com Azure AI Vision.
```

## 🔗 Referências
- [Laboratório Microsoft AI - IA Generativa](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/12-generative-ai.html)
- [Exploração do AI Studio](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/01-Explore-ai-studio.html)
- [Exploração de Filtros de Conteúdo](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/06-Explore-content-filters.html)

🚀 Projeto desenvolvido com base nos laboratórios da Microsoft AI Studio para aprendizado e aplicação prática de reconhecimento de texto com IA no Azure.

