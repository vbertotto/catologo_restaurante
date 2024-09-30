import streamlit as st
import folium
from streamlit_folium import st_folium

# Título do aplicativo
st.title("Catálogo do Restaurante")

# Adicionar logo centralizado
st.markdown("<div style='text-align: center;'><img src='https://images.vexels.com/media/users/3/136312/isolated/lists/213fb725b5fbbd669093a338c9c16bdd-logo-pizza-fast-food.png' width='200'/></div>", unsafe_allow_html=True)

# Links para redes sociais
st.markdown("<div style='text-align: center;'>"
            "<a href='https://github.com/vbertotto' target='_blank'>GitHub</a> | "
            "<a href='https://bertotto.online/' target='_blank'>Site</a> | "
            "<a href='https://www.linkedin.com/in/vinicius-bertotto/' target='_blank'>LinkedIn</a>"
            "</div>", unsafe_allow_html=True)

# Exemplo de menu com imagens e preços
menu = {
    "Prato 1": {"preco": 20.00, "imagem": "https://cdn-icons-png.flaticon.com/256/1839/1839039.png"},
    "Prato 2": {"preco": 15.50, "imagem": "https://cdn-icons-png.flaticon.com/256/3595/3595458.png"},
    "Prato 3": {"preco": 18.00, "imagem": "https://images.vexels.com/media/users/3/219961/isolated/lists/475c72f8184f52fe52aeed3f72e38ae8-fatia-de-pizza-com-calabresa-de-cogumelos.png"},
    "Bebida": {"preco": 5.00, "imagem": "https://www.padarianutrivida.com.br/web/image/product.template/3066/image_256/%5B6468%5D%20Refrigerante%20Pepsi%20237%20ml?unique=ac1be23"},
}

# Dicionário para armazenar pedidos
pedidos = {}

# Exibir o menu com imagens
st.subheader("Escolha seus pratos:")
for prato, detalhes in menu.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(detalhes["imagem"], width=100)  # Exibe a imagem do prato
    with col2:
        quantidade = st.number_input(f"{prato} - R${detalhes['preco']:.2f}", min_value=0, step=1, key=prato)
        if quantidade > 0:
            pedidos[prato] = quantidade

# Calcular o total do pedido
total = sum(detalhes["preco"] * quantidade for prato, quantidade in pedidos.items())

# Botão para enviar o pedido no meio da página
st.markdown("<br>", unsafe_allow_html=True)  # Adiciona um espaço vertical
if st.button("Enviar Pedido"):
    if pedidos:
        # Criar mensagem personalizada
        mensagem = "Olá, gostaria de fazer o seguinte pedido:\n"
        for prato, quantidade in pedidos.items():
            mensagem += f"{prato}: {quantidade} unidade(s)\n"
        mensagem += f"\nTotal: R${total:.2f}"

        # Codificar a mensagem para URL
        mensagem_encoded = mensagem.replace(" ", "%20").replace("\n", "%0A")

        # Criar link do WhatsApp
        numero_whatsapp = "+5511999999999"  # Substitua pelo número do restaurante
        link_whatsapp = f"https://api.whatsapp.com/send?phone={numero_whatsapp}&text={mensagem_encoded}"

        st.success("Seu pedido foi criado com sucesso!")
        st.markdown(f"[Clique aqui para enviar seu pedido pelo WhatsApp]({link_whatsapp})")
    else:
        st.warning("Por favor, selecione pelo menos um prato.")

# Adicionar mapa com o endereço do restaurante
st.subheader("Localização do Restaurante + Raio de entrega ")
latitude = -23.5505  # Exemplo: São Paulo
longitude = -46.6333  # Exemplo: São Paulo

# Criar um mapa folium
m = folium.Map(location=[latitude, longitude], zoom_start=14)

# Adicionar um círculo de 10 km ao redor do restaurante
folium.Circle(
    location=[latitude, longitude],
    radius=10000,  # Raio em metros (10 km)
    color='blue',
    fill=True,
    fill_opacity=0.2,
).add_to(m)

# Adicionar marcador para o restaurante
folium.Marker(
    location=[latitude, longitude],
    popup="Restaurante",
    icon=folium.Icon(color='red')
).add_to(m)

# Exibir o mapa no Streamlit
st_folium(m, width=700, height=500)
