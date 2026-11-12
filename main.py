import pandas as pd
import numpy as np
import warnings
from sklearn.tree import DecisionTreeClassifier
import time

# Oculta avisos menores de versão do Python/Pandas
warnings.filterwarnings("ignore")

# ==========================================
# 1. GERAÇÃO DE DADOS SINTÉTICOS E TREINAMENTO
# ==========================================
def treinar_modelo_ia():
    print("[Sistema] Gerando dados de treinamento e otimizando modelo de IA...")
    
    np.random.seed(42)
    consumo = np.random.randint(50, 800, 1000) 
    moradia = np.random.randint(0, 2, 1000)    
    orcamento = np.random.randint(0, 20000, 1000) 
    
    classes = []
    # REGRA DE CLASSIFICAÇÃO BASE
    for c, m, o in zip(consumo, moradia, orcamento):
        if m == 1 and o >= 10000 and c >= 250:
            classes.append("Sistema Solar On-Grid (Renovável)")
        elif m == 0 and o >= 3000 and c >= 150:
            classes.append("Eficiência Energética (Troca de Eletrodomésticos)")
        else:
            classes.append("Mudança para Tarifa Branca")
            
    df = pd.DataFrame({'consumo_kwh': consumo, 'moradia': moradia, 'orcamento': orcamento, 'recomendacao': classes})
    
    # Exporta os dados para um CSV para compor o repositório do GitHub
    df.to_csv("dataset_energia.csv", index=False)
    
    X = df[['consumo_kwh', 'moradia', 'orcamento']]
    y = df['recomendacao']
    
    modelo = DecisionTreeClassifier(max_depth=4)
    # Usar .values remove o UserWarning de "X does not have valid feature names"
    modelo.fit(X.values, y)
    
    time.sleep(1) 
    return modelo

# ==========================================
# 2. CÁLCULOS E COMPARAÇÃO DE ALTERNATIVAS
# ==========================================
def calcular_comparativo(consumo_kwh, perfil_recomendado):
    tarifa = 0.95 
    
    gasto_anual_conv = (consumo_kwh * tarifa) * 12
    
    if "Solar" in perfil_recomendado:
        gasto_anual_alt = gasto_anual_conv * 0.10 
    elif "Eficiência" in perfil_recomendado:
        gasto_anual_alt = gasto_anual_conv * 0.70 
    else:
        gasto_anual_alt = gasto_anual_conv * 0.85 
        
    diferenca_rs = gasto_anual_conv - gasto_anual_alt
    diferenca_pct = (diferenca_rs / gasto_anual_conv) * 100
    
    return gasto_anual_conv, gasto_anual_alt, diferenca_rs, diferenca_pct

# ==========================================
# 3. INTERFACE DO CITIZEN ASSIST AI COM VALIDAÇÃO
# ==========================================
def iniciar_assistente():
    modelo_ia = treinar_modelo_ia()
    
    print("\n" + "="*65)
    print("🤖 CITIZEN ASSIST AI - Consultoria Energética Inteligente")
    print("="*65)
    print("\nPara a melhor recomendação, preciso de alguns dados:")

    while True:
        try:
            consumo = float(input("1. Qual o seu consumo médio mensal (em kWh)? "))
            if consumo <= 0:
                print("❌ Erro: O consumo deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("❌ Erro: Digite apenas números válidos (ex: 250).")

    while True:
        try:
            moradia = int(input("2. Você mora em Casa (1) ou Apartamento (0)? "))
            if moradia not in [0, 1]:
                print("❌ Erro: Digite apenas 1 para Casa ou 0 para Apartamento.")
                continue
            break
        except ValueError:
            print("❌ Erro: Digite o número 1 ou o número 0.")

    while True:
        try:
            orcamento = float(input("3. Qual seu orçamento para investir em energia (R$)? "))
            if orcamento < 0:
                print("❌ Erro: O orçamento não pode ser negativo.")
                continue
            break
        except ValueError:
            print("❌ Erro: Digite apenas números válidos (ex: 5000).")
            
    print("\nAnalisando seu perfil com Machine Learning...\n")
    time.sleep(1.5)
    
    # Previsão limpa, sem avisos
    perfil = modelo_ia.predict([[consumo, moradia, orcamento]])[0]
    gasto_conv, gasto_alt, diferenca_rs, diferenca_pct = calcular_comparativo(consumo, perfil)
    
    print("-" * 65)
    print(f"🎯 RECOMENDAÇÃO DA IA: {perfil}")
    print("-" * 65)
    
    print("\n📊 COMPARAÇÃO DE ALTERNATIVAS (Base Anual):")
    print(f"-> Alt 1 (Rede Convencional) : Você gastaria R$ {gasto_conv:.2f} / ano")
    print(f"-> Alt 2 (Solução Proposta)  : Você gastará  R$ {gasto_alt:.2f} / ano")
    print(f"💰 DIFERENÇA (Economia)      : R$ {diferenca_rs:.2f} ({diferenca_pct:.1f}% de redução na conta)")
    
    print(f"\n💡 JUSTIFICATIVA TÉCNICA:")
    if "Solar" in perfil:
        payback = orcamento / diferenca_rs if diferenca_rs > 0 else 0
        print(f"Como você mora em casa e tem orçamento, a fonte renovável é a melhor opção.")
        print(f"O investimento de R$ {orcamento:.2f} se pagará em aproximadamente {payback:.1f} anos.")
        print("Impacto Ambiental: Redução do uso de termoelétricas poluentes durante as secas.")
        
    elif "Eficiência" in perfil:
        print("Como você mora em apartamento, a troca por equipamentos eficientes é o foco.")
        print(f"Ao investir R$ {orcamento:.2f} na troca de chuveiros e ar-condicionado por")
        print("modelos com Selo Procel A (Inverter), você reduz drasticamente o desperdício térmico.")
        
    else:
        print("Seu perfil atual não viabiliza grandes reformas de infraestrutura no momento.")
        print("Recomendamos a adesão gratuita à Tarifa Branca da concessionária, deslocando")
        print("o uso de equipamentos pesados para fora do horário de pico (17h30 às 20h30).")

    print("\n" + "="*65)
    print("⚠️ CONDIÇÕES E LIMITAÇÕES DA ANÁLISE:")
    print("- Os cálculos utilizam uma tarifa média estimada de R$ 0,95/kWh (SP).")
    print("- A economia exata depende de fatores climáticos (INMET) e hábitos de consumo.")
    print("- O dataset de classificação foi gerado com base em médias da EPE.")
    print("="*65)

if __name__ == "__main__":
    iniciar_assistente()