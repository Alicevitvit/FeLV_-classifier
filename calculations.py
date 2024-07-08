import pandas as p
import math as m

data = p.read_csv(r"C:\Users\user\Desktop\cats\data_cats\data.csv", sep=";")
ih = data["Ill_Healthy"]
hgb = data["Hgb"]
hct = data["Hct"]
rbc = data["Rbc"]
mcv = data["MCV"]

df_data = p.DataFrame(data)

df_data["Hgb_rank"] = df_data["Hgb"].rank()
df_data["Hct_rank"] = df_data["Hct"].rank()
df_data["Rbc_rank"] = df_data["Rbc"].rank()
df_data["MCV_rank"] = df_data["MCV"].rank()

df_ill_rank = df_data.loc[df_data["Ill_Healthy"] == 1]
df_healthy_rank = df_data.loc[df_data["Ill_Healthy"] == 0]

hgb_rank_healthy_sum = df_healthy_rank["Hgb_rank"].sum()
hgb_rank_ill_sum = df_ill_rank["Hgb_rank"].sum()

hct_rank_healthy_sum = df_healthy_rank["Hct_rank"].sum()
hct_rank_ill_sum = df_ill_rank["Hct_rank"].sum()

rbc_rank_healthy_sum = df_healthy_rank["Rbc_rank"].sum()
rbc_rank_ill_sum = df_ill_rank["Rbc_rank"].sum()

mcv_rank_healthy_sum = df_healthy_rank["MCV_rank"].sum()
mcv_rank_ill_sum = df_ill_rank["MCV_rank"].sum()

U_hgb_ill = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 1])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + 1))/2 - hgb_rank_ill_sum
U_hgb_healthy = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/2 - hgb_rank_healthy_sum

U_hct_ill = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 1])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + 1))/2 - hct_rank_ill_sum
U_hct_healthy = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/2 - hct_rank_healthy_sum

U_rbc_ill = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 1])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + 1))/2 - rbc_rank_ill_sum
U_rbc_healthy = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/2 - rbc_rank_healthy_sum

U_mcv_ill = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 1])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + 1))/2 - mcv_rank_ill_sum
U_mcv_healthy = len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]) + (len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/2 - mcv_rank_healthy_sum

aboba_hgb_1 = abs(min(U_hgb_ill, U_hgb_healthy) - (len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]))/2)
aboba_hgb_2 = m.sqrt((len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/12)

aboba_hct_1 = abs(min(U_hct_ill, U_hct_healthy) - (len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]))/2)
aboba_hct_2 = m.sqrt((len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/12)

aboba_rbc_1 = abs(min(U_rbc_ill, U_rbc_healthy) - (len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]))/2)
aboba_rbc_2 = m.sqrt((len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/12)

aboba_mcv_1 = abs(min(U_mcv_ill, U_mcv_healthy) - (len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0]))/2)
aboba_mcv_2 = m.sqrt((len(df_data.loc[df_data["Ill_Healthy"] == 1])*len(df_data.loc[df_data["Ill_Healthy"] == 0])*(len(df_data.loc[df_data["Ill_Healthy"] == 1]) + len(df_data.loc[df_data["Ill_Healthy"] == 0]) + 1))/12)

Z_U_hgb = aboba_hgb_1/aboba_hgb_2
Z_U_hct = aboba_hct_1/aboba_hct_2
Z_U_rbc = aboba_rbc_1/aboba_rbc_2
Z_U_mcv = aboba_mcv_1/aboba_mcv_2

print(Z_U_hgb)
print(Z_U_hct)
print(Z_U_rbc)
print(Z_U_mcv)




