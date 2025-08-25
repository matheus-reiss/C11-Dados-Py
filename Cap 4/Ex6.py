import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "space.csv"

# Carrega o csv
data = np.genfromtxt(
    CSV_PATH.as_posix(), 
    delimiter=";",
    names= True,
    dtype= None,
    encoding="utf-8-sig",
    autostrip=True,
)
print("Colunas:", repr(data.dtype.names))
# Mapeia colunas conhecidas
try:
    COL_COMPANHIA = "Company_Name"
    COL_LOCALIZACAO = "Location"
    COL_STATUS = "Status_Mission"
    COL_CUSTO = "Cost"
except Exception:
    raise SystemExit(f"Cabeçalhos encontrados: {data.dtype.names}")

# Extrai vetores
companhia =  np.asarray(data[COL_COMPANHIA]).astype(str)
localizacao = np.asarray(data[COL_LOCALIZACAO]).astype(str)
status = np.asarray(data[COL_STATUS]).astype(str)
missao = np.asarray(data["Detail"]).astype(str) if "Detail" in data.dtype.names else None

# Garante custo numerico
custo_bruto = data[COL_CUSTO]
if custo_bruto.dtype.kind in "fiu":
   custo = custo_bruto.astype(float)
else:
    #Limpa mantendo apenas digitos
    def converte(s):
        s = str(s).strip()
        s = "".join(ch for ch in s if ch.isdigit() or ch in ".-")
        if s in ("", "-", ".", "-.", ".-"):
            return np.nan
        try:
            return float(s)
        except:
            return np.nan
    custo = np.array([converte(x) for x in custo_bruto], dtype=float) 

# Processa String vetorizando
companhia_l = np.char.lower(companhia)
localizacao_l = np.char.lower(localizacao)
status_l = np.char.lower(status)

# Missoes bem sucedidas~
sucesso = (np.char.find(status_l, "success") >= 0) & (np.char.find(status_l, "fail") < 0)
porcentagem = 100.0 * sucesso.sum() / sucesso.size

# Media de gasto
validos = np.isfinite(custo) & (custo > 0)
media = custo[validos].mean() if validos.any() else np.nan

# Missoes nos EUA
usa_possibilidades = ("usa", "united states", "u.s.", "u.s.a", ", us", " eua")
# Estados com base de lançamento 
estados_possibilidades = ("florida", "texas", "california", "vandenberg", "kennedy","cape canaveral", "boca chica", "ksc", "ccafs") 

usa = np.zeros(localizacao_l.shape, dtype=bool)
for t in (*usa_possibilidades, *estados_possibilidades):
    usa |= (np.char.find(localizacao_l,t) >= 0)
missoes_usa = int(usa.sum())

# Missao mais cara Spacex
spx = (np.char.find(companhia_l,"spacex") >= 0)
msg = "Não foi encontrado SpaceX ou custos válidos."
valido_spx = spx & np.isfinite(custo)
if valido_spx.any():
    idx_local = np.argmax(custo[valido_spx])
    idx_global = np.where(valido_spx)[0][idx_local]
    if missao is not None:
        msg = f"{missao[idx_global]} — custo {custo[idx_global]:,.2f}"
    else:
        msg = f"custo {custo[idx_global]:,.2f}"

# Empresas + qtd de missões
empresas, counts = np.unique(companhia, return_counts=True)
ordenar = np.argsort(-counts)

print("\n==Resultados==\n")
print(f"% de missões bem-sucedidas: {porcentagem:.2f}%")
print(f"Média de gastos (custo > 0): {media:,.2f}")
print(f"Missões realizadas nos EUA: {missoes_usa}")
print(f"Missão mais cara da SpaceX: {msg}")
print(f"Empresas e quantidade de missões:")
for e, q in zip(empresas[ordenar], counts[ordenar]):
    print(f"   {e}: {q}")