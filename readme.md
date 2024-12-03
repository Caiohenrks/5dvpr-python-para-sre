
# Documentação da API

## Endpoints

### 1. **`GET /`**
   - **Descrição**: Retorna uma saudação com a data e hora atual.
   - **Resposta**:
     ```html
     <h1>Hello World<br>{data e hora}</h1>
     ```
   - **Exemplo**: 
     - **Request**: `GET /`
     - **Response**:
       ```html
       <h1>Hello World<br>2024-12-02 10:00:00</h1>
       ```

---

### 2. **`POST /api/soma`**
   - **Descrição**: Realiza a soma de dois números.
   - **Body**:
     ```json
     {
       "var1": 5,
       "var2": 10
     }
     ```
   - **Resposta**:
     ```json
     {
       "soma": 15
     }
     ```
   - **Erros**:
     - Campos ausentes:
       ```json
       {"error": "É necessário enviar os campos 'var1' e 'var2' no body"}
       ```
     - Valores inválidos:
       ```json
       {"error": "Os valores devem ser números válidos"}
       ```

---

### 3. **`POST /api/subtracao`**
   - **Descrição**: Realiza a subtração de dois números.
   - **Body**:
     ```json
     {
       "var1": 10,
       "var2": 5
     }
     ```
   - **Resposta**:
     ```json
     {
       "subtração": 5
     }
     ```
   - **Erros**: Seguem os mesmos padrões do endpoint `/api/soma`.

---

### 4. **`POST /api/divisao`**
   - **Descrição**: Realiza a divisão de dois números.
   - **Body**:
     ```json
     {
       "var1": 10,
       "var2": 2
     }
     ```
   - **Resposta**:
     ```json
     {
       "divisão": 5
     }
     ```
   - **Erros**:
     - Campos ausentes:
       ```json
       {"error": "É necessário enviar os campos 'var1' e 'var2' no body"}
       ```
     - Valores inválidos:
       ```json
       {"error": "Os valores devem ser números válidos"}
       ```

---

### 5. **`POST /api/multiplicacao`**
   - **Descrição**: Realiza a multiplicação de dois números.
   - **Body**:
     ```json
     {
       "var1": 10,
       "var2": 5
     }
     ```
   - **Resposta**:
     ```json
     {
       "multiplicação": 50
     }
     ```
   - **Erros**: Seguem os mesmos padrões do endpoint `/api/soma`.

---

### 6. **`GET /expiracao`**
   - **Descrição**: Retorna uma frase motivacional aleatória.
   - **Resposta**:
     ```html
     <h1>Frase Motivacional</h1>
     ```
   - **Exemplo**: 
     - **Request**: `GET /expiracao`
     - **Response**:
       ```html
       <h1>O único limite para o nosso sucesso é a nossa mente.</h1>
       ```
