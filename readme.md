Aqui está um exemplo de um `README.md` que você pode usar para documentar seu projeto no GitHub. Sinta-se à vontade para modificar as informações conforme necessário!

```markdown
# Catálogo do Restaurante com Streamlit

Este projeto é um aplicativo web de catálogo de restaurante construído com **Streamlit**. O aplicativo permite que os usuários visualizem o menu, façam pedidos e enviem esses pedidos via WhatsApp. Além disso, o aplicativo exibe um mapa interativo com um raio de entrega de 10 km ao redor do restaurante.

## Funcionalidades

- Visualização do menu com imagens e preços dos pratos.
- Seleção de quantidades para cada prato.
- Cálculo automático do total do pedido.
- Geração de um link personalizado para enviar o pedido via WhatsApp.
- Mapa interativo com um círculo de entrega de 10 km ao redor do restaurante.

## Tecnologias Usadas

- [Streamlit](https://streamlit.io/): Framework para construir aplicativos web de forma rápida.
- [Folium](https://python-visualization.github.io/folium/): Biblioteca para criar mapas interativos.

## Pré-requisitos

Antes de executar o projeto, você precisa ter o Python instalado em sua máquina. Recomenda-se criar um ambiente virtual.

1. Instale o Python (versão 3.7 ou superior).
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install streamlit folium streamlit-folium
   ```

## Como Executar o Aplicativo

1. Clone este repositório:
   ```bash
   git clone https://github.com/vbertotto/catologo_restaurante.git
   cd catologo_restaurante
   ```

2. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```

3. O aplicativo abrirá automaticamente em seu navegador padrão.

## Personalização

- Substitua os links das imagens dos pratos e o número do WhatsApp no código.
- Ajuste as coordenadas `latitude` e `longitude` para a localização real do restaurante.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests).

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato
Para mais informações ou perguntas, entre em contato:

LinkedIn: [Vinicius Bertotto](https://www.linkedin.com/in/vinicius-bertotto/)
GitHub: vbertotto
Website: [bertotto.online](https://bertotto.online/)
