import json, textwrap, os
import pandas as pd

class Turni:
    def __init__(self, csvName):
        self.urls = os.path.join(os.path.dirname(__file__), csvName)
        self.df = pd.read_csv(self.urls)



    def view_calendar(self):
        try: print(self.df)
        except: print('Something went wrong with the opening of the file')


    def add_preferences(self, name):
        options = ["m", "p", "s"]
        istruzioni ='''
            Seleziona una delle tre opzioni per indicare:
            m => 6-14
            p => 14-22
            s => 22-6
            Se non selezioni una delle tre opzioni verrà richiesta la domanda.
        '''
        print(textwrap.dedent(istruzioni))

        for column_name, value in self.df.loc[name].items():
            selection = ""
            time = "x"
            while True:
                selection = input(f"Quale preferenza ha {name} per {column_name}?: ")
                if selection in options: break
            if selection == 'm': time = "6-14"
            elif selection == 'p': time = "14-22"
            elif selection == 's': time = "22-6"
            else: print("Qualcosa è andato storto nell'elaborazione del programma")
            
            self.df.at[name, column_name] = time

        csv_data = self.df.loc[name].to_csv(sep=',', encoding='utf-8')
        with open(os.path.join(os.path.dirname(__file__),'calendario.csv'), 'a') as c: c.write(csv_data)



    def return_everyone_calendar(self):
        for index, row in self.df.iterrows(): self.add_preferences(index[0])
        self.view_calendar()
        csv_data = self.df.to_csv(sep=',', encoding='utf-8')
        with open(os.path.join(os.path.dirname(__file__),'calendario.csv'), 'w') as c: c.write(csv_data)



lavoratori_1 = Turni('turni.csv')
lavoratori_1.return_everyone_calendar()













""" turni_url = os.path.join(os.path.dirname(__file__), 'turni.csv')
turni_df = pd.read_csv(turni_url)

def view_calendar(calendar):
    try: print(calendar)
    except: print('Something went wrong with the opening of the file')

def add_preferences(calendar, name):
    options = ["m", "p", "s"]
    istruzioni ='''
        Seleziona una delle tre opzioni per indicare:
        m => 6-14
        p => 14-22
        s => 22-6
        Se non selezioni una delle tre opzioni verrà richiesta la domanda.
    '''
    print(textwrap.dedent(istruzioni))

    for column_name, value in calendar.loc[name].items():
        selection = ""
        time = "x"
        while True:
            selection = input(f"Quale preferenza ha {name} per {column_name}?: ")
            if selection in options: break
        if selection == 'm': time = "6-14"
        elif selection == 'p': time = "14-22"
        elif selection == 's': time = "22-6"
        else: print("Qualcosa è andato storto nell'elaborazione del programma")
        
        calendar.at[name, column_name] = time

    csv_data = calendar.loc[name].to_csv(sep=',', encoding='utf-8')
    with open(os.path.join(os.path.dirname(__file__),'calendario.csv'), 'a') as c: c.write(csv_data)
    
    


def return_everyone_calendar(calendar):
    for index, row in calendar.iterrows(): add_preferences(calendar, index[0])
    view_calendar(calendar)
    csv_data = calendar.to_csv(sep=',', encoding='utf-8')
    with open(os.path.join(os.path.dirname(__file__),'calendario.csv'), 'w') as c: c.write(csv_data)
            
    


return_everyone_calendar(turni_df)"""
