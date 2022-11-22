string = '''
df_montag_mean = df_durchschnitt_montag['Super'].mean
df_montag_median = df_durchschnitt_montag['Super'].median
'''
days = ['montag', 'dienstag', 'mittwoch', 'donnnerstag', 'freitag', 'samstag', 'sonntag']
for i in days:
    print(f'"{i}":round(df_{i}_median(), 2),', end='')
    
    