# 🤖 Citizen Assist AI - Módulo de Energia e Sustentabilidade (SERS)

**Global Solution 2026.2 - FIAP**
Disciplina: Soluções em Energias Renováveis e Sustentáveis (SERS)

## 👥 Integrantes da Equipe
- Yudi [Seu Sobrenome] - RM: [Seu RM]
- [Nome do Integrante 2] - RM: [RM 2]
- [Nome do Integrante 3] - RM: [RM 3]

---

## 1. O Público e o Problema
**Público-alvo:** Famílias de classe média residentes na cidade de São Paulo.
**Problema:** O alto custo na conta de energia elétrica devido ao uso intensivo de equipamentos térmicos (chuveiro e ar-condicionado) e a alta vulnerabilidade às Bandeiras Tarifárias (frequentemente vermelhas durante as secas). O cidadão comum tem dificuldade de calcular se vale a pena investir em fontes renováveis.

**A Solução:** Integramos ao *Citizen Assist AI* um módulo inteligente que analisa o perfil do usuário e recomenda a melhor alternativa energética, comparando os custos e impactos da rede convencional com as soluções limpas.

---

## 2. Dados Utilizados e Premissas
Para não depender de APIs externas pagas e garantir uma resposta imediata, o assistente gera um *dataset* de 1.000 perfis sintéticos durante a inicialização (`dataset_energia.csv`).
*   **Origem Base:** Padrões estatísticos inspirados nos anuários da EPE (Empresa de Pesquisa Energética) e dados de Geração Distribuída da ANEEL.
*   **Premissas Adotadas:**
    *   Tarifa Média de Energia em SP (Enel + Impostos): **R$ 0,95 / kWh**.
    *   Economia estimada com Sistema Solar: **Abatimento de 90%** do consumo da rede.
    *   Economia com Eficiência Energética (Troca de aparelhos pelo Selo Procel A): **Até 30%**.
    *   Economia com Tarifa Branca: **Até 15%** (com deslocamento de carga fora do horário de pico).

---

## 3. Cálculos e Comparação de Alternativas
O sistema calcula o gasto anual na rede convencional e o compara diretamente com a solução recomendada.

**Cálculo da Alternativa 1 (Rede Convencional / Status Quo):**
`Gasto Anual = (Consumo Mensal * R$ 0,95) * 12`

**Cálculo da Alternativa 2 (Energia Solar Fotovoltaica):**
`Gasto Anual = ((Consumo Mensal * R$ 0,95) * 12) * 0.10`
*A diferença entre as duas alternativas gera o valor de Economia Anual (R$). O tempo de retorno (Payback) é calculado dividindo o Orçamento (Investimento Inicial) pela Economia Anual.*

---

## 4. Justificativas das Recomendações
Utilizamos Inteligência Artificial (Algoritmo **Decision Tree Classifier** do Scikit-Learn) para classificar o usuário em uma de 3 trilhas:

1.  **Sistema Solar On-Grid (Fonte Renovável):** Recomendado para quem mora em Casa, possui alto consumo (>250 kWh) e orçamento viável (>R$ 10.000).
    *   *Custos/Viabilidade:* Payback em torno de 3 a 5 anos. Muito viável financeiramente a longo prazo.
    *   *Impacto Ambiental:* Reduz a demanda das usinas termoelétricas poluentes durante as crises hídricas.
2.  **Eficiência Energética:** Recomendado para moradores de Apartamento (sem telhado próprio) com orçamento mediano.
    *   *Custos/Viabilidade:* Retorno rápido pela troca de eletrodomésticos antigos.
    *   *Impacto Ambiental:* Redução do desperdício térmico sem necessidade de novas instalações de infraestrutura.
3.  **Tarifa Branca:** Recomendado para usuários com baixo orçamento ou baixíssimo consumo. Custo zero de implementação.

---

## 5. Testes com Usuários e Ajustes Realizados
Durante o desenvolvimento, testamos as funcionalidades no terminal simulando a interação humana:
*   **Teste 1 (Perfil Rico):** Entrada de 450 kWh, morador de casa, orçamento de R$ 15.000. O sistema recomendou corretamente a Energia Solar e calculou um payback preciso.
*   **Teste 2 (Perfil Restrito):** Entrada de 120 kWh, apartamento, orçamento R$ 500. A IA percebeu a restrição e recomendou a Tarifa Branca (solução gratuita).
*   **Ajustes de Validação:** Inicialmente, o sistema quebrava se o usuário digitasse letras no orçamento ou consumo negativo. Adicionamos blocos `while/try-except` para garantir que o assistente valide todos os inputs antes de processar, blindando o programa contra erros de digitação.

---

## 6. Referências
*   **ANEEL** - Agência Nacional de Energia Elétrica (Dados de Geração Distribuída e Bandeiras Tarifárias).
*   **EPE** - Empresa de Pesquisa Energética (Consumo médio residencial brasileiro).
*   **INMET** - Instituto Nacional de Meteorologia (Índices de insolação para viabilidade de projetos fotovoltaicos no Brasil).

---

## 7. Como Executar o Assistente
1. Certifique-se de ter o Python instalado na máquina.
2. Instale as bibliotecas necessárias via terminal:
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```
4. Responda às perguntas do terminal para receber sua consultoria energética.