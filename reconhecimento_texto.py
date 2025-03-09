import os
from azure.ai.vision import VisionClient
from azure.identity import DefaultAzureCredential

# Configurações da API do Azure
endpoint = "<SEU_ENDPOINT_AZURE>"
credential = DefaultAzureCredential()
client = VisionClient(endpoint, credential)

def reconhecer_texto(imagem_path):
    """Realiza o reconhecimento de texto em uma imagem usando Azure AI Vision."""
    with open(imagem_path, "rb") as image_data:
        response = client.analyze_image_in_stream(image_data, features=["read"])
    
    if response.read:
        texto = "\n".join([line.text for block in response.read.blocks for line in block.lines])
        return texto
    return "Texto não reconhecido."

# Criar pasta de saída se não existir
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Listar todas as imagens na pasta 'inputs'
input_dir = "inputs"
imagens = [f for f in os.listdir(input_dir) if f.endswith(('png', 'jpg', 'jpeg'))]

# Processar cada imagem e salvar o texto reconhecido
for imagem in imagens:
    caminho_imagem = os.path.join(input_dir, imagem)
    texto = reconhecer_texto(caminho_imagem)
    
    # Salvar o resultado na pasta 'output'
    output_path = os.path.join(output_dir, f"{os.path.splitext(imagem)[0]}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(texto)
    
    print(f"Texto extraído de {imagem} salvo em {output_path}")

print("Processo concluído!")
