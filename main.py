import datetime
from application.db.people import get_employes
from application.salary import calculate_salary
if __name__ == '__main__':
    get_employes()
    calculate_salary()
    print(datetime.date.today())


