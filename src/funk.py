import pandas as pd
import pylab as plt
import seaborn as sns

class Funk:
    def check_nan(df: pd.DataFrame) -> None:
        """Recibe un dataframe y enseña % de valores nulos y la grafica"""
        nan_cols = df.isna().mean()  * 100  # porcentaje de nulo en cada columna
        
        display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
        display(nan_cols[nan_cols>0])
        
        # grafico de nulos en el dataframe
        plt.figure(figsize=(10, 6))  # inicia la figura y establece el tamaño
        
        sns.heatmap(df.isna(),   # datos
                    yticklabels=False,
                    cmap='viridis',
                    cbar=False
                   )
        
        plt.show();