import pandas as pd
import matplotlib.pyplot as plt
class Week13:
    def run(self):
        try:
            df = pd.read_csv('data.csv')
            data = pd.to_numeric(
                df.loc[df['status'] == 'ok', 'duration'],
                errors='coerce').dropna()
        except Exception:
            user_input = input("Введите значения duration через запятую: ")
            data = pd.to_numeric([x.strip() for x in user_input.split(',')],
                errors='coerce')
            data = pd.Series(data).dropna()
        plt.hist(data, bins='auto', edgecolor='black')
        plt.xlabel('duration')
        plt.ylabel('count')
        plt.title('duration histogram (ok)')
        plt.savefig('duration_histogram.png', format='png')
        plt.close()
if __name__ == "__main__":
    Week13().run()
#Мысал:10, 20, 30, 15, 50