import load_big5_data as lbd
import matplotlib.pyplot as plt

big5data = lbd.s.connect("big5.db")
mycursor = big5data.cursor()

#why is this so huge
print(f'Average age is {mycursor.execute("SELECT AVG(age) FROM responses").fetchone()[0]}\n\n)')
print(f"Why is this so huge? Check for missing data commonly stored as a series of 9's.\n\n")
print(f'Average age is {mycursor.execute("SELECT AVG(age) FROM responses WHERE age <= 100").fetchone()[0]}\n\n')
print(f'There were {mycursor.execute("SELECT COUNT (*) FROM responses").fetchone()[0]} cases.')

mycursor.execute("ALTER TABLE responses ADD COLUMN extraversion_total INTEGER")

mycursor.execute("""
    UPDATE responses 
    SET extraversion_total = E1 + E2 + E3 + E4 + E5 + E6 + E7 + E8 + E9 + E10
""")

#since we changed the database
big5data.commit()

age_escore_plot_data = mycursor.execute("SELECT age,extraversion_total FROM responses WHERE age < 100").fetchall()

ages, escores = zip(*age_escore_plot_data)

plt.scatter(ages,escores)

plt.show()

big5.close()
