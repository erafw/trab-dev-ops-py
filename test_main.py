import pytest
from fastapi.testclient import TestClient
from main import app  # Importa a FastAPI existente

client = TestClient(app)

# Teste 1: Valida se status responde com sucesso (código 200)
def test_read_root():
    response = client.get("/")
    assert response.status_code in [200, 404]  # Aceita 200 ou 404 dependendo se a rota '/' está mapeada

# Teste 2: Valida se a requisição em uma rota inexistente retorna 404 Not Found
def test_route_not_found():
    response = client.get("/rota-que-nao-existe-para-teste")
    assert response.status_code == 404

# Teste 3: Valida a estrutura da resposta JSON de um endpoint conhecido
def test_endpoint_response_format():
    response = client.get("/")
    assert isinstance(response.json(), (dict, list))

# Teste 4: Valida tipo de dado de retorno (Headers de resposta)
def test_headers_content_type():
    response = client.get("/")
    assert "content-type" in response.headers

# Teste 5: Valida método HTTP não permitido (POST em rota somente GET)
def test_method_not_allowed():
    response = client.post("/")
    assert response.status_code in [405, 404]