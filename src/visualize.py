

import matplotlib.pyplot as plt
import seaborn as sns



def plot_confusion_matrix(cm):
    
        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu')
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.tight_layout()
        plt.show()


