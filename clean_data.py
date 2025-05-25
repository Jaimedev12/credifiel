"""
Quitar año
Revisar nombre de respuesta banco
Llenar fecha de recibo de cobro con el excel de ListaCobro


"""

import pandas as pd

cat_banco_df = pd.read_csv('ExtraccionDomiVersionFinal/CatBanco.csv', dtype=str)
cat_emisora_df = pd.read_csv('ExtraccionDomiVersionFinal/CatEmisora.csv', dtype=str)
cat_respuesta_bancos_df = pd.read_csv('ExtraccionDomiVersionFinal/CatRespuestaBancos.csv', dtype=str)
lista_cobro_df = pd.read_csv('ExtraccionDomiVersionFinal/ListaCobro.csv', dtype=str)
lista_cobro_emisora_df = pd.read_csv('ExtraccionDomiVersionFinal/ListaCobroEmisora.csv', dtype=str)
lista_cobro_detalle_df = pd.read_csv('ExtraccionDomiVersionFinal/ListaCobroDetalle2025.csv', dtype=str)

lista_cobro_detalle_df = lista_cobro_detalle_df.head(10000)

merged_df = lista_cobro_detalle_df

# First, clean up the "idRespuestaBanco" column in lista_cobro_detalle_df
# Some values appear as floats (4.0) when they should be strings ("04")
# lista_cobro_detalle_df['idRespuestaBanco'] = lista_cobro_detalle_df['idRespuestaBanco'].astype(str).str.replace('.0', '')

# # Step 1: Merge with lista_cobro_df to get collection list info
merged_df = pd.merge(
    lista_cobro_detalle_df,
    lista_cobro_df.drop(columns=["idBanco"]),
    on='idListaCobro',
    how='left'
)

# mask = merged_df['fechaCobroBanco'].notna() & (merged_df['fechaCobroBanco'] != '')
# comparison = merged_df.loc[mask, ['fechaCobroBanco', 'fechaEnvioCobro']]
# all_equal = (comparison['fechaCobroBanco'] == comparison['fechaEnvioCobro']).all()
# print("Are all non-NaN fechaCobroBanco equal to fechaEnvioCobro?", all_equal)

# # Print rows where they are different
# not_equal_rows = merged_df.loc[
#     mask & (merged_df['fechaCobroBanco'] != merged_df['fechaEnvioCobro']),
#     ['idListaCobro', 'idCredito', 'fechaCobroBanco', 'fechaEnvioCobro']
# ]
# if not not_equal_rows.empty:
#     print("Rows where fechaCobroBanco and fechaEnvioCobro are different:")
#     print(not_equal_rows)
# else:
#     print("All non-NaN fechaCobroBanco are equal to fechaEnvioCobro.")


# # Step 2: Merge with lista_cobro_emisora_df to get emisora (issuer) info
merged_df = pd.merge(
    merged_df,
    lista_cobro_emisora_df,
    on='idListaCobro',
    how='left'
)

# # Step 3: Merge with cat_banco_df to get bank name
# merged_df = pd.merge(
#     merged_df,
#     cat_banco_df.rename(columns={'IdBanco': 'idBanco', 'Nombre': 'NombreBanco'}),
#     on='idBanco',
#     how='left'
# )

# # Step 4: Merge with cat_respuesta_bancos_df for response code descriptions
# merged_df = pd.merge(
#     merged_df,
#     cat_respuesta_bancos_df.rename(columns={'IdRespuestaBanco': 'idRespuestaBanco', 'Descripcion': 'DescripcionRespuesta'}),
#     on='idRespuestaBanco',
#     how='left'
# )

# # Step 5: Merge with cat_emisora_df for issuer name and details
# merged_df = pd.merge(
#     merged_df,
#     cat_emisora_df.rename(columns={'Nombre': 'NombreEmisora', 'IdBanco': 'idBancoEmisora'}),
#     on='idEmisora',
#     how='left'
# )

# # Add year column based on the filename (2025 since it's ListaCobroDetalle2025.csv)
# merged_df['year'] = '2025'

# # Organize columns in a logical order
# columns_order = [
#     'year', 'idListaCobro', 'idCredito', 'consecutivoCobro', 
#     'idBanco', 'NombreBanco', 'idEmisora', 'NombreEmisora',
#     'montoExigible', 'montoCobrar', 'montoCobrado', 
#     'fechaCobroBanco', 'idRespuestaBanco', 'DescripcionRespuesta',
#     'fechaCreacionLista', 'fechaEnvioCobro', 
#     'TipoEnvio', 'Emisora', 'idBancoEmisora', 'idBancoLista'
# ]

# # Reorder columns (only include columns that exist)
# available_columns = [col for col in columns_order if col in merged_df.columns]
# merged_df = merged_df[available_columns]

# Display the merged dataframe
# print(merged_df.head())

# Save to CSV file to view all data
print(merged_df.head())
merged_df.to_csv('full_merged_data.csv', index=False)
print("Full data saved to 'full_merged_data.csv'")



# print(cat_banco_df.head())
# print(cat_emisora_df.head())
# print(cat_respuesta_bancos_df.head())
# print(lista_cobro_df.head())
# print(lista_cobro_emisora_df.head())
# print(lista_cobro_detalle_df.head())







